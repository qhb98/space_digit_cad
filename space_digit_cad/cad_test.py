# coding: utf-8
# @FileName: cad_test.py
# @Time: 2022/7/18 19:46
# @Author: QHB


import unittest
import HTMLTestRunner
import time


class Test(unittest.TestCase):
    def setUp(self) -> None:
        # 每个测试方法前执行
        print("setUp方法")

    def tearDown(self) -> None:
        # 每个测试方法后执行
        print("tearDown方法")

    @classmethod
    def setUpClass(cls) -> None:
        print("setUpClass每个类执行一次")

    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDownClass每个类执行一次")

    def test_01(self):
        a = 1
        b = 2
        c = a + b
        self.assertEqual(c, 3)

    def test_02(self):
        a = 2
        b = 3
        c = a * b
        self.assertEqual(c, 5, "不相等")


if __name__ == '__main__':

    test_dir = './'
    # test_dir为要指定的目录 ./为当前目录；pattern：为查找的.py文件的格式
    discover = unittest.defaultTestLoader.discover(test_dir,pattern='test_*.py')
    # 定义报告目录
    file_dir = "./report/"
    # 定义报告名称格式
    now_time = time.strftime("%Y-%m-%d %H_%M_%S")
    # 报告完整路径和名称
    file_name = file_dir + now_time + "Report.html"