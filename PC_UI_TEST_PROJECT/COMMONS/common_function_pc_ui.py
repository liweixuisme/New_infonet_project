from BASEVIEW.baseview import BaseView
import logging
import logging.config
import os
import time
import GL
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import *
from selenium.webdriver.common.action_chains import ActionChains



#appium 定位时：  resrouce-id属性是id ; text属性是name ; class属性是classname; accessibilityid 的属性是 content-desc
# uiautomator 使用方法如下：
# new UiSelector().text(text)  使用元素 text 属性定位
# new UiSelector().resourceId(id)         # 使用 id 属性
# new UiSelector().className(className)   # 使用元素类型定位
# # 还可以元素多个属性自由组合
# new UiSelector().className(className).text(text)
# new UiSelector().resourceId(id).clickable(val)
# new UiSelector().className(className).text(text).longClickable(val)

#特殊方法 //*[@id='app']/../div[4]//*[contains(text(),"store_name")]/..

class ComMon(BaseView):
    max_times=1000
    circle_times=2
    sleep_time=2
    forever=1
    CON_FIG=GL.CONFIGS_DIR+'/log.conf'
    logging.config.fileConfig(CON_FIG)
    logging = logging.getLogger()
    
    def Input(self, type, value, inputvalue):
        if type == "xpath":
            for forever in range(1, self.max_times):
                if forever < self.circle_times:
                    try:
                        element = self.driver.find_element_by_xpath(value)
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        time.sleep(self.sleep_time)
                    else:
                        element.send_keys(inputvalue)
                        self.out_log("input successfully : " + str(value))
                        break
                else:
                    try:
                        element = self.driver.find_element_by_xpath(value)
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        self.driver.find_element_by_xpath(value)
                    else:
                        element.send_keys(inputvalue)
                        self.out_log("input successfully : " + str(value))
                        break
        elif type == "id":
            for forever in range(1, self.max_times):
                if forever < self.circle_times:
                    try:
                        element = self.driver.find_element_by_id(value)
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        time.sleep(self.sleep_time)
                    else:
                        element.send_keys(inputvalue)
                        self.out_log("input successfully : " + str(value))
                        break
                else:
                    try:
                        element = self.driver.find_element_by_id(value)
                    except NoSuchElementException as msg:
                        self.out_log("no such element :%s " %msg + str(value))
                        self.driver.find_element_by_id(value)
                    else:
                        element.send_keys(inputvalue)
                        self.out_log("input successfully : " + str(value))
                        break
        elif type == "accessibilityid":
            for forever in range(1, self.max_times):
                if forever < self.circle_times:
                    try:
                        element = self.driver.find_element_by_accessibility_id(value)
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        time.sleep(self.sleep_time)
                    else:
                        element.send_keys(inputvalue)
                        self.out_log("input successfully : " + str(value))
                        break
                else:
                    try:
                        element = self.driver.find_element_by_accessibility_id(value)
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        self.driver.find_element_by_accessibility_id(value)
                    else:
                        element.send_keys(inputvalue)
                        self.out_log("input successfully : " + str(value))
                        break
        elif type == "class_name":
            for forever in range(1, self.max_times):
                if forever < self.circle_times:
                    try:
                        element = self.driver.find_element_by_class_name(value)
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        time.sleep(self.sleep_time)
                    else:
                        element.send_keys(inputvalue)
                        self.out_log("input successfully : " + str(value))
                        break
                else:
                    try:
                        element = self.driver.find_element_by_class_name(value)
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        self.driver.find_element_by_class_name(value)
                    else:
                        element.send_keys(inputvalue)
                        self.out_log("input successfully : " + str(value))
                        break
        elif type == "name":
            for forever in range(1, self.max_times):
                if forever < self.circle_times:
                    try:
                        element = self.driver.find_element_by_name(value)
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        time.sleep(self.sleep_time)
                    else:
                        element.send_keys(inputvalue)
                        self.out_log("input successfully : " + str(value))
                        break
                else:
                    try:
                        element = self.driver.find_element_by_name(value)
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        self.driver.find_element_by_name(value)
                    else:
                        element.send_keys(inputvalue)
                        self.out_log("input successfully : " + str(value))
                        break
        elif type == "uiautomator":
            for forever in range(1, self.max_times):
                if forever < self.circle_times:
                    try:
                        element = self.driver.find_element_by_android_uiautomator(value)
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        time.sleep(self.sleep_time)
                    else:
                        element.send_keys(inputvalue)
                        self.out_log("input successfully : " + str(value))
                        break
                else:
                    try:
                        element = self.driver.find_element_by_android_uiautomator(value)
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        self.driver.find_element_by_android_uiautomator(value)
                    else:
                        element.send_keys(inputvalue)
                        self.out_log("input successfully : " + str(value))
                        break
        elif type == "uiautomator_id":
            for forever in range(1, self.max_times):
                if forever < self.circle_times:
                    try:
                        element = self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("%s")'%str(value))
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        time.sleep(self.sleep_time)
                    else:
                        element.send_keys(inputvalue)
                        self.out_log("input successfully : " + str(value))
                        break
                else:
                    try:
                        element = self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("%s")'%str(value))
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("%s")'%str(value))
                    else:
                        element.send_keys(inputvalue)
                        self.out_log("input successfully : " + str(value))
                        break
        elif type == "uiautomator_text":
            for forever in range(1, self.max_times):
                if forever < self.circle_times:
                    try:
                        element = self.driver.find_element_by_android_uiautomator('new UiSelector().text("%s")'%str(value))
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        time.sleep(self.sleep_time)
                    else:
                        element.send_keys(inputvalue)
                        self.out_log("input successfully : " + str(value))
                        break
                else:
                    try:
                        element = self.driver.find_element_by_android_uiautomator('new UiSelector().text("%s")'%str(value))
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        self.driver.find_element_by_android_uiautomator('new UiSelector().text("%s")'%str(value))
                    else:
                        element.send_keys(inputvalue)
                        self.out_log("input successfully : " + str(value))
                        break
        elif type == "uiautomator_classname":
            for forever in range(1, self.max_times):
                if forever < self.circle_times:
                    try:
                        element = self.driver.find_element_by_android_uiautomator('new UiSelector().className("%s")'%str(value))
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        time.sleep(self.sleep_time)
                    else:
                        element.send_keys(inputvalue)
                        self.out_log("input successfully : " + str(value))
                        break
                else:
                    try:
                        element = self.driver.find_element_by_android_uiautomator('new UiSelector().className("%s")'%str(value))
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        self.driver.find_element_by_android_uiautomator('new UiSelector().className("%s")'%str(value))
                    else:
                        element.send_keys(inputvalue)
                        self.out_log("input successfully : " + str(value))
                        break
    def Clear_Input(self, type, value, inputvalue):
        if type == "xpath":
            for forever in range(1, self.max_times):
                if forever < self.circle_times:
                    try:
                        element = self.driver.find_element_by_xpath(value)
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        time.sleep(self.sleep_time)
                    else:
                        element.send_keys(Keys.CONTROL + "a")
                        element.send_keys(inputvalue)
                        self.out_log("input successfully : " + str(value))
                        break
                else:
                    try:
                        element = self.driver.find_element_by_xpath(value)
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        self.driver.find_element_by_xpath(value)
                    else:
                        element.send_keys(Keys.CONTROL + "a")
                        element.send_keys(inputvalue)
                        self.out_log("input successfully : " + str(value))
                        break
        elif type == "id":
            for forever in range(1, self.max_times):
                if forever < self.circle_times:
                    try:
                        element = self.driver.find_element_by_id(value)
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        time.sleep(self.sleep_time)
                    else:
                        element.send_keys(Keys.CONTROL + "a")
                        element.send_keys(inputvalue)
                        self.out_log("input successfully : " + str(value))
                        break
                else:
                    try:
                        element = self.driver.find_element_by_id(value)
                    except NoSuchElementException as msg:
                        self.out_log("no such element :%s " %msg + str(value))
                        self.driver.find_element_by_id(value)
                    else:
                        element.send_keys(Keys.CONTROL + "a")
                        element.send_keys(inputvalue)
                        self.out_log("input successfully : " + str(value))
                        break
        elif type == "accessibilityid":
            for forever in range(1, self.max_times):
                if forever < self.circle_times:
                    try:
                        element = self.driver.find_element_by_accessibility_id(value)
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        time.sleep(self.sleep_time)
                    else:
                        element.send_keys(Keys.CONTROL + "a")
                        element.send_keys(inputvalue)
                        self.out_log("input successfully : " + str(value))
                        break
                else:
                    try:
                        element = self.driver.find_element_by_accessibility_id(value)
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        self.driver.find_element_by_accessibility_id(value)
                    else:
                        element.send_keys(Keys.CONTROL + "a")
                        element.send_keys(inputvalue)
                        self.out_log("input successfully : " + str(value))
                        break
        elif type == "classname":
            for forever in range(1, self.max_times):
                if forever < self.circle_times:
                    try:
                        element = self.driver.find_element_by_class_name(value)
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        time.sleep(self.sleep_time)
                    else:
                        element.send_keys(Keys.CONTROL + "a")
                        element.send_keys(inputvalue)
                        self.out_log("input successfully : " + str(value))
                        break
                else:
                    try:
                        element = self.driver.find_element_by_class_name(value)
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        self.driver.find_element_by_class_name(value)
                    else:
                        element.send_keys(Keys.CONTROL + "a")
                        element.send_keys(inputvalue)
                        self.out_log("input successfully : " + str(value))
                        break
        elif type == "name":
            for forever in range(1, self.max_times):
                if forever < self.circle_times:
                    try:
                        element = self.driver.find_element_by_name(value)
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        time.sleep(self.sleep_time)
                    else:
                        element.send_keys(Keys.CONTROL + "a")
                        element.send_keys(inputvalue)
                        self.out_log("input successfully : " + str(value))
                        break
                else:
                    try:
                        element = self.driver.find_element_by_name(value)
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        self.driver.find_element_by_name(value)
                    else:
                        element.send_keys(Keys.CONTROL + "a")
                        element.send_keys(inputvalue)
                        self.out_log("input successfully : " + str(value))
                        break
        elif type == "uiautomator":
            for forever in range(1, self.max_times):
                if forever < self.circle_times:
                    try:
                        element = self.driver.find_element_by_android_uiautomator(value)
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        time.sleep(self.sleep_time)
                    else:
                        element.send_keys(Keys.CONTROL + "a")
                        element.send_keys(inputvalue)
                        self.out_log("input successfully : " + str(value))
                        break
                else:
                    try:
                        element = self.driver.find_element_by_android_uiautomator(value)
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        self.driver.find_element_by_android_uiautomator(value)
                    else:
                        element.send_keys(Keys.CONTROL + "a")
                        element.send_keys(inputvalue)
                        self.out_log("input successfully : " + str(value))
                        break
        elif type == "uiautomator_id":
            for forever in range(1, self.max_times):
                if forever < self.circle_times:
                    try:
                        element = self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("%s")'%str(value))
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        time.sleep(self.sleep_time)
                    else:
                        element.send_keys(Keys.CONTROL + "a")
                        element.send_keys(inputvalue)
                        self.out_log("input successfully : " + str(value))
                        break
                else:
                    try:
                        element = self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("%s")'%str(value))
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("%s")'%str(value))
                    else:
                        element.send_keys(Keys.CONTROL + "a")
                        element.send_keys(inputvalue)
                        self.out_log("input successfully : " + str(value))
                        break
        elif type == "uiautomator_text":
            for forever in range(1, self.max_times):
                if forever < self.circle_times:
                    try:
                        element = self.driver.find_element_by_android_uiautomator('new UiSelector().text("%s")'%str(value))
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        time.sleep(self.sleep_time)
                    else:
                        element.send_keys(Keys.CONTROL + "a")
                        element.send_keys(inputvalue)
                        self.out_log("input successfully : " + str(value))
                        break
                else:
                    try:
                        element = self.driver.find_element_by_android_uiautomator('new UiSelector().text("%s")'%str(value))
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        self.driver.find_element_by_android_uiautomator('new UiSelector().text("%s")'%str(value))
                    else:
                        element.send_keys(Keys.CONTROL + "a")
                        element.send_keys(inputvalue)
                        self.out_log("input successfully : " + str(value))
                        break
        elif type == "uiautomator_classname":
            for forever in range(1, self.max_times):
                if forever < self.circle_times:
                    try:
                        element = self.driver.find_element_by_android_uiautomator('new UiSelector().className("%s")'%str(value))
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        time.sleep(self.sleep_time)
                    else:
                        element.send_keys(Keys.CONTROL + "a")
                        element.send_keys(inputvalue)
                        self.out_log("input successfully : " + str(value))
                        break
                else:
                    try:
                        element = self.driver.find_element_by_android_uiautomator('new UiSelector().className("%s")'%str(value))
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        self.driver.find_element_by_android_uiautomator('new UiSelector().className("%s")'%str(value))
                    else:
                        element.send_keys(Keys.CONTROL + "a")
                        element.send_keys(inputvalue)
                        self.out_log("input successfully : " + str(value))
                        break
    def Click(self, type, value):
        if type == "xpath":
            for forever in range(1, self.max_times):
                if forever < self.circle_times:
                    try:
                        element = self.driver.find_element_by_xpath(value)
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        time.sleep(self.sleep_time)
                    else:
                        element.click()
                        self.out_log("click successfully : " + str(value))
                        break
                else:
                    try:
                        element = self.driver.find_element_by_xpath(value)
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        self.driver.find_element_by_xpath(value)
                    else:
                        element.click()
                        self.out_log("input successfully : " + str(value))
                        break
        elif type == "id":
            for forever in range(1, self.max_times):
                if forever < self.circle_times:
                    try:
                        element = self.driver.find_element_by_id(value)
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        time.sleep(self.sleep_time)
                    else:
                        element.click()
                        self.out_log("input successfully : " + str(value))
                        break
                else:
                    try:
                        element = self.driver.find_element_by_id(value)
                    except NoSuchElementException as msg:
                        self.out_log("no such element :%s " %msg + str(value))
                        self.driver.find_element_by_id(value)
                    else:
                        element.click()
                        self.out_log("input successfully : " + str(value))
                        break
        elif type == "accessibilityid":
            for forever in range(1, self.max_times):
                if forever < self.circle_times:
                    try:
                        element = self.driver.find_element_by_accessibility_id(value)
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        time.sleep(self.sleep_time)
                    else:
                        element.click()
                        self.out_log("input successfully : " + str(value))
                        break
                else:
                    try:
                        element = self.driver.find_element_by_accessibility_id(value)
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        self.driver.find_element_by_accessibility_id(value)
                    else:
                        element.click()
                        self.out_log("input successfully : " + str(value))
                        break
        elif type == "class_name":
            for forever in range(1, self.max_times):
                if forever < self.circle_times:
                    try:
                        element = self.driver.find_element_by_class_name(value)
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        time.sleep(self.sleep_time)
                    else:
                        element.click()
                        self.out_log("input successfully : " + str(value))
                        break
                else:
                    try:
                        element = self.driver.find_element_by_class_name(value)
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        self.driver.find_element_by_class_name(value)
                    else:
                        element.click()
                        self.out_log("input successfully : " + str(value))
                        break
        elif type == "name":
            for forever in range(1, self.max_times):
                if forever < self.circle_times:
                    try:
                        element = self.driver.find_element_by_name(value)
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        time.sleep(self.sleep_time)
                    else:
                        element.click()
                        self.out_log("input successfully : " + str(value))
                        break
                else:
                    try:
                        element = self.driver.find_element_by_name(value)
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        self.driver.find_element_by_name(value)
                    else:
                        element.click()
                        self.out_log("input successfully : " + str(value))
                        break
        elif type == "uiautomator":
            for forever in range(1, self.max_times):
                if forever < self.circle_times:
                    try:
                        element = self.driver.find_element_by_android_uiautomator(value)
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        time.sleep(self.sleep_time)
                    else:
                        element.click()
                        self.out_log("input successfully : " + str(value))
                        break
                else:
                    try:
                        element = self.driver.find_element_by_android_uiautomator(value)
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        self.driver.find_element_by_android_uiautomator(value)
                    else:
                        element.click()
                        self.out_log("input successfully : " + str(value))
                        break
        elif type == "uiautomator_id":
            for forever in range(1, self.max_times):
                if forever < self.circle_times:
                    try:
                        element = self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("%s")'%str(value))
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        time.sleep(self.sleep_time)
                    else:
                        element.click()
                        self.out_log("input successfully : " + str(value))
                        break
                else:
                    try:
                        element = self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("%s")'%str(value))
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("%s")'%str(value))
                    else:
                        element.click()
                        self.out_log("input successfully : " + str(value))
                        break
        elif type == "uiautomator_text":
            for forever in range(1, self.max_times):
                if forever < self.circle_times:
                    try:
                        element = self.driver.find_element_by_android_uiautomator('new UiSelector().text("%s")'%str(value))
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        time.sleep(self.sleep_time)
                    else:
                        element.click()
                        self.out_log("input successfully : " + str(value))
                        break
                else:
                    try:
                        element = self.driver.find_element_by_android_uiautomator('new UiSelector().text("%s")'%str(value))
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        self.driver.find_element_by_android_uiautomator('new UiSelector().text("%s")'%str(value))
                    else:
                        element.click()
                        self.out_log("input successfully : " + str(value))
                        break
        elif type == "uiautomator_classname":
            for forever in range(1, self.max_times):
                if forever < self.circle_times:
                    try:
                        element = self.driver.find_element_by_android_uiautomator('new UiSelector().className("%s")'%str(value))
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        time.sleep(self.sleep_time)
                    else:
                        element.click()
                        self.out_log("input successfully : " + str(value))
                        break
                else:
                    try:
                        element = self.driver.find_element_by_android_uiautomator('new UiSelector().className("%s")'%str(value))
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        self.driver.find_element_by_android_uiautomator('new UiSelector().className("%s")'%str(value))
                    else:
                        element.click()
                        self.out_log("input successfully : " + str(value))
                        break
        elif type == "pc_text_..":
            for forever in range(1, self.max_times):
                if forever < self.circle_times:
                    try:
                        element = self.driver.find_element_by_xpath('//*[contains(text(),"%s")]/..'%value)
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        time.sleep(self.sleep_time)
                    else:
                        element.click()
                        self.out_log("input successfully : " + str(value))
                        break
                else:
                    try:
                        element = self.driver.find_element_by_xpath('//*[contains(text(),"%s")]/..'%value)
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        self.driver.find_element_by_xpath('//*[contains(text(),"%s")]/..'%value)
                    else:
                        element.click()
                        self.out_log("input successfully : " + str(value))
                        break
        elif type == "pc_text":
            for forever in range(1, self.max_times):
                if forever < self.circle_times:
                    try:
                        element = self.driver.find_element_by_xpath('//*[contains(text(),"%s")]'%value)
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        time.sleep(self.sleep_time)
                    else:
                        element.click()
                        self.out_log("input successfully : " + str(value))
                        break
                else:
                    try:
                        element = self.driver.find_element_by_xpath('//*[contains(text(),"%s")]'%value)
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        self.driver.find_element_by_xpath('//*[contains(text(),"%s")]'%value)
                    else:
                        element.click()
                        self.out_log("input successfully : " + str(value))
                        break
    def Clear(self, type, value):
        if type == "xpath":
            for forever in range(1, self.max_times):
                if forever < self.circle_times:
                    try:
                        element = self.driver.find_element_by_xpath(value)
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        time.sleep(self.sleep_time)
                    else:
                        element.clear()
                        self.out_log("input successfully : " + str(value))
                        break
                else:
                    try:
                        element = self.driver.find_element_by_xpath(value)
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        self.driver.find_element_by_xpath(value)
                    else:
                        element.clear()
                        self.out_log("input successfully : " + str(value))
                        break
        elif type == "id":
            for forever in range(1, self.max_times):
                if forever < self.circle_times:
                    try:
                        element = self.driver.find_element_by_id(value)
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        time.sleep(self.sleep_time)
                    else:
                        element.clear()
                        self.out_log("input successfully : " + str(value))
                        break
                else:
                    try:
                        element = self.driver.find_element_by_id(value)
                    except NoSuchElementException as msg:
                        self.out_log("no such element :%s " %msg + str(value))
                        self.driver.find_element_by_id(value)
                    else:
                        element.clear()
                        self.out_log("input successfully : " + str(value))
                        break
        elif type == "accessibilityid":
            for forever in range(1, self.max_times):
                if forever < self.circle_times:
                    try:
                        element = self.driver.find_element_by_accessibility_id(value)
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        time.sleep(self.sleep_time)
                    else:
                        element.clear()
                        self.out_log("input successfully : " + str(value))
                        break
                else:
                    try:
                        element = self.driver.find_element_by_accessibility_id(value)
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        self.driver.find_element_by_accessibility_id(value)
                    else:
                        element.clear()
                        self.out_log("input successfully : " + str(value))
                        break
        elif type == "classname":
            for forever in range(1, self.max_times):
                if forever < self.circle_times:
                    try:
                        element = self.driver.find_element_by_class_name(value)
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        time.sleep(self.sleep_time)
                    else:
                        element.clear()
                        self.out_log("input successfully : " + str(value))
                        break
                else:
                    try:
                        element = self.driver.find_element_by_class_name(value)
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        self.driver.find_element_by_class_name(value)
                    else:
                        element.clear()
                        self.out_log("input successfully : " + str(value))
                        break
        elif type == "name":
            for forever in range(1, self.max_times):
                if forever < self.circle_times:
                    try:
                        element = self.driver.find_element_by_name(value)
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        time.sleep(self.sleep_time)
                    else:
                        element.clear()
                        self.out_log("input successfully : " + str(value))
                        break
                else:
                    try:
                        element = self.driver.find_element_by_name(value)
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        self.driver.find_element_by_name(value)
                    else:
                        element.clear()
                        self.out_log("input successfully : " + str(value))
                        break
        elif type == "uiautomator":
            for forever in range(1, self.max_times):
                if forever < self.circle_times:
                    try:
                        element = self.driver.find_element_by_android_uiautomator(value)
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        time.sleep(self.sleep_time)
                    else:
                        element.clear()
                        self.out_log("input successfully : " + str(value))
                        break
                else:
                    try:
                        element = self.driver.find_element_by_android_uiautomator(value)
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        self.driver.find_element_by_android_uiautomator(value)
                    else:
                        element.clear()
                        self.out_log("input successfully : " + str(value))
                        break
        elif type == "uiautomator_id":
            for forever in range(1, self.max_times):
                if forever < self.circle_times:
                    try:
                        element = self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("%s")'%str(value))
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        time.sleep(self.sleep_time)
                    else:
                        element.clear()
                        self.out_log("input successfully : " + str(value))
                        break
                else:
                    try:
                        element = self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("%s")'%str(value))
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("%s")'%str(value))
                    else:
                        element.clear()
                        self.out_log("input successfully : " + str(value))
                        break
        elif type == "uiautomator_text":
            for forever in range(1, self.max_times):
                if forever < self.circle_times:
                    try:
                        element = self.driver.find_element_by_android_uiautomator('new UiSelector().text("%s")'%str(value))
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        time.sleep(self.sleep_time)
                    else:
                        element.clear()
                        self.out_log("input successfully : " + str(value))
                        break
                else:
                    try:
                        element = self.driver.find_element_by_android_uiautomator('new UiSelector().text("%s")'%str(value))
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        self.driver.find_element_by_android_uiautomator('new UiSelector().text("%s")'%str(value))
                    else:
                        element.clear()
                        self.out_log("input successfully : " + str(value))
                        break
        elif type == "uiautomator_classname":
            for forever in range(1, self.max_times):
                if forever < self.circle_times:
                    try:
                        element = self.driver.find_element_by_android_uiautomator('new UiSelector().className("%s")'%str(value))
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        time.sleep(self.sleep_time)
                    else:
                        element.clear()
                        self.out_log("input successfully : " + str(value))
                        break
                else:
                    try:
                        element = self.driver.find_element_by_android_uiautomator('new UiSelector().className("%s")'%str(value))
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        self.driver.find_element_by_android_uiautomator('new UiSelector().className("%s")'%str(value))
                    else:
                        element.clear()
                        self.out_log("input successfully : " + str(value))
                        break
    def Get_text(self, type, value):
        if type == "xpath":
            for forever in range(1, self.max_times):
                if forever < self.circle_times:
                    try:
                        element = self.driver.find_element_by_xpath(value)
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        # time.sleep(self.sleep_time)
                    else:
                        TEXT=element.get_attribute("name")
                        if TEXT!='':
                            self.out_log("input successfully : " + str(value))
                            return TEXT
                        else:
                            self.out_log("continue to get_text")
                            continue
                else:
                    try:
                        element = self.driver.find_element_by_xpath(value)
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        self.driver.find_element_by_xpath(value)
                    else:
                        TEXT = element.get_attribute("name")
                        self.out_log("input successfully : " + str(value))
                        return TEXT
        elif type == "id":
            for forever in range(1, self.max_times):
                if forever < self.circle_times:
                    try:
                        element = self.driver.find_element_by_id(value)
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        time.sleep(self.sleep_time)
                    else:
                        TEXT = element.get_attribute("name")
                        if TEXT != '':
                            self.out_log("input successfully : " + str(value))
                            return TEXT
                        else:
                            self.out_log("continue to get_text")
                            continue
                else:
                    try:
                        element = self.driver.find_element_by_id(value)
                    except NoSuchElementException as msg:
                        self.out_log("no such element :%s " %msg + str(value))
                        self.driver.find_element_by_id(value)
                    else:
                        TEXT = element.get_attribute("name")
                        self.out_log("input successfully : " + str(value))
                        return TEXT
        elif type == "accessibilityid":
            for forever in range(1, self.max_times):
                if forever < self.circle_times:
                    try:
                        element = self.driver.find_element_by_accessibility_id(value)
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        time.sleep(self.sleep_time)
                    else:
                        TEXT = element.get_attribute("name")
                        if TEXT != '':
                            self.out_log("input successfully : " + str(value))
                            return TEXT
                        else:
                            self.out_log("continue to get_text")
                            continue
                else:
                    try:
                        element = self.driver.find_element_by_accessibility_id(value)
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        self.driver.find_element_by_accessibility_id(value)
                    else:
                        TEXT = element.get_attribute("name")
                        self.out_log("input successfully : " + str(value))
                        return TEXT
        elif type == "classname":
            for forever in range(1, self.max_times):
                if forever < self.circle_times:
                    try:
                        element = self.driver.find_element_by_class_name(value)
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        time.sleep(self.sleep_time)
                    else:
                        TEXT = element.get_attribute("name")
                        if TEXT != '':
                            self.out_log("input successfully : " + str(value))
                            return TEXT
                        else:
                            self.out_log("continue to get_text")
                            continue
                else:
                    try:
                        element = self.driver.find_element_by_class_name(value)
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        self.driver.find_element_by_class_name(value)
                    else:
                        TEXT = element.get_attribute("name")
                        self.out_log("input successfully : " + str(value))
                        return TEXT
        elif type == "name":
            for forever in range(1, self.max_times):
                if forever < self.circle_times:
                    try:
                        element = self.driver.find_element_by_name(value)
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        time.sleep(self.sleep_time)
                    else:
                        TEXT = element.get_attribute("name")
                        if TEXT != '':
                            self.out_log("input successfully : " + str(value))
                            return TEXT
                        else:
                            self.out_log("continue to get_text")
                            continue
                else:
                    try:
                        element = self.driver.find_element_by_name(value)
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        self.driver.find_element_by_name(value)
                    else:
                        TEXT = element.get_attribute("name")
                        self.out_log("input successfully : " + str(value))
                        return TEXT
        elif type == "uiautomator":
            for forever in range(1, self.max_times):
                if forever < self.circle_times:
                    try:
                        element = self.driver.find_element_by_android_uiautomator(value)
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        time.sleep(self.sleep_time)
                    else:
                        TEXT = element.get_attribute("name")
                        if TEXT != '':
                            self.out_log("input successfully : " + str(value))
                            return TEXT
                        else:
                            self.out_log("continue to get_text")
                            continue
                else:
                    try:
                        element = self.driver.find_element_by_android_uiautomator(value)
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        self.driver.find_element_by_android_uiautomator(value)
                    else:
                        TEXT = element.get_attribute("name")
                        self.out_log("input successfully : " + str(value))
                        return TEXT
        elif type == "uiautomator_id":
            for forever in range(1, self.max_times):
                if forever < self.circle_times:
                    try:
                        element = self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("%s")'%str(value))
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        time.sleep(self.sleep_time)
                    else:
                        TEXT = element.get_attribute("name")
                        if TEXT != '':
                            self.out_log("input successfully : " + str(value))
                            return TEXT
                        else:
                            self.out_log("continue to get_text")
                            continue
                else:
                    try:
                        element = self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("%s")'%str(value))
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("%s")'%str(value))
                    else:
                        TEXT = element.get_attribute("name")
                        self.out_log("input successfully : " + str(value))
                        return TEXT
        elif type == "uiautomator_text":
            for forever in range(1, self.max_times):
                if forever < self.circle_times:
                    try:
                        element = self.driver.find_element_by_android_uiautomator('new UiSelector().text("%s")'%str(value))
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        time.sleep(self.sleep_time)
                    else:
                        TEXT = element.get_attribute("name")
                        if TEXT != '':
                            self.out_log("input successfully : " + str(value))
                            return TEXT
                        else:
                            self.out_log("continue to get_text")
                            continue
                else:
                    try:
                        element = self.driver.find_element_by_android_uiautomator('new UiSelector().text("%s")'%str(value))
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        self.driver.find_element_by_android_uiautomator('new UiSelector().text("%s")'%str(value))
                    else:
                        TEXT = element.get_attribute("name")
                        self.out_log("input successfully : " + str(value))
                        return TEXT
        elif type == "uiautomator_classname":
            for forever in range(1, self.max_times):
                if forever < self.circle_times:
                    try:
                        element = self.driver.find_element_by_android_uiautomator('new UiSelector().className("%s")'%str(value))
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        time.sleep(self.sleep_time)
                    else:
                        TEXT = element.get_attribute("name")
                        if TEXT != '':
                            self.out_log("input successfully : " + str(value))
                            return TEXT
                        else:
                            self.out_log("continue to get_text")
                            continue
                else:
                    try:
                        element = self.driver.find_element_by_android_uiautomator('new UiSelector().className("%s")'%str(value))
                    except NoSuchElementException as msg:
                        self.out_log("no such element : " + str(value))
                        self.driver.find_element_by_android_uiautomator('new UiSelector().className("%s")'%str(value))
                    else:
                        TEXT = element.get_attribute("name")
                        self.out_log("input successfully : " + str(value))
                        return TEXT
    def get_screenSize(self):
        #获取屏幕尺寸
        x = self.get_window_size()['width']
        y = self.get_window_size()['height']
        return (x, y)
    def swipeLeft(self):
        self.out_log('swipeLeft')
        l = self.get_screenSize()
        y1 = int(l[1] * 0.5)
        x1 = int(l[0] * 0.95)
        x2 = int(l[0] * 0.25)
        self.swipe(x1, y1, x2, y1, 1000)
    def getTime(self):
        self.now = time.strftime("%Y-%m-%d %H_%M_%S")
        return self.now
    def getScreenShot(self, module):
        time = self.getTime()
        image_file = GL.SCREENSHOTS_DIR + '/screenshots/%s_%s.png' % (module, time)
        logging.info('get %s screenshot' % module)
        self.driver.get_screenshot_as_file(image_file)
    def out_log(self,info):
        return logging.info(str(info))
    # 隐式等待
    def wait(self, seconds):
        self.out_log("implicitly wait for : "+str(seconds)+" seconds")
        self.driver.implicitly_wait(seconds)
    def Get_text_PC(self, type, value):
        if type == "xpath":
            element_text = self.driver.find_element_by_xpath(value).text
            self.out_log(str(element_text))
            return element_text
    # 强制等待
    def sleep(self, seconds):
        self.out_log("sleep for : "+str(seconds)+" seconds")
        time.sleep(seconds)

    def wait_and_sleep(self,wait_seconds,sleep_seconds):
        self.out_log("wait for: "+str(wait_seconds)+" seconds , sleep for "+str(sleep_seconds)+" seconds" )
        self.wait(wait_seconds)
        self.sleep(sleep_seconds)

    def swipe_bar(self):
        js = "var q=document.documentElement.scrollTop=10000"
        self.driver.execute_script(js)
        self.out_log("swipe the bar to bottom")

    def time_date(self):
        # 获得当前时间时间戳
        now = int(time.time())
        # 转换为其他日期格式,如:"%Y-%m-%d %H:%M:%S"
        timeStruct = time.localtime(now)
        strTime = time.strftime("%Y-%m-%d %H:%M:%S", timeStruct)
        return strTime