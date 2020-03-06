import test_runner
import os
import utils

def test_run_single_testcase_success(self):
    testcase_filepath = os.path.join(os.getcwd(), 'tests/data/demo.json')
    testcases = utils.load_testcases(testcase_filepath)
    success, _ = self.test_runner.run_single_testcase(testcases[0])
    self.assertTrue(success)