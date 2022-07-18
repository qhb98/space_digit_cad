# coding: utf-8
# @FileName: con_db.py
# @Time: 2022/7/16 15:59
# @Author: QHB

import psycopg2

conn = psycopg2.connect(dbname="postgres", user="postgres", password="postgres")
# 创建cursor以访问数据库
cur = conn.cursor()
