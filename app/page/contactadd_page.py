#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
添加联系人页面
"""
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
# from app.page.member_invite_menu_page import MemberInviteMenuPage
from app.page.base_page import BasePage


class ContactAddPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver

    def add_contact(self, name, gender, phonenum):
        self.find(MobileBy.XPATH,
                                 "//*[contains(@text,'姓名')]/../*[@text='必填']").send_keys(name)
        self.find(MobileBy.XPATH,
                                 "//*[contains(@text,'性别')]/..//*[@text='男']").click()
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element(MobileBy.XPATH, "//*[@text='女']"))
        if gender == '男':
            self.find(MobileBy.XPATH, "//*[@text='男']").click()
        else:
            self.find(MobileBy.XPATH, "//*[@text='女']").click()

        self.find(MobileBy.XPATH, "//*[@text='手机号']").send_keys(phonenum)
        # 保存
        self.find(MobileBy.XPATH, "//*[@text='保存']").click()

        from app.page.member_invite_menu_page import MemberInviteMenuPage
        return MemberInviteMenuPage(self.driver)
