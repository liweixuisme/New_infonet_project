# coding=UTF-8
import os
import yaml
import time
import warnings
import unittest
import datetime
import random
import string
import logging
from COMMONS.pc_ui_desired_caps import pc_ui_start
from BUSINESSVIEWS.pc_login_businessview import Pc_login_businessview
from BUSINESSVIEWS.pc_store_businessview import Pc_petrochina_store_businessview
import GL

base_dir=os.path.dirname(os.path.dirname(__file__))

class Test_case(unittest.TestCase):
    with open(GL.DATAS_DIR + '/elements_data.yaml', encoding='utf-8') as file:
        data = yaml.load(file)
#PC中石油 测试环境的网址
    url = "https://petrochina-data-test.esmart365.com"
#商品excel文件的路径
    goods_excel_path = data['pc_good_improt_goods_path']

    def setUp(self):
        logging.info('===setup====')
        self.driver =pc_ui_start()

    # @unittest.skip("编辑门店信息")
    def test_pc_c_store_edit(self):
        store_name = "lwlw_在们。现，及他王"
        contator = 'ytf 许立伟ns'
        number_current_time = lambda: int(round(time.time() * 0.01))
        login_phone = str("187" + str(number_current_time()))
        sn = "1553136557023"
        province = '广东省'
        city = '珠海市'
        county = '香洲区'
        address = '横琴区创意谷7栋 Mr.Xu'
        L = Pc_login_businessview(self.driver)
        L.get_url(self.url)
        L.maximize_window()
        L.pc_petrochina_login("uSmileAdmin","usmile2018","pc_petro_login_page")
        L = Pc_petrochina_store_businessview(self.driver)
        L.pc_storelist_get_into()
        L.pc_store_searchstore(str(store_name))
        L.pc_store_edit_get_into()
        judge_text=L.pc_store_edit(store_name, contator, sn, province, city, county, str(address)+str(login_phone)+"编辑成功")
        self.assertEqual(str(judge_text), "修改店铺成功", "断言结果应该是 修改店铺成功，实际为： "+str(judge_text))

    def tearDown(self):
        logging.info('====tearDown====')
        time.sleep(5)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

