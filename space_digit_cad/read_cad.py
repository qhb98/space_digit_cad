# coding: utf-8
# @FileName: read_cad.py
# @Time: 2022/7/16 15:56
# @Author: QHB

import pandas as pd
import os
import ezdxf
import logging


class CadRead:
    def __init__(self, cads_path):
        self.cads_path = cads_path
        self.cad_msp_df = self.read_cad()

    def read_cad(self):
        filenames = os.listdir(self.cads_path)
        cad_msp_list = []
        for filename in filenames:
            cad_path = os.path.join(self.cads_path, filename)
            logging.info("正在读取的CAD图纸文件的名称是: ", cad_path)
            # 读取cad dxf格式文件
            cad_doc = ezdxf.readfile(cad_path)
            # 遍历布局的所有DXF实体 modelspace是公共建筑空间
            msp = cad_doc.modelspace()
            cad_msp_list.append({cad_path: msp})
        return pd.DataFrame(cad_msp_list)
