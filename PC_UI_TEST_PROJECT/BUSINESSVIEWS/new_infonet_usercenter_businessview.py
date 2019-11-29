# coding=UTF-8
from appium import webdriver
import os
import yaml
import logging
from logging import config
import warnings
from HTMLTestRunner import HTMLTestRunner
from selenium.webdriver.common.by import By
from COMMONS.common_function_pc_ui import ComMon
from COMMONS.pc_ui_desired_caps import pc_ui_start
from BUSINESSVIEWS.new_info_net_login_businessview import *
import time
import unittest
import GL

base_dir=os.path.dirname(os.path.dirname(__file__))

class New_InfoNet_UsercenterBusinessview(ComMon,unittest.TestCase):
    with open(GL.DATAS_DIR + '/new_infonet_elements.yaml', encoding='utf-8') as file:
        data = yaml.load(file)

    def UpLoadFood(self,**dict):
        # dict = {
        #     "photo_path": "photo_path",
        #     "name": "name",
        #     "price":"price",
        #     "guige":"guige",
        #     "buylink":"buylink",
        #     "describe":"describe",
        #     "page_name":"page_name"
        # }
        for key in dict:
            print(dict[key])
        # a.upploadfood(*list,**dict)
        # --->
        #     for key in dict:
        #         eval("self.Input(page['%s_input_GPS'],page['%s_input'],%s_path)"%(key,key,key))
        # for key in dict:
        #     eval("self.Input(page['%s_input_GPS'],page['food_photo_input'],food_photo_path)"%())

    def userCenterGetInto(self,**dict):
        page = self.data[dict["page_name"]]
        self.Click(page['user_center_a_GPS'],page['user_center_a'])
        self.out_log("get into user_center")
        self.wait(60)
        self.sleep(30)
        msg="userCenterGetInto success"
        return msg

    def uploadFoodGetInto(self,**dict):
        page = self.data[dict["page_name"]]
        self.Click(page['upload_food_a_GPS'],page['upload_food_a'])
        self.out_log("get into usercenter>uploadfood to upload food")
        self.wait(60)
        self.sleep(40)
        # self.Click(page['En_launage_button_GPS'],page['En_launage_button'])
        msg="uploadFoodGetInto success"
        return msg

    def uploadFood(self,**dict):
        path=dict['path']
        name=dict['name']
        price=dict['price']
        guige=dict['guige']
        buylink=dict['buylink']
        detail=dict['detail']
        page = self.data[dict["page_name"]]
        self.Input(page['food_photo_input_GPS'],page['food_photo_input'],path)
        self.sleep(2)
        self.Input(page['food_name_input_GPS'],page['food_name_input'],name)
        self.Input(page['food_price_input_GPS'],page['food_price_input'],price)
        self.Input(page['food_guige_input_GPS'],page['food_guige_input'],guige)
        self.Input(page['food_buylink_input_GPS'],page['food_buylink_input'],buylink)
        self.Input(page['food_detail_input_GPS'],page['food_detail_input'],detail)
        self.Click(page['food_foodcategory_select_GPS'],page['food_foodcategory_select'])
        self.sleep(5)
        self.Click(page['food_seafood_FAN_span_GPS'],page['food_seafood_FAN_span'])
        self.Click(page['food_category_select_GPS'],page['food_category_select'])
        self.sleep(5)
        self.Click(page['food_design_FAN_span_GPS'],page['food_design_FAN_span'])
        self.Click(page['food_orginplace_select_GPS'],page['food_orginplace_select'])
        self.sleep(5)
        self.Click(page['food_country_brazi_FAN_span_GPS'],page['food_country_brazi_FAN_span'])
        self.Click(page['food_yewuleixing_select_GPS'],page['food_yewuleixing_select'])
        self.swipe_bar()
        self.Click(page['food_xieyi_checkbox_GPS'],page['food_xieyi_checkbox'])
        self.Click(page['food_save_button_GPS'],page['food_save_button'])
        msg = "uploadFood success"
        return msg

    def jobseekerInfoGetInto(self,**dict):
        page = self.data[dict["page_name"]]
        self.Click(page['jobseeker_info_goto_a_GPS'],page['jobseeker_info_goto_a'])
        self.out_log("get into usercenter>jobseeker_info to upload jobseeker_info")
        self.wait(60)
        self.sleep(40)
        # self.Click(page['En_launage_button_GPS'],page['En_launage_button'])
        msg = "jobseekerInfoGetInto success"
        return msg

    def uploadJobseekerInfo(self,**dict):
        name=dict['name']
        phone=dict['phone']
        email=dict['email']
        detail=dict['detail']
        experience=dict['experience']
        page = self.data[dict["page_name"]]
        self.Input(page['jobseeker_info_name_input_GPS'],page['jobseeker_info_name_input'],name)
        self.sleep(2)
        self.Input(page['jobseeker_info_phone_input_GPS'],page['jobseeker_info_phone_input'],phone)
        self.Input(page['jobseeker_info_email_input_GPS'],page['jobseeker_info_email_input'],email)
        self.swipe_bar()
        self.sleep(2)

        self.Click(page['jobseeker_info_zhuanye_area_input_GPS'],page['jobseeker_info_zhuanye_area_input'])
        self.wait(10)
        self.sleep(3)
        self.Click(page['jobseeker_info_zhuanye_area_law_input_GPS'],page['jobseeker_info_zhuanye_area_law_input'])
        self.Click(page['jobseeker_info_zhuanye_area_input_GPS'],page['jobseeker_info_zhuanye_area_input'])
        self.wait(10)
        self.sleep(3)

        self.Click(page['jobseeker_info_country_input_GPS'],page['jobseeker_info_country_input'])
        self.wait(30)
        self.sleep(3)
        self.Click(page['jobseeker_info_country_brazi_input_GPS'],page['jobseeker_info_country_brazi_input'])
        self.Click(page['jobseeker_info_country_input_GPS'],page['jobseeker_info_country_input'])
        self.wait(10)
        self.sleep(3)

        self.Click(page['jobseeker_info_nowlive_area_input_GPS'],page['jobseeker_info_nowlive_area_input'])
        self.wait(30)
        self.sleep(3)
        self.Click(page['jobseeker_info_nowlive_area_brazi_input_GPS'],page['jobseeker_info_nowlive_area_brazi_input'])
        self.wait(10)
        self.sleep(3)



        self.Input(page['jobseeker_info_person_say_textarea_GPS'],page['jobseeker_info_person_say_textarea'],detail)
        self.Input(page['jobseeker_info_person_experience_textarea_GPS'],page['jobseeker_info_person_experience_textarea'],experience)
        self.Click(page['jobseeker_info_save_button_GPS'],page['jobseeker_info_save_button'])

        msg = "uploadJobseekerInfo success"
        return msg

    def supplierInfoGetInto(self,**dict):
        page = self.data[dict["page_name"]]
        self.Click(page['supplier_info_goto_a_GPS'],page['supplier_info_goto_a'])
        self.out_log("get into usercenter>supplier_info to upload supplier_info")
        self.wait(60)
        self.sleep(5)
        # self.Click(page['En_launage_button_GPS'],page['En_launage_button'])
        msg = "supplierInfoGetInto success"
        return msg

    def uploadFoodSupplierInfo(self,):
        path=dict['path']
        company_name=dict['company_name']
        connector=dict['connector']
        email=dict['email']
        phone=dict['phone']
        website=dict['website']
        address=dict['address']
        edm_code=dict['edm_code']
        introduce=dict['introduce']
        page = self.data[dict["page_name"]]
        self.Input(page['foodsupplier_info_photo_GPS'],page['foodsupplier_info_photo'],path)
        self.sleep(3)
        self.Click(page['foodsupplier_info_identity_select_GPS'],page['foodsupplier_info_identity_select'])
        self.wait(10)
        self.sleep(3)
        self.Click(page['foodsupplier_info_apily_span_GPS'],page['foodsupplier_info_apily_span'])
        self.Click(page['foodsupplier_info_country_select_GPS'],page['foodsupplier_info_country_select'])
        self.wait(10)
        self.sleep(3)
        self.Click(page['foodsupplier_info_country_brazi_span_GPS'],page['foodsupplier_info_country_brazi_span'])
        self.Input(page['foodsupplier_info_company_name_input_GPS'],page['foodsupplier_info_company_name_input'],company_name)
        self.Input(page['foodsupplier_info_contector_name_input_GPS'],page['foodsupplier_info_contector_name_input'],connector)
        self.Input(page['foodsupplier_info_email_input_GPS'],page['foodsupplier_info_email_input'],email)
        self.Input(page['foodsupplier_info_phone_input_GPS'],page['foodsupplier_info_phone_input'],phone)
        self.Click(page['foodsupplier_info_chuanzhen_select_GPS'],page['foodsupplier_info_chuanzhen_select'])
        self.wait(10)
        self.sleep(3)
        self.Click(page['foodsupplier_info_chuanzhen_86_span_GPS'],page['foodsupplier_info_chuanzhen_86_span'])
        self.Input(page['foodsupplier_info_chuanzhen_num_input_GPS'],page['foodsupplier_info_chuanzhen_num_input'],phone)
        self.Input(page['foodsupplier_info_website_input_GPS'],page['foodsupplier_info_website_input'],website)
        self.swipe_bar()
        self.sleep(3)
        self.Input(page['foodsupplier_info_connect_address_input_GPS'],page['foodsupplier_info_connect_address_input'],address)
        self.Click(page['foodsupplier_info_hire_num_select_GPS'],page['foodsupplier_info_hire_num_select'])
        self.wait(10)
        self.sleep(3)
        self.Click(page['foodsupplier_info_hire_50_150_span_GPS'],page['foodsupplier_info_hire_50_150_span'])
        self.Input(page['foodsupplier_info_family_phone_input_GPS'],page['foodsupplier_info_family_phone_input'],phone)
        self.Input(page['foodsupplier_info_registe_code_input_GPS'],page['foodsupplier_info_registe_code_input'],phone)
        self.Input(page['foodsupplier_info_edm_code_input_GPS'],page['foodsupplier_info_edm_code_input'],edm_code)
        self.Click(page['foodsupplier_info_yewu_type_span_GPS'],page['foodsupplier_info_yewu_type_span'])
        self.Input(page['foodsupplier_info_company_introduce_textarea_GPS'],page['foodsupplier_info_company_introduce_textarea'],introduce)
        self.Click(page['foodsupplier_info_save_button_GPS'],page['foodsupplier_info_save_button'])
        msg = "uploadFoodSupplierInfo success"
        return msg

    def uploadServiceSupplierInfo(self,**dict):
        path=dict['path']
        company_name=dict['company_name']
        connector=dict['connector']
        career=dict['career']
        email=dict['email']
        phone=dict['phone']
        website=dict['website']
        address=dict['address']
        money=dict['money']
        market=dict['market']
        introduce=dict['introduce']
        page = self.data[dict["page_name"]]
        self.Input(page['servicesupplier_info_photo_GPS'],page['servicesupplier_info_photo'],path)
        self.sleep(3)
        self.Input(page['servicesupplier_info_company_name_input_GPS'],page['servicesupplier_info_company_name_input'],company_name)
        self.Input(page['servicesupplier_info_contector_name_input_GPS'],page['servicesupplier_info_contector_name_input'],connector)
        self.Input(page['servicesupplier_info_career_input_GPS'],page['servicesupplier_info_career_input'],career)
        self.Input(page['servicesupplier_info_email_input_GPS'],page['servicesupplier_info_email_input'],email)
        self.Input(page['servicesupplier_info_phone_input_GPS'],page['servicesupplier_info_phone_input'],phone)
        self.Click(page['servicesupplier_info_country_select_GPS'],page['servicesupplier_info_country_select'])
        self.wait(10)
        self.sleep(3)
        self.Click(page['servicesupplier_info_country_brazi_span_GPS'],page['servicesupplier_info_country_brazi_span'])
        self.wait(10)
        self.sleep(3)
        self.Click(page['servicesupplier_info_belong_hangye_select_GPS'],page['servicesupplier_info_belong_hangye_select'])
        self.wait(10)
        self.sleep(3)
        self.Click(page['servicesupplier_info_belong_hangye_law_span_GPS'],page['servicesupplier_info_belong_hangye_law_span'])
        self.sleep(3)
        self.Input(page['servicesupplier_info_chuanzhen_num_input_GPS'],page['servicesupplier_info_chuanzhen_num_input'],phone)
        self.Input(page['servicesupplier_info_website_input_GPS'],page['servicesupplier_info_website_input'],website)
        self.swipe_bar()
        self.sleep(3)
        self.Input(page['servicesupplier_info_connect_address_input_GPS'],page['servicesupplier_info_connect_address_input'],address)
        self.Click(page['servicesupplier_info_year_select_GPS'],page['servicesupplier_info_year_select'])
        self.wait(10)
        self.sleep(3)
        self.Click(page['servicesupplier_info_year_2019_span_GPS'],page['servicesupplier_info_year_2019_span'])
        self.Click(page['servicesupplier_info_hire_num_select_GPS'],page['servicesupplier_info_hire_num_select'])
        self.wait(10)
        self.sleep(3)
        self.Click(page['servicesupplier_info_hire_50_150_span_GPS'],page['servicesupplier_info_hire_50_150_span'])
        self.Input(page['servicesupplier_info_money_per_year_input_GPS'],page['servicesupplier_info_money_per_year_input'],money)
        self.Input(page['servicesupplier_info_main_market_input_GPS'],page['servicesupplier_info_main_market_input'],market)
        self.Input(page['servicesupplier_info_company_introduce_textarea_GPS'],page['servicesupplier_info_company_introduce_textarea'],introduce)
        self.Click(page['foodsupplier_info_save_button_GPS'],page['foodsupplier_info_save_button'])
        msg = "uploadServiceSupplierInfo success"
        return msg

if __name__ == '__main__':
    driver=pc_ui_start()
    L=New_info_net_login_businessview(driver)

    # driver=pc_ui_start()
    # L=New_info_net_login_businessview(driver)
    # url="http://infonet.new.bringbuys.com/login?lang=zht"
    # L.get_url(url)
    # L.maximize_window()
    # L.new_info_net_login("LW_foodsupplier6","abc123456","login_page")
    # L=New_info_net_usercenter_businessview(driver)
    # L.new_info_net_usercenter_get_into('user_center_page')

    # L.new_info_net_uploadfood_get_into('user_center_page')
    # L.new_info_net_uploadfood("C:\PC_UI_TEST_PROJECT\DATAS\photos\\food_photo1.jpg","LW_前台测试食品上传01测试繁体","32","123321","www.baidu.com","lw_商品详情繁体",'user_center_page')

    # foodsupplier_photo_path="C:\PC_UI_TEST_PROJECT\DATAS\photos\\food_photo1.jpg"
    # website='www.baidu.com'
    # address='LW联系地址繁'
    # company_introduce='LW_公司 简介 描述 繁体'
    # L.new_info_net_supplier_info_get_into('user_center_page')
    # L.new_info_net_upload_food_supplier_info(foodsupplier_photo_path,"LW_前台食品供应商上传01测试繁体","liwei.xu繁","977820015@qq.com","13229794612",website,address,"515535",company_introduce,'user_center_page')

