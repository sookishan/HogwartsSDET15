#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
例子
"""
from time import sleep
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait


class TestDemo:
    def setup(self):
        # 定义了一个字典
        caps = {}
        caps["platformName"] = "Android"
        caps["platformVersion"] = "6.0.1"
        caps["deviceName"] = "test"
        caps["appActivity"] = ".launch.WwMainActivity"
        caps["appPackage"] = "com.tencent.wework"
        caps["noReset"] = "true"
        caps["unicodeKeyboard"] = "true"
        caps["resetKeyboard"] = "true"
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

    def test_demo(self):
        el4 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.ListView/android.widget.RelativeLayout[4]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.TextView")
        el4.click()
        el5 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[4]")
        el5.click()
        el6 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.RelativeLayout/android.widget.ListView/android.widget.RelativeLayout[4]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.TextView")
        el6.click()

    def test_outsidedaka(self):
        self.driver.find_element(MobileBy.XPATH,"//*[@text='工作台']").click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()\
                                 .scrollable(true).instance(0))\
                                 .scrollIntoView(new UiSelector()\
                                 .text("打卡").instance(0));').click()
        # settings
        self.driver.update_settings({"waitForIdleTimeout": 2})
        self.driver.find_element(MobileBy.XPATH,"//*[@text='外出打卡']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'次外出')]").click()
        # sleep(2)
        # assert "外出打卡成功" in self.driver.page_source
        #显示等待
        WebDriverWait(self.driver, 10).until(lambda x: "外出打卡成功" in x.page_source)

    '''
    点击添加成员
    '''
    def test_addcontact(self):
        name = 'zhangsan7'
        gender = '女'
        telephone = '13000000005'
        # 进入到通讯录界面
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']").click()
        # 滚动查找【添加成员】
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()\
                                 .scrollable(true).instance(0))\
                                 .scrollIntoView(new UiSelector()\
                                 .text("添加成员").instance(0));').click()
        sleep(3)
        # 点击【手动输入添加】
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        sleep(1)
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[contains(@text,'姓名')]/../*[@text='必填']").send_keys(name)
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[contains(@text,'性别')]/..//*[@text='男']").click()
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element(MobileBy.XPATH, "//*[@text='女']"))
        if gender == '男':
            self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        else:
            self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()

        self.driver.find_element(MobileBy.XPATH, "//*[@text='手机号']").send_keys(telephone)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()
        sleep(1)
        # print(self.driver.page_source)
        result = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").get_attribute('text')
        assert '添加成功' == result

    '''
    删除成员
    '''
    def test_deletecontect(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/ie5').click()
        sleep(1)
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[@text='zhangsan6']/../../../..//*[\
                                 contains(@resource-id,'com.tencent.wework:id/gnw')]").click()
        sleep(1)
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/eqy').click()
        sleep(1)
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/bom').click()
        sleep(3)
        assert 'zhangsan6' not in self.driver.page_source






    def teardown(self):
        self.driver.quit()
