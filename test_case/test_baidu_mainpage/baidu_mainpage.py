from common.utils import BasePage


class BaiDuMainPage(BasePage):

    def open_baidu_url(self):
        """打开百度首页"""
        self.visit("https://www.baidu.com")

    def search(self, keyword):
        """搜索关键字"""
        self.find_element("id", "kw").send_keys(keyword)
        self.find_element("id", "su").click()

    def click_news(self):
        """点击新闻"""
        self.find_element("link_text", "新闻").click()

    def click_hao123(self):
        """点击hao123"""
        self.find_element("link_text", "hao123").click()

    def click_map(self):
        """点击地图"""
        self.find_element("link_text", "地图").click()

    def click_baidu_hot(self):
        """未登录状态下"""
        self.click('xpath', "//*[@class='title-text c-font-medium c-color-t']")
