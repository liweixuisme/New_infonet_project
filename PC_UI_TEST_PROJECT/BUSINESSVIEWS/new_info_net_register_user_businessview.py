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

class New_info_net_register_user_businessview(ComMon):
    with open(GL.DATAS_DIR + '/new_infonet_elements.yaml', encoding='utf-8') as file:
        data = yaml.load(file)

    def new_info_net_register_get_into(self,page_name):
        page = self.data[page_name]
        self.Click(page['job_seeker_register_for_free_button_GPS'],page['job_seeker_register_for_free_button'])
        self.out_log("get into register select page")
        self.wait_and_sleep(300,44)

    def new_info_net_register_job_seeker_get_into(self,page_name):
        page = self.data[page_name]
        self.Click(page['job_seeker_goto_register_button_GPS'],page['job_seeker_goto_register_button'])
        self.out_log("get into register jobseeker page")
        self.wait_and_sleep(300,44)


    def new_info_net_register_supplier_get_into(self,page_name):
        page = self.data[page_name]
        self.Click(page['supplier_goto_register_button_GPS'],page['supplier_goto_register_button'])
        self.out_log("get into register supplier page")
        self.wait_and_sleep(300,44)


    def new_info_net_register_jobseeker(self,job_seeker_name,job_seeker_email,register_code,password,page_name):
        page = self.data[page_name]
        self.Input(page['job_seeker_register_name_input_GPS'],page['job_seeker_register_name_input'],job_seeker_name)
        self.Input(page['job_seeker_register_email_input_GPS'],page['job_seeker_register_email_input'],job_seeker_email)
        self.Input(page['job_seeker_register_code_input_GPS'],page['job_seeker_register_code_input'],register_code)
        self.Input(page['job_seeker_register_password_input_GPS'],page['job_seeker_register_password_input'],password)
        self.Input(page['job_seeker_register_again_password_input_GPS'],page['job_seeker_register_again_password_input'],password)
        self.Click(page['job_seeker_register_agree_xieyi_checkbox_GPS'],page['job_seeker_register_agree_xieyi_checkbox'])
        self.wait_and_sleep(300,10)
        self.Click(page['job_seeker_register_register_button_GPS'],page['job_seeker_register_register_button'])
        self.wait_and_sleep(300,44)


    def new_info_net_register_supplier(self,supplier_name,supplier_email,supplier_company_name,supplier_type,register_code,password,page_name):
        page = self.data[page_name]
        self.Input(page['supplier_register_name_input_GPS'],page['supplier_register_name_input'],supplier_name)
        self.Input(page['supplier_register_email_input_GPS'],page['supplier_register_email_input'],supplier_email)
        self.Input(page['supplier_register_company_name_input_GPS'],page['supplier_register_company_name_input'],supplier_company_name)
        if supplier_type=="food_supplier":
            self.Click(page['supplier_register_foodsupplier_span_GPS'],page['supplier_register_foodsupplier_span'])
        elif supplier_type=="service_supplier":
            self.Click(page['supplier_register_service_supplier_span_GPS'],page['supplier_register_service_supplier_span'])
        elif supplier_type=="both":
            self.Click(page['supplier_register_both_food_and_service_supplier_span_GPS'],page['supplier_register_both_food_and_service_supplier_span'])
        self.Input(page['supplier_register_code_input_GPS'],page['supplier_register_code_input'],register_code)
        self.Input(page['job_seeker_register_password_input_GPS'],page['job_seeker_register_password_input'],password)
        self.Input(page['supplier_register_again_password_input_GPS'],page['supplier_register_again_password_input'],password)
        self.Click(page['supplier_register_agree_xieyi_checkbox_GPS'],page['supplier_register_agree_xieyi_checkbox'])
        self.wait_and_sleep(300,10)
        self.Click(page['job_seeker_register_register_button_GPS'],page['job_seeker_register_register_button'])
        self.wait_and_sleep(300,44)



if __name__ == '__main__':

    driver=pc_ui_start()
    L=New_info_net_register_user_businessview(driver)
    url="http://infonet.new.bringbuys.com/login?lang=zht"
    L.get_url(url)
    L.maximize_window()
    L.new_info_net_register_get_into("register_page")


    # strTime = int(time.time())
    # L.new_info_net_register_job_seeker_get_into("register_page")
    # var_job_seeker_name = "LW_font_register_jobseeker" + str(strTime)
    # L.new_info_net_register_jobseeker(var_job_seeker_name,"2321628281@qq.com","fanxiangyunjisuanhahaha","abc123456","register_page")
    # L=New_info_net_login_businessview(driver)
    # L.new_info_net_goto_login("login_page")
    # L.new_info_net_login(var_job_seeker_name,"abc123456","login_page")
    # L=New_info_net_usercenter_businessview(driver)
    # L.new_info_net_usercenter_get_into("user_center_page")
    # L.new_info_net_jobseeker_info_get_into("user_center_page")
    # L.new_info_net_upload_jobseeker_info("liwei.xu","13229794612","2321628281@qq.com","lw_个人简述繁体","lw_个人职业经历繁体","user_center_page")


    # strTime = int(time.time())
    # var_supplier_name = "LW_font_register_service_supplier" + str(strTime)
    # L.new_info_net_register_supplier_get_into("register_page")
    # L.new_info_net_register_supplier(var_supplier_name,"13229794612@163.com","lw_company","food_supplier","fanxiangyunjisuanhahaha","abc123456","register_page")
