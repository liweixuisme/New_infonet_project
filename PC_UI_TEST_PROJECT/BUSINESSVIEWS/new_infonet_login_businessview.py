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
import time
import GL


class New_InfoNet_LoginBusinessView(ComMon):
    with open(GL.DATAS_DIR + '/new_infonet_elements.yaml', encoding='utf-8') as file:
        data = yaml.load(file)

    def loginButtonClick(self,**dict):
        page=self.data[dict["page_name"]]
        self.Click(page['goto_login_a_GPS'], page['goto_login_a'])
        self.wait(60)
        self.sleep(10)
        msg = "loginButtonClick success"
        return msg

    def login(self,**dict):
        user_name=dict["user_name"]
        password=dict["password"]
        page=self.data[dict["page_name"]]
        self.out_log("inputing name")
        self.Input(page['username_input_GPS'], page['username_input'],user_name)
        self.Input(page['password_input_GPS'], page['password_input'],password)
        self.out_log("inputing password")
        self.out_log("clicking confirm to login")
        self.Click(page['login_button_GPS'], page['login_button']) # 点击登录
        self.wait(60)
        self.sleep(10)
        msg = "login success"
        return msg


if __name__ == '__main__':
    driver=pc_ui_start()
    L=New_InfoNet_LoginBusinessView(driver)
    # url="http://infonet.new.bringbuys.com/login?lang=zht"
    url="http://infonet.new.bringbuys.com/?lang=zht"
    L.get_url(url)
    L.maximize_window()

    dict = {
        "page_name": "login_page",
    }
    msg=L.loginButtonClick(**dict)
    print(msg)

    dict={
        "user_name": "LW_multi_supplier3",
        "password": "abc123456",
        "page_name":"login_page",
    }
    msg=L.login(**dict)
    print(msg)

    # L.new_info_net_login("LW_multi_supplier3","abc123456","login_page")
    # url="http://infonet.new.bringbuys.com/user/my-collected/food?lang=zht"
    # L.get_url(url)


