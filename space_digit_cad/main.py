# coding: utf-8
# @FileName: main.py
# @Time: 2022/7/18 12:39
# @Author: QHB

import pandas as pd
from space_digit_cad.read_cad import CadRead
from space_digit_cad.cad_parse import CadParse
from space_digit_cad.con_db import ConDb


# 遍历所有DXF图纸, 解析图纸中的图元信息集合
cads_path = r'../cad_data/'
cad_msp_df = CadRead(cads_path).cad_msp_df
# 解析图元信息
cad_entity_collections = pd.DataFrame(CadParse(cad_msp_df).cad_entities_list)
cad_entity_collections.to_csv('./cad.csv')
# 将解析得到的图元信息写入到PG数据库中
ConDb(cad_entity_collections)
