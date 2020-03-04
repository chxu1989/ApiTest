# coding=utf-8

import unittest
import HTMLTestRunner
from sendfunc import RunMain

class TestRun(unittest.TestCase):
    def setUp(self):
      self.rm = RunMain()

    def test_01(self):
        url = 'https://gov-admin-test.zcloud.ac.cn/#/login'
        res = self.rm.run('get',url)
        print(res)
        self.(res.['status_code'], 200, "测试通过")


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