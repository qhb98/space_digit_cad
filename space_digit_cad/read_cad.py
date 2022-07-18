# coding: utf-8
# @FileName: read_cad.py
# @Time: 2022/7/16 15:56
# @Author: QHB

import pandas as pd
import os
import ezdxf
from log_write import all_log, error_log


class CadRead:
    def __init__(self, cads_path):
        self.cads_path = cads_path
        self.cad_msp_df = self.read_cad()

    def read_cad(self):
        try:
            filenames = os.listdir(self.cads_path)
            cad_msp_list = []
            for filename in filenames:
                cad_path = os.path.join(self.cads_path, filename)
                all_log.logger.info("正在读取的CAD图纸文件的名称是: ", cad_path)
                # 读取cad dxf格式文件
                cad_doc = ezdxf.readfile(cad_path)
                # 遍历布局的所有DXF实体 modelspace是公共建筑空间
                msp = cad_doc.modelspace()
                all_log.logger.info(cad_path, "CAD图纸中的所有图元信息已被完全读取")
                cad_msp_list.append({cad_path: msp})
        except IOError as e:
            all_log.logger.error("图纸文件读取失败.", e)
        else:
            all_log.logger.info("读取的图纸文件的数量为: ", len(filenames))
            return pd.DataFrame(cad_msp_list)
