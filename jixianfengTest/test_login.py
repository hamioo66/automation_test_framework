# -*-coding:UTF-8 -*-
import unittest
from framework.browser_engine import BrowserEngine
from jixianfengPage.login import Login
class jixianfeng_login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """
        cls.driver.quit()
    def test_login(self):
        login=Login(self.driver)
        login.fileTxt('../file/login.txt',2)
        #login.login()


