class BaseView(object):
    def __init__(self, driver):
        self.driver = driver


    #PC端的公共方法封装
    def get_url(self,url):
        return self.driver.get(url)

    def maximize_window(self):
        return self.driver.maximize_window()


    # 获取屏幕尺寸
    def get_window_size(self):
        return self.driver.get_window_size()

    # 滑动
    def swipe(self, start_x, start_y, end_x, end_y, duration):
        return self.driver.swipe(start_x, start_y, end_x, end_y, duration)
