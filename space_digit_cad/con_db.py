# coding: utf-8
# @FileName: con_db.py
# @Time: 2022/7/16 15:59
# @Author: QHB

import psycopg2
from io import StringIO


class ConDb:
    def __init__(self, cad_entity_collections):
        self.entities = cad_entity_collections
        self.conn = psycopg2.connect(dbname="postgres", user="postgres", password="postgres")
        self.write_db()

    def write_db(self):
        # 将dataframe类型数据转换为IO缓冲区中的str类型数据
        output = StringIO()
        self.entities.to_csv(output, sep='\t', index=True, header=False)
        output1 = output.getvalue()
        print("output1", output1)
        # 创建cursor以访问数据库
        cur = self.conn.cursor()
        # 批量插入数据
        cur.copy_from(StringIO(output1), 'entity', null='')
        # 提交事务
        self.conn.commit()
        # 关闭连接
        self.conn.close()
