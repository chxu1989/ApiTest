# coding=utf-8

import unittest
import HTMLTestRunner
from sendfunc import RunMain
import utils
import os

class TestRun(unittest.TestCase):
    def setUp(self):
      self.rm = RunMain()

    def test_run_single_testcase(self):
      testcase_filepath = os.
      pass


if __name__ =='__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestRun('test_01'))
    file_path = 'report/test_report.html'
    fp = open(file_path,'wb')
    reportRunner = HTMLTestRunner.HTMLTestRunner(
      stream=fp,
      title='SC system',
      description='测试报告')
    reportRunner.run(suite)