#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
邀请页
"""
from appium.webdriver.common.mobileby import MobileBy

# from app.page.contactadd_page import ContactAddPage


class MemberInviteMenuPage:
    def __init__(self, driver):
        self.driver = driver

    def add_member_menual(self):
        # 点击【手动输入添加】
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        from app.page.contactadd_page import ContactAddPage
        return ContactAddPage(self.driver)

    def get_toast(self):
        result = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").get_attribute('text')
        return result
