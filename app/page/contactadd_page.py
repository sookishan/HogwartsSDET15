#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
添加联系人页面
"""
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
# from app.page.member_invite_menu_page import MemberInviteMenuPage


class ContactAddPage:
    def __init__(self, driver):
        self.driver = driver

    def add_contact(self, name, gender, phonenum):
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[contains(@text,'姓名')]/../*[@text='必填']").send_keys(name)
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[contains(@text,'性别')]/..//*[@text='男']").click()
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element(MobileBy.XPATH, "//*[@text='女']"))
        if gender == '男':
            self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        else:
            self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()

        self.driver.find_element(MobileBy.XPATH, "//*[@text='手机号']").send_keys(phonenum)
        # 保存
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()

        from app.page.member_invite_menu_page import MemberInviteMenuPage
        return MemberInviteMenuPage(self.driver)
