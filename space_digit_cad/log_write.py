# coding: utf-8
# @FileName: log_write.py
# @Time: 2022/7/18 17:14
# @Author: QHB

# 日志参考链接: https://zdyxry.github.io/2018/07/22/%E8%AF%91-python-logging-%E6%9C%80%E4%BD%B3%E5%AE%9E%E8%B7%B5/

import logging
from logging import FileHandler


class Logger(object):
    def __init__(self, filename, level='debug', fmt='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'):
        # 日志级别关系映射
        self.level_relations = {
            'debug': logging.DEBUG,
            'info': logging.INFO,
            'warning': logging.WARNING,
            'error': logging.ERROR,
            'critical': logging.CRITICAL
        }
        self.logger = logging.getLogger(filename)
        # 设置日志级别
        self.logger.setLevel(self.level_relations.get(level))
        # 往文件里写入
        handler = FileHandler(filename=filename, encoding='utf-8')
        # 设置写入日志的级别
        handler.setLevel(self.level_relations.get(level))
        # 设置日志格式
        format_str = logging.Formatter(fmt)
        handler.setFormatter(format_str)
        # 把对象加到logger里
        self.logger.addHandler(handler)


# 生成日志, 并写入到日志文件中
all_log = Logger('../log_record/all.log', level='warning')
error_log = Logger('../log_record/error.log', level='error')
