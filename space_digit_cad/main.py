# coding: utf-8
# @FileName: main.py
# @Time: 2022/7/18 12:39
# @Author: QHB

import pandas as pd
from space_digit_cad.read_cad import CadRead
from space_digit_cad.cad_parse import CadParse
from space_digit_cad.con_db import ConDb
from log_write import all_log, error_log

# 遍历所有DXF图纸, 解析图纸中的图元信息集合
cads_path = r'../cad_data/'
all_log.logger.info("图纸本地存放地址获取成功: -------------------------")
cad_msp_df = CadRead(cads_path).cad_msp_df
all_log.logger.info("所有图纸的图元信息获取完毕: -----------------------")
# 解析图元信息
all_log.logger.info("开始解析获取得到的图元信息: -----------------------")
cad_entity_collections = pd.DataFrame(CadParse(cad_msp_df).cad_entities_list)
all_log.logger.info("所有获取得到的图元信息均已解析完成: -----------------------")
# cad_entity_collections.to_csv('./cad.csv')
# 将解析得到的图元信息写入到PG数据库中
all_log.logger.info("开始将解析得到的数据存储入PG数据库: -----------------------")
ConDb(cad_entity_collections)
all_log.logger.info("数据已经被成功写入数据库中: -----------------------")
