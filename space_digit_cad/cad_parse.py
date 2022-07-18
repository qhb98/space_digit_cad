# coding: utf-8
# @FileName: cad_parse.py
# @Time: 2022/7/16 15:58
# @Author: QHB

from shapely.geometry import LineString, Point
from log_write import all_log, error_log


class CadParse:
    def __init__(self, cad_msp_df):
        self.cad_msp_df = cad_msp_df
        self.cad_entities_list = []
        self.parse_start()

    def parse_start(self):
        for col, row in self.cad_msp_df.iteritems():
            drawing_name = col
            drawing_context = None
            try:
                for r in row.dropna():
                    if r is not None:
                        drawing_context = [entity for entity in r]
                all_log.logger.info("开始解析 ", drawing_name, " 图纸中所有类型图元的信息: ------------------")
                for entity in drawing_context:
                    # 提前设置内存空间存放不同类型的entity属性值
                    line_entity = None
                    text_entity = None
                    point_entity = None
                    insert_entity = None
                    if entity.dxf.dxftype == 'LINE':
                        line_list = self.add_entity(drawing_name, entity.dxf.layer, 'LINE', self.parse_line(entity).wkt,
                                                    text_entity, point_entity, insert_entity)
                        self.cad_entities_list.append(line_list)
                        # print("line", self.parse_line(entity))
                    elif entity.dxf.dxftype == 'INSERT':
                        insert_list = self.add_entity(drawing_name, entity.dxf.layer, 'INSERT', line_entity,
                                                      text_entity, point_entity, self.parse_insert(entity).wkt)
                        self.cad_entities_list.append(insert_list)
                        # print("insert", self.parse_insert(entity))
                    elif entity.dxf.dxftype == 'LWPOLYLINE':
                        line_list = self.add_entity(drawing_name, entity.dxf.layer, 'LWPOLYLINE',
                                                    self.parse_lwpolyline(entity).wkt,
                                                    text_entity, point_entity, insert_entity)
                        self.cad_entities_list.append(line_list)
                        # print("lwpolyline", self.parse_lwpolyline(entity))
                    elif entity.dxf.dxftype == 'TEXT':
                        text_list = self.add_entity(drawing_name, entity.dxf.layer, 'TEXT',
                                                    line_entity, self.parse_text(entity)[0],
                                                    self.parse_text(entity)[1].wkt,
                                                    insert_entity)
                        self.cad_entities_list.append(text_list)
                        # print("text", self.parse_text(entity))
                    else:
                        pass
            except Exception:
                error_log.logger.error("图元解析失败.", drawing_name, drawing_context)
            else:
                all_log.logger.info("解析出的图元数量为: ", len(self.cad_entities_list))

    @staticmethod
    def parse_text(entity):
        text_label = entity.dxf.text
        text_point = Point(entity.dxf.insert.x, entity.dxf.insert.y)
        return [text_label, text_point]

    @staticmethod
    def parse_lwpolyline(entity):
        x_list = []
        y_list = []
        for i in range(len(list(entity.lwpoints.values))):
            if i % 5 == 0:
                x_list.append(list(entity.lwpoints.values)[i])
            elif i % 5 == 1:
                y_list.append(list(entity.lwpoints.values)[i])
        point_list = zip(x_list, y_list)
        lwpolyline = LineString(point_list)
        return lwpolyline

    @staticmethod
    def parse_insert(entity):
        insert_point = Point(entity.dxf.insert.x, entity.dxf.insert.y)
        return insert_point

    @staticmethod
    def parse_line(entity):
        start_point = Point(entity.dxf.start.x, entity.dxf.start.y)
        end_point = Point(entity.dxf.end.x, entity.dxf.end.y)
        line = LineString([start_point, end_point])
        return line

    @staticmethod
    def add_entity(drawing_name, layer_name, entity_type, line, text, point, insert):
        return {
            "cad_name": drawing_name,
            "cad_layer_name": layer_name,
            "entity_type": entity_type,
            "line_entity": line,
            "text_entity": text,
            "point_entity": point,
            "insert_entity": insert
        }
