# coding=UTF-8
from selenium import webdriver

def pc_ui_start():
    driver=webdriver.Chrome("C:\\Program Files\\Python 3.5\\chromedriver.exe")
    # driver=webdriver.Firefox()
    return driver


if __name__ == '__main__':
    driver=pc_ui_start()
    driver.get("http://www.baidu.com")
    driver.find_element_by_id("kw").send_keys("51zxw")
