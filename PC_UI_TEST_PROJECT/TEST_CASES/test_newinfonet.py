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
import sys
from COMMONS.pc_ui_desired_caps import pc_ui_start
from BUSINESSVIEWS.new_info_net_login_businessview import New_info_net_login_businessview
from BUSINESSVIEWS.new_info_net_register_user_businessview import *
from BUSINESSVIEWS.new_info_net_usercenter_businessview import *
import GL

base_dir=os.path.dirname(os.path.dirname(__file__))
# sys.path.insert(0, 'C:\\PC_UI_TEST_PROJECT\\TEST_CASES\\test_newinfonet.py')

class Test_case(unittest.TestCase):
    with open(GL.DATAS_DIR + '/new_infonet_elements.yaml', encoding='utf-8') as file:
        data = yaml.load(file)
    url = "https://web.infonet2.bringbuys.com/login?lang=zht"

    def setUp(self):
        logging.info('===setup====')
        self.driver =pc_ui_start()

    #@unittest.skip("上传食品")
    def test_new_infonet_upload_food(self):
        L = New_info_net_login_businessview(self.driver)
        url = "http://infonet.new.bringbuys.com/login?lang=zht"
        L.get_url(url)
        L.maximize_window()
        L.new_info_net_login("LW_foodsupplier6", "abc123456", "login_page")
        L = New_info_net_usercenter_businessview(self.driver)
        L.new_info_net_usercenter_get_into('user_center_page')
        L.new_info_net_uploadfood_get_into('user_center_page')
        now = int(time.time())
        # 转换为其他日期格式,如:"%Y-%m-%d %H:%M:%S"
        timeStruct = time.localtime(now)
        strTime = time.strftime("%Y-%m-%d %H:%M:%S", timeStruct)
        var_food_name="LW_前台测试食品繁体"+ str(strTime)
        L.new_info_net_uploadfood("C:\\PC_UI_TEST_PROJECT\\DATAS\\photos\\food_photo1.jpg", var_food_name, "32","123321", "www.baidu.com", "lw_商品详情繁体", 'user_center_page')

    @unittest.skip("注册 个人用户 jobseeker")
    def test_new_infonet_register_jobseeker(self):
        L = New_info_net_register_user_businessview(self.driver)
        url = "http://infonet.new.bringbuys.com/login?lang=zht"
        L.get_url(url)
        L.maximize_window()
        L.new_info_net_register_get_into("register_page")
        L.new_info_net_register_job_seeker_get_into("register_page")
        strTime = int(time.time())
        var_jobseeker_name="LW_font_register_jobseeker"+ str(strTime)
        L.new_info_net_register_jobseeker(var_jobseeker_name, "2321628281@qq.com","fanxiangyunjisuanhahaha", "abc123456", "register_page")

    # @unittest.skip("注册 个人用户 jobseeker 并上传人才资料")
    def test_new_infonet_upload_jobseeker_info(self):
        L = New_info_net_register_user_businessview(self.driver)
        url = "http://infonet.new.bringbuys.com/login?lang=zht"
        L.get_url(url)
        L.maximize_window()
        L.new_info_net_register_get_into("register_page")
        strTime = int(time.time())
        L.new_info_net_register_job_seeker_get_into("register_page")
        var_job_seeker_name = "LW_font_register_jobseeker" + str(strTime)
        L.new_info_net_register_jobseeker(var_job_seeker_name, "2321628281@qq.com", "fanxiangyunjisuanhahaha","abc123456", "register_page")
        L = New_info_net_login_businessview(self.driver)
        L.new_info_net_goto_login("login_page")
        L.new_info_net_login(var_job_seeker_name, "abc123456", "login_page")
        L = New_info_net_usercenter_businessview(self.driver)
        L.new_info_net_usercenter_get_into("user_center_page")
        L.new_info_net_jobseeker_info_get_into("user_center_page")
        now = int(time.time())
        timeStruct = time.localtime(now)
        strTime = time.strftime("%Y-%m-%d %H:%M:%S", timeStruct)
        var_jobseeker_name="LW_liwei.xu"+ str(strTime)
        L.new_info_net_upload_jobseeker_info(var_jobseeker_name, "13229794612", "2321628281@qq.com", "lw_个人简述繁体", "lw_个人职业经历繁体","user_center_page")

    #@unittest.skip("注册 食品供应商 foodsupplier 并上传 食品供应商基本信息")
    def test_new_infonet_upload_foodsupplier_info(self):
        L = New_info_net_register_user_businessview(self.driver)
        url = "http://infonet.new.bringbuys.com/login?lang=zht"
        L.get_url(url)
        L.maximize_window()
        L.new_info_net_register_get_into("register_page")
        strTime = int(time.time())
        L.new_info_net_register_supplier_get_into("register_page")
        var_foodsupplier_name = "LW_font_register_foodsupplier" + str(strTime)
        L.new_info_net_register_supplier(var_foodsupplier_name,"390485519@qq.com",var_foodsupplier_name+"_company","food_supplier","fanxiangyunjisuanhahaha","abc123456", "register_page")
        L = New_info_net_login_businessview(self.driver)
        L.new_info_net_goto_login("login_page")
        L.new_info_net_login(var_foodsupplier_name, "abc123456", "login_page")
        L = New_info_net_usercenter_businessview(self.driver)
        L.new_info_net_usercenter_get_into("user_center_page")
        L.new_info_net_supplier_info_get_into("user_center_page")
        now = int(time.time())
        timeStruct = time.localtime(now)
        strTime = time.strftime("%Y-%m-%d %H:%M:%S", timeStruct)
        var_foodsupplier_name="LW_前台测试食品供应商繁体"+ str(strTime)
        foodsupplier_photo_path = "C:\PC_UI_TEST_PROJECT\DATAS\photos\\food_photo1.jpg"
        website = 'www.baidu.com'
        address = 'LW联系地址繁'
        company_introduce = 'LW_公司 简介 描述 繁体'
        L.new_info_net_supplier_info_get_into('user_center_page')
        L.new_info_net_upload_food_supplier_info(foodsupplier_photo_path,var_foodsupplier_name, "liwei.xu繁","390485519@qq.com", "13229794612", website, address, "515535",company_introduce, 'user_center_page')

    #@unittest.skip("注册 专业服务商 service_supplier 并上传 专业服务商基本信息")
    def test_new_infonet_upload_servicesupplier_info(self):
        L = New_info_net_register_user_businessview(self.driver)
        url = "http://infonet.new.bringbuys.com/login?lang=zht"
        L.get_url(url)
        L.maximize_window()
        L.new_info_net_register_get_into("register_page")
        strTime = int(time.time())
        L.new_info_net_register_supplier_get_into("register_page")
        var_service_supplier_name = "LW_font_register_service_supplier" + str(strTime)
        L.new_info_net_register_supplier(var_service_supplier_name,"13229794612@163.com",var_service_supplier_name+"_company","service_supplier","fanxiangyunjisuanhahaha","abc123456", "register_page")
        L = New_info_net_login_businessview(self.driver)
        L.new_info_net_goto_login("login_page")
        L.new_info_net_login(var_service_supplier_name, "abc123456", "login_page")
        L = New_info_net_usercenter_businessview(self.driver)
        L.new_info_net_usercenter_get_into("user_center_page")
        L.new_info_net_supplier_info_get_into("user_center_page")
        now = int(time.time())
        timeStruct = time.localtime(now)
        strTime = time.strftime("%Y-%m-%d %H:%M:%S", timeStruct)
        var_service_supplier_name="LW_前台测试专业服务商繁体"+ str(strTime)
        service_supplier_photo_path="C:\PC_UI_TEST_PROJECT\DATAS\photos\\food_photo1.jpg"
        website='www.baidu.com'
        address='LW联系地址繁'
        company_introduce='LW_公司 简介 描述 繁体'
        L.new_info_net_supplier_info_get_into('user_center_page')
        L.new_info_net_upload_service_supplier_info(service_supplier_photo_path,var_service_supplier_name,"liwei.xu繁","lw_career繁体","13229794612@163.com","13229794612",website,address,"50000000","中国市场",company_introduce,'user_center_page')


    def tearDown(self):
        logging.info('====tearDown====')
        time.sleep(5)
        self.driver.quit()

if __name__ == '__main__':
    for i in range(1,2):
        unittest.main()

