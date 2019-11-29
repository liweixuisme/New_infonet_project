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


class Pc_login_businessview(ComMon):
    with open(GL.DATAS_DIR + '/elements_data.yaml', encoding='utf-8') as file:
        data = yaml.load(file)
    def pc_petrochina_login(self,username,password,page_name):
        page=self.data[page_name]
        self.Input(page['pc_username_ele_GPS'], page['pc_username_ele'],username)
        self.out_log("inputed name")
        self.Input(page['pc_password_ele_GPS'], page['pc_password_ele'], password)
        self.out_log("inputed password")
        self.Click(page['pc_login_ele_GPS'], page['pc_login_ele']) # 点击登录
        self.out_log("clicked confirm to login")
        self.wait(20)
        time.sleep(3)


if __name__ == '__main__':
    driver=pc_ui_start()
    L=Pc_login_businessview(driver)
    url="https://petrochina-data-test.esmart365.com"
    L.get_url(url)
    L.maximize_window()
    L.pc_petrochina_login("uSmileAdmin","usmile2018","pc_petro_login_page")


