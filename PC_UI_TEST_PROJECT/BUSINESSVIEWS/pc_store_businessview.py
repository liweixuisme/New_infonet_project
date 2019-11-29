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
from BUSINESSVIEWS.pc_login_businessview import *
import time
import unittest
import GL

base_dir=os.path.dirname(os.path.dirname(__file__))

class Pc_petrochina_store_businessview(ComMon,unittest.TestCase):
    with open(GL.DATAS_DIR + '/elements_data.yaml', encoding='utf-8') as file:
        data = yaml.load(file)

    def pc_storelist_get_into(self):
        self.Click(self.data['pc_store_ele_GPS'],self.data['pc_store_ele'])
        self.out_log("get into store list")
        self.wait(20)

    def pc_store_add_get_into(self):
        self.Click(self.data['pc_store_add_ele_GPS'],self.data['pc_store_add_ele'])
        self.out_log("get into store_add to input store's params")
        self.wait(20)

    def pc_store_add(self,store_name,contator,login_phone,login_password,sn,province,city,county,address):
        self.Input(self.data['pc_store_add_storename_input_ele_GPS'],self.data['pc_store_add_storename_input_ele'],store_name)
        self.Input(self.data['pc_store_add_contator_input_ele_GPS'],self.data['pc_store_add_contator_input_ele'],contator)
        self.Input(self.data['pc_store_add_login_phonenumber_input_ele_GPS'],self.data['pc_store_add_login_phonenumber_input_ele'],login_phone)
        self.Input(self.data['pc_store_add_login_password_input_ele_GPS'],self.data['pc_store_add_login_password_input_ele'],login_password)
        self.Input(self.data['pc_store_add_sn_input_ele_GPS'],self.data['pc_store_add_sn_input_ele'],sn)
        element_province=self.data['pc_store_add_select_a_province_ele'].replace("province",str(province))
        self.Click(self.data['pc_store_add_province_select_ele_GPS'],self.data['pc_store_add_province_select_ele'])
        self.wait(20)
        time.sleep(3)
        forever=1
        self.out_log("select a  province")
        while forever<5:
            try:
                self.Click(self.data['pc_store_edit_select_a_province_ele_GPS'], element_province)
                break
            except:
                self.Click(self.data['pc_store_edit_province_select_ele_GPS'],
                           self.data['pc_store_edit_province_select_ele'])
                self.wait(20)
                time.sleep(3)
                self.Click(self.data['pc_store_edit_province_select_ele_GPS'],
                           self.data['pc_store_edit_province_select_ele'])
                forever=forever+1
        time.sleep(3)
        element_city=self.data['pc_store_add_select_a_city_ele'].replace("city",str(city))
        self.Click(self.data['pc_store_add_city_select_ele_GPS'],self.data['pc_store_add_city_select_ele'])
        self.wait(20)
        time.sleep(3)
        forever=1
        self.out_log("select a  city")
        while forever<5:
            try:
                self.Click(self.data['pc_store_edit_select_a_city_ele_GPS'], element_city)
                break
            except:
                self.Click(self.data['pc_store_edit_city_select_ele_GPS'], self.data['pc_store_edit_city_select_ele'])
                self.wait(20)
                time.sleep(3)
                self.Click(self.data['pc_store_edit_city_select_ele_GPS'], self.data['pc_store_edit_city_select_ele'])
                forever=forever+1
        time.sleep(3)
        element_county=self.data['pc_store_add_select_a_county_ele'].replace("county",str(county))
        self.Click(self.data['pc_store_add_county_select_ele_GPS'],self.data['pc_store_add_county_select_ele'])
        self.wait(20)
        time.sleep(3)
        forever=1
        self.out_log("select a  county")
        while forever<5:
            try:
                self.Click(self.data['pc_store_edit_select_a_county_ele_GPS'], element_county)
                break
            except:
                self.Click(self.data['pc_store_edit_county_select_ele_GPS'],
                           self.data['pc_store_edit_county_select_ele'])
                self.wait(20)
                time.sleep(3)
                self.Click(self.data['pc_store_edit_county_select_ele_GPS'],
                           self.data['pc_store_edit_county_select_ele'])
                forever=forever+1
        time.sleep(3)
        self.Input(self.data['pc_store_add_address_input_ele_GPS'],self.data['pc_store_add_address_input_ele'],address)
        self.Click(self.data['pc_store_add_save_button_ele_GPS'],self.data['pc_store_add_save_button_ele'])
        time.sleep(0.5)
        rng=0
        while rng < 10:
            try:
                text=self.Get_text_PC(self.data['pc_store_add_successfully_text_ele_GPS'], self.data['pc_store_add_successfully_text_ele'])
                self.assertNotEqual(text,"","取到text为空")
                self.out_log("successfully: "+str(text))
                break
            except:
                self.out_log("failed to get the text !")
                rng = rng + 1
        else:
            self.out_log("failed to get_text")
            text = self.Get_text_PC(self.data['pc_store_add_successfully_text_ele_GPS'],self.data['pc_store_add_successfully_text_ele'])
        return text

    def pc_store_edit_get_into(self):
        self.Click(self.data['pc_store_list_edit_button_ele_GPS'],self.data['pc_store_list_edit_button_ele'])
        self.wait(20)
        time.sleep(3)

    def pc_store_edit(self,store_name,contator,sn,province,city,county,address):
        self.Clear_Input(self.data['pc_store_edit_storename_input_ele_GPS'], self.data['pc_store_edit_storename_input_ele'],
                   store_name)
        time.sleep(3)
        self.Clear_Input(self.data['pc_store_edit_contator_input_ele_GPS'], self.data['pc_store_edit_contator_input_ele'],
                   contator)
        time.sleep(3)
        self.Clear_Input(self.data['pc_store_edit_sn_input_ele_GPS'], self.data['pc_store_edit_sn_input_ele'], sn)
        time.sleep(3)
        element_province = self.data['pc_store_edit_select_a_province_ele'].replace("province", str(province))
        self.Click(self.data['pc_store_edit_province_select_ele_GPS'], self.data['pc_store_edit_province_select_ele'])
        time.sleep(3)
        forever=1
        self.out_log("select a  province")
        while forever<5:
            try:
                self.Click(self.data['pc_store_edit_select_a_province_ele_GPS'], element_province)
                forever=5
                time.sleep(3)
            except:
                self.Click(self.data['pc_store_edit_province_select_ele_GPS'],self.data['pc_store_edit_province_select_ele'])
                time.sleep(3)
                self.Click(self.data['pc_store_edit_province_select_ele_GPS'],self.data['pc_store_edit_province_select_ele'])
                forever=forever+1
        element_city = self.data['pc_store_edit_select_a_city_ele'].replace("city", str(city))
        self.Click(self.data['pc_store_edit_city_select_ele_GPS'], self.data['pc_store_edit_city_select_ele'])
        time.sleep(3)
        forever=1
        self.out_log("select a  city")
        while forever<5:
            try:
                self.Click(self.data['pc_store_edit_select_a_city_ele_GPS'], element_city)
                forever=5
                time.sleep(3)
            except:
                self.Click(self.data['pc_store_edit_city_select_ele_GPS'], self.data['pc_store_edit_city_select_ele'])
                time.sleep(3)
                self.Click(self.data['pc_store_edit_city_select_ele_GPS'], self.data['pc_store_edit_city_select_ele'])
                forever=forever+1
        element_county = self.data['pc_store_edit_select_a_county_ele'].replace("county", str(county))
        self.Click(self.data['pc_store_edit_county_select_ele_GPS'], self.data['pc_store_edit_county_select_ele'])
        time.sleep(3)
        forever=1
        self.out_log("select a  county")
        while forever<5:
            try:
                self.Click(self.data['pc_store_edit_select_a_county_ele_GPS'], element_county)
                forever=5
                time.sleep(3)
            except:
                self.Click(self.data['pc_store_edit_county_select_ele_GPS'],
                           self.data['pc_store_edit_county_select_ele'])
                time.sleep(3)
                self.Click(self.data['pc_store_edit_county_select_ele_GPS'],
                           self.data['pc_store_edit_county_select_ele'])
                forever=forever+1
        self.Clear(self.data['pc_store_edit_editress_input_ele_GPS'], self.data['pc_store_edit_editress_input_ele'])
        time.sleep(3)
        self.Clear_Input(self.data['pc_store_edit_editress_input_ele_GPS'], self.data['pc_store_edit_editress_input_ele'],address)
        self.Click(self.data['pc_store_edit_save_button_ele_GPS'], self.data['pc_store_edit_save_button_ele'])
        rng = 0
        while rng < 10:
            try:
                text = self.Get_text_PC(self.data['pc_store_edit_successfully_text_ele_GPS'],
                                        self.data['pc_store_edit_successfully_text_ele'])
                self.assertNotEqual(text,"","取到text为空")
                self.out_log("successfully: " + str(text))
                break
            except:
                self.out_log("failed to get the text !")
                rng = rng + 1
        else:
            self.out_log("failed to get_text")
            text = self.Get_text_PC(self.data['pc_store_edit_successfully_text_ele_GPS'],
                                    self.data['pc_store_edit_successfully_text_ele'])
        return text

    def pc_store_searchstore(self,search_value):
        self.Input(self.data['pc_store_add_storesearch_input_ele_GPS'],self.data['pc_store_add_storesearch_input_ele'],search_value)
        self.Click(self.data['pc_store_add_storesearch_button_ele_GPS'],self.data['pc_store_add_storesearch_button_ele'])
        self.wait(20)
        time.sleep(3)





if __name__ == '__main__':

    with open(base_dir + '/DATA/pos_petrochina_elements_and_params.yaml', encoding='utf-8') as file:
        login_params = yaml.load(file)

    store_name="04-26-18-37_lw有限公司"
    contator="liwei.许"
    login_phone="15850655055"
    login_password="123456"
    sn="15850655055"
    province="广东省"
    city="珠海市"
    county="香洲区"
    address="环岛东路横琴创意谷7栋"
    broswer=pc_ui_start()
    L=Pc_login_businessview(broswer)
    url="https://petrochina-data-test.esmart365.com"
    L.get_url(url)
    L.maximize_window()
    L.pc_petrochina_login(login_params['pc_username'],login_params['pc_password'],"pos_petro_login_page")
    L=Pc_petrochina_store_businessview(broswer)
    L.pc_storelist_get_into()
    # L.pc_store_add_get_into()
    L.pc_store_searchstore(str(store_name))
    L.pc_store_edit_get_into()
    L.pc_store_edit(store_name,contator,sn,province,city,county,address)
    # L.pc_store_add(store_name,contator,login_phone,login_password,sn,province,city,county,address)
