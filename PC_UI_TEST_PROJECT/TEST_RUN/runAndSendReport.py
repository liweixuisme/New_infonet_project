import os
import sys
sys.path.append("C:\\PC_UI_TEST_PROJECT")
sys.path.append("C:\\PC_UI_TEST_PROJECT\\TEST_CASES")
# sys.path.insert(0, "C:\\PC_UI_TEST_PROJECT\\TEST_CASES")
print(sys.path)
import GL
import unittest
from BSTestRunner import BSTestRunner
import time
import logging
from COMMONS.email_report import *
test_dir = GL.TEST_CASES_DIR
report_dir = GL.REPORTS_DIR



# 加载测试用例
# discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_pc_petrochina.py')
# discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_petro_api.py')
# discover = unittest.defaultTestLoader.discover(test_dir, pattern='*.py')
def run():
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_newinfonet.py')
    # 定义测试报告格式
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    report_name = report_dir + '/' + now + 'test_report.html'
    # 运行并生成测试报告
    with open(report_name, 'wb') as file:
        runner = BSTestRunner(stream=file, title='new_infonet test report', description='new_infonet test report')
        logging.info('start run testcase...')
        runner.run(discover)
    EmailReport().sendEmail(report_name)

if __name__ == '__main__':
    run()
