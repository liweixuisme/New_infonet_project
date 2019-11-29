# coding=UTF-8
from selenium import webdriver
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
from BUSINESSVIEWS.new_info_net_usercenter_businessview import *
import time
import GL

base_dir=os.path.dirname(os.path.dirname(__file__))

class New_InfoNet_RegisterUserBusinessview(ComMon):
    with open(GL.DATAS_DIR + '/new_infonet_elements.yaml', encoding='utf-8') as file:
        data = yaml.load(file)


    def registerGetInto(self,**dict):
        page = self.data[dict["page_name"]]
        self.out_log("get into register select page")
        self.Click(page['job_seeker_register_for_free_button_GPS'],page['job_seeker_register_for_free_button'])
        self.wait(60)
        self.sleep(10)
        msg="registerGetInto success"
        return msg

    def registerJobSeekerGetInto(self,**dict):
        page = self.data[dict["page_name"]]
        self.Click(page['job_seeker_goto_register_button_GPS'],page['job_seeker_goto_register_button'])
        self.out_log("get into register jobseeker page")
        self.wait(60)
        self.sleep(10)
        msg="registerJobSeekerGetInto success"
        return msg

    def registerSupplierGetInto(self,**dict):
        page = self.data[dict["page_name"]]
        self.Click(page['supplier_goto_register_button_GPS'],page['supplier_goto_register_button'])
        self.out_log("get into register supplier page")
        self.wait(60)
        self.sleep(10)
        msg="registerSupplierGetInto success"
        return msg

    def registerJobseeker(self,**dict):
        name=dict["name"]
        email=dict["email"]
        code=dict["code"]
        password=dict["password"]
        page = self.data[dict["page_name"]]
        self.Input(page['job_seeker_register_name_input_GPS'],page['job_seeker_register_name_input'],name)
        self.sleep(2)
        self.Input(page['job_seeker_register_email_input_GPS'],page['job_seeker_register_email_input'],email)
        self.Input(page['job_seeker_register_code_input_GPS'],page['job_seeker_register_code_input'],code)
        self.Input(page['job_seeker_register_password_input_GPS'],page['job_seeker_register_password_input'],password)
        self.Input(page['job_seeker_register_again_password_input_GPS'],page['job_seeker_register_again_password_input'],password)
        self.Click(page['job_seeker_register_agree_xieyi_checkbox_GPS'],page['job_seeker_register_agree_xieyi_checkbox'])
        self.sleep(3)
        self.Click(page['job_seeker_register_register_button_GPS'],page['job_seeker_register_register_button'])
        self.wait(60)
        self.sleep(10)
        msg="registerJobseeker success"
        return msg

    def registerSupplier(self,**dict):
        name = dict["name"]
        email = dict["email"]
        company_name = dict["company_name"]
        type = dict["type"]
        code = dict["code"]
        password = dict["password"]
        page_name = self.data[dict["page_name"]]
        self.Input(page_name['supplier_register_name_input_GPS'],page_name['supplier_register_name_input'],name)
        self.sleep(2)
        self.Input(page_name['supplier_register_email_input_GPS'],page_name['supplier_register_email_input'],email)
        self.Input(page_name['supplier_register_company_name_input_GPS'],page_name['supplier_register_company_name_input'],company_name)
        if type=="food_supplier":
            self.Click(page_name['supplier_register_foodsupplier_span_GPS'],page_name['supplier_register_foodsupplier_span'])
        elif type=="service_supplier":
            self.Click(page_name['supplier_register_service_supplier_span_GPS'],page_name['supplier_register_service_supplier_span'])
        elif type=="both":
            self.Click(page_name['supplier_register_both_food_and_service_supplier_span_GPS'],page_name['supplier_register_both_food_and_service_supplier_span'])
        self.Input(page_name['supplier_register_code_input_GPS'],page_name['supplier_register_code_input'],code)
        self.Input(page_name['job_seeker_register_password_input_GPS'],page_name['job_seeker_register_password_input'],password)
        self.Input(page_name['supplier_register_again_password_input_GPS'],page_name['supplier_register_again_password_input'],password)
        self.Click(page_name['supplier_register_agree_xieyi_checkbox_GPS'],page_name['supplier_register_agree_xieyi_checkbox'])
        self.sleep(3)
        self.Click(page_name['job_seeker_register_register_button_GPS'],page_name['job_seeker_register_register_button'])
        msg="registerSupplier success"
        return msg

if __name__ == '__main__':

    driver=pc_ui_start()
    L=New_InfoNet_RegisterUserBusinessview(driver)
    url="http://infonet.new.bringbuys.com/login?lang=zht"
    L.get_url(url)
    L.maximize_window()

    dict1={
        "page_name":"register_page"
    }
    msg=L.registerGetInto(**dict1)
    print(msg)


    # msg=L.jobSeekerGetInto(**dict1)
    # print(msg)
    #
    # strTime = int(time.time())
    # job_seeker_name = "LwFontRegisterJobseeker_" + str(strTime)
    # dict2={
    #     "name": job_seeker_name,
    #     "email": "2321628281@qq.com",
    #     "code": "fanxiangyunjisuanhahaha",
    #     "password": "abc123456",
    #     "page_name":"register_page"
    # }
    # msg=L.registerJobseeker(**dict2)
    # print(msg)


    msg=L.registerSupplierGetInto(**dict1)
    print(msg)

    strTime = int(time.time())
    supplier_name = "LwFontRegisterSupplier_" + str(strTime)
    timeStruct = time.localtime(strTime)
    strTime = time.strftime("%Y-%m-%d %H:%M:%S", timeStruct)
    company_name = "LwFontRegisterSupplier_" + str(strTime)
    dict3={
        "name": supplier_name,
        "email": "2321628281@qq.com",
        "company_name": company_name,
        "type": "food_supplier",
        "code": "fanxiangyunjisuanhahaha",
        "password": "abc123456",
        "page_name":"register_page"
    }
    msg=L.registerSupplier(**dict3)
    print(msg)
