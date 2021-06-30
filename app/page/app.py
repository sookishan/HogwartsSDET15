#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
app.py 模块，存放App相关的一些操作。
比如 启动应用，重启应用，停止应用，进入到首页
"""
from appium import webdriver

from app.page.main_page import MainPage


class App:
    def start(self):
        # 启动app
        # 定义了一个字典
        caps = {}
        caps["platformName"] = "Android"
        caps["platformVersion"] = "6.0.1"
        caps["deviceName"] = "test"
        caps["appActivity"] = ".launch.WwMainActivity"
        caps["appPackage"] = "com.tencent.wework"
        # noReset 保留缓存，比如登录状态
        caps["noReset"] = "true"
        # 不停止应用，直接运行测试用例
        # caps["dontStopAppOnReset"] = "true"
        caps['skipDeviceInitialization'] = "true"
        caps['skipServerInstallation'] = "true"
        caps["unicodeKeyboard"] = "true"
        caps["resetKeyboard"] = "true"
        # caps["settings[waitForId..]"]
        # 关键 localhost:4723 本机ip ：127.0.0.1
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

        # 停留在当前页面
        return self

    def restart(self):
        # 重启app
        pass

    def stop(self):
        # 停止app
        self.driver.quit()

    def goto_main(self) -> MainPage:
        # 进入首页
        return MainPage(self.driver)
