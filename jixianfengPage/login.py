# -*- coding=UTF-8 -*-
from framework.base_page import BasePage
from framework.logger import Logger
logger=Logger(logger="BasePage").getlog()
"""集鲜丰登录"""
class Login(BasePage):
    telephone="name=>telephone" #用户名
    password="name=>password"   #密码
    loginBtn="name=>loginBtn"   #登录按钮

    def fileTxt(self,file,num):
        user_file = open(file, 'r')
        values = user_file.readlines()
        user_file.close()
        i = []
        for search in values:
            i.append(search)
        type = i[num].split(':')[0]
        keys = i[num].split(':')[1]
        username = keys.split(',')[0]
        password = keys.split(',')[1]
        num=num+1
        logger.info("用户名是:%s,密码是:%s",(username,password))
        return username,password,num
    def login(self):
        self.type(self.telephone)
        self.type(self.password)
        # self.click(self.,num)


