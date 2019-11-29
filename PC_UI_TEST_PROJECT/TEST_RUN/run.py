import os
import sys
sys.path.append("C:\\PC_UI_TEST_PROJECT")
sys.path.append("C:\\PC_UI_TEST_PROJECT\\TEST_CASES")
import unittest
from BSTestRunner import BSTestRunner
import time
import logging
import GL

test_dir = GL.TEST_CASES_DIR
report_dir = GL.REPORTS_DIR

for cirecle in range(1,2):
    try:
        # 加载测试用例
        # discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_pc_petrochina.py')
        # discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_petro_api.py')
        # discover = unittest.defaultTestLoader.discover(test_dir, pattern='*.py')
        discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_new_infonet.py')
        # 定义测试报告格式
        now = time.strftime("%Y-%m-%d %H_%M_%S")
        report_name = report_dir + '/' + now + 'test_report.html'
        # 运行并生成测试报告
        with open(report_name, 'wb') as file:
            runner = BSTestRunner(stream=file, title='new_infonet test report', description='new_infonet test report')
            logging.info('start run testcase...')
            runner.run(discover)
    except:
        continue