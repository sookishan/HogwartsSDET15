#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
测试用例
"""
from app.page.app import App


class TestContact:
    def setup(self):
        self.app = App()
        self.main = self.app.start().goto_main()

    def test_addcontact(self):
        name = 'zhangsan7'
        gender = '女'
        phonenum = '13000000007'
        result = self.main.goto_address()\
            .click_addmember()\
            .add_member_menual()\
            .add_contact(name, gender, phonenum).get_toast()
        assert '添加成功' == result
