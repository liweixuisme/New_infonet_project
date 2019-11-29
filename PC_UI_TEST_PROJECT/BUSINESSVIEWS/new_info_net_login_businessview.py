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


class New_info_net_login_businessview(ComMon):
    with open(GL.DATAS_DIR + '/new_infonet_elements.yaml', encoding='utf-8') as file:
        data = yaml.load(file)

    def new_info_net_goto_login(self,page_name):
        page=self.data[page_name]
        self.Click(page['goto_login_a_GPS'], page['goto_login_a'])
        self.wait_and_sleep(60,10)

    def new_info_net_login(self,username,password,page_name):
        page=self.data[page_name]
        self.Input(page['username_input_GPS'], page['username_input'],username)
        self.out_log("inputed name")
        self.Input(page['password_input_GPS'], page['password_input'], password)
        self.out_log("inputed password")
        self.Click(page['login_button_GPS'], page['login_button']) # 点击登录
        self.out_log("clicked confirm to login")
        self.wait_and_sleep(300,44)


if __name__ == '__main__':
    driver=pc_ui_start()
    L=New_info_net_login_businessview(driver)
    url="http://infonet.new.bringbuys.com/login?lang=zht"
    L.get_url(url)
    L.maximize_window()
    L.new_info_net_login("LW_multi_supplier3","abc123456","login_page")
    url="http://infonet.new.bringbuys.com/user/my-collected/food?lang=zht"
    L.get_url(url)


