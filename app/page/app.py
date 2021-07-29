#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
app.py 模块，存放App相关的一些操作。
比如 启动应用，重启应用，停止应用，进入到首页
"""
import yaml
from appium import webdriver
from app.page.base_page import BasePage
from app.page.main_page import MainPage

with open('../datas/caps.yml') as f:
    myconfig = yaml.safe_load(f)
    caps = myconfig['desirecaps']
    ip = myconfig['server']['ip']
    port = myconfig['server']['port']

class App(BasePage):
    def start(self):
        if self.driver == None:
            # 启动app
            # 定义了一个字典
            # caps = {}
            # caps["platformName"] = "Android"
            # caps["platformVersion"] = "6.0.1"
            # caps["deviceName"] = "test"
            # caps["appActivity"] = ".launch.WwMainActivity"
            # caps["appPackage"] = "com.tencent.wework"
            # # noReset 保留缓存，比如登录状态
            # caps["noReset"] = "true"
            # # 不停止应用，直接运行测试用例
            # # caps["dontStopAppOnReset"] = "true"
            # caps['skipDeviceInitialization'] = "true"
            # caps['skipServerInstallation'] = "true"
            # caps["unicodeKeyboard"] = "true"
            # caps["resetKeyboard"] = "true"
            # # caps["settings[waitForId..]"]
            # # 关键 localhost:4723 本机ip ：127.0.0.1
            self.driver = webdriver.Remote(f"http://{ip}:{port}/wd/hub", caps)
            self.driver.implicitly_wait(5)
        else:
            self.driver.launch_app()
            # self.driver.start_activity(package,activity)
        # 停留在当前页面
        return self

    def restart(self):
        # 重启app
        self.driver.close_app()
        self.driver.launch_app()

    def stop(self):
        # 停止app
        self.driver.quit()

    def goto_main(self) -> MainPage:
        # 进入首页
        return MainPage(self.driver)
