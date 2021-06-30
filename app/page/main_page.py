#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
首页
"""
from appium.webdriver.common.mobileby import MobileBy

from app.page.addresslist_page import AddressListPage


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def goto_message(self):
        """
        进入到消息页
        :return:
        """
        pass

    def goto_address(self):
        """
        进入到通讯录页面
        :return:
        """
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        return AddressListPage(self.driver)