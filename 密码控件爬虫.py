# encoding: utf-8
"""
--------------------------------------
@describe dd驱动键盘(window平台)
@version: 1.0
@project: PeopleBankCredit
@file: dd_keybored.py
@author: yuanlang
@time: 2019-07-15 17:06
---------------------------------------
"""
from ctypes import *
import time
import os
import win32api


class DDKeyborad():

    def __init__(self):
        parentDirPath = os.path.dirname(os.path.abspath(__file__))
        path = parentDirPath + ("\\dll\\DD81200x64.64.dll")
        # 查看路径是否正确
        # print(path)

        self.dd_dll = windll.LoadLibrary(path)

        # DD虚拟码，可以用DD内置函数转换。
        self.vk = {'5': 205, 'c': 503, 'n': 506, 'z': 501, '3': 203, '1': 201, 'd': 403, '0': 210, 'l': 409, '8': 208, 'w': 302,
                'u': 307, '4': 204, 'e': 303, '[': 311, 'f': 404, 'y': 306, 'x': 502, 'g': 405, 'v': 504, 'r': 304, 'i': 308,
                'a': 401, 'm': 507, 'h': 406, '.': 509, ',': 508, ']': 312, '/': 510, '6': 206, '2': 202, 'b': 505, 'k': 408,
                '7': 207, 'q': 301, "'": 411, '\\': 313, 'j': 407, '`': 200, '9': 209, 'p': 310, 'o': 309, 't': 305, '-': 211,
                '=': 212, 's': 402, ';': 410}
        # 需要组合shift的按键。
        self.vk2 = {'"': "'", '#': '3', ')': '0', '^': '6', '?': '/', '>': '.', '<': ',', '+': '=', '*': '8', '&': '7', '{': '[', '_': '-',
                '|': '\\', '~': '`', ':': ';', '$': '4', '}': ']', '%': '5', '@': '2', '!': '1', '(': '9'}

    def move_to(self,x,y):
        """
        功能： 模拟鼠标结对移动
        参数： 参数x , 参数y 以屏幕左上角为原点。
        例子： 把鼠标移动到分辨率1920*1080 的屏幕正中间，
        int x = 1920/2 ; int y = 1080/2;
        DD_mov(x,y)
        """
        self.dd_dll.DD_mov(x,y)

    def move_r(self,x,y):
        """
        功能： 模拟鼠标相对移动
        参数： 参数dx , 参数dy 以当前坐标为原点。
        例子： 把鼠标向左移动10像素
        DD_movR(-10,0) ;
        """
        self.dd_dll.DD_movR(x, y)

    def down_up(self, code):
        """
        功能： 模拟键盘按键
        参数： 参数1 ，请查看[DD虚拟键盘码表]。
        参数2，1=按下，2=放开
        例子： 模拟单键WIN，
        DD_key(601, 1);DD_key(601, 2);
        组合键：ctrl+alt+del
        DD_key(600,1);
        DD_key(602,1);
        DD_key(706,1);
        DD_key(706,2);
        DD_key(602,2);
        DD_key(600,2);
        """
        self.dd_dll.DD_key(self.vk[code], 1)
        self.dd_dll.DD_key(self.vk[code], 2)

    def wheel(self):
        """
        功能: 模拟鼠标滚轮
        参数: 1=前 , 2 = 后
        例子: 向前滚一格, DD_whl(1)
        :return:
        """
        pass

    def click(self):
        """
        功能： 模拟鼠标点击
        参数： 1 =左键按下 ，2 =左键放开
        4 =右键按下 ，8 =右键放开
        16 =中键按下 ，32 =中键放开
        64 =4键按下 ，128 =4键放开
        256 =5键按下 ，512 =5键放开
        例子：模拟鼠标右键 只需要连写(中间可添加延迟) DD_btn(4); DD_btn(8);
        """
        self.dd_dll.DD_btn(1)
        self.dd_dll.DD_btn(2)

    def input_str(self):
        """
        功能： 直接输入键盘上可见字符和空格
        参数： 字符串, (注意，这个参数不是int32 类型)
        例子： DD_str(“MyEmail@aa.bb.cc !@#$”)
        """
        pass

    def dd(self, i):
        # 500是shift键码。
        if i.isupper():
            # 如果是一个大写的玩意。

            # 按下抬起。
            self.dd_dll.DD_key(500, 1)
            self.down_up(i.lower())
            self.dd_dll.DD_key(500, 2)

        elif i in '~!@#$%^&*()_+{}|:"<>?':
            # 如果是需要这样按键的玩意。
            self.dd_dll.DD_key(500, 1)
            self.down_up(self.vk2[i])
            self.dd_dll.DD_key(500, 2)
        else:
            self.dd_dll.DD_key(203, 1)
            self.dd_dll.DD_key(203, 1)
            self.dd_dll.DD_key(203, 1)
            self.dd_dll.DD_key(203, 1)
            self.dd_dll.DD_key(203, 1)
            self.dd_dll.DD_key(203, 1)

    # 释放dll
    def release(self):
        win32api.FreeLibrary(self.dd_dll._handle)


if __name__ == "__main__":
    dd_input = DDKeyborad()
    time.sleep(5)
    print("这里没有指定鼠标光标位置，自己新建一个txt并点击，进入输入模式，正在输入。。。")
    # 测试按键。
    for i in '12345667':
        # print(i)
        # dd_input.dd("c")
        dd_input.dd_dll.DD_key(dd_input.vk[i], 1)
        dd_input.dd_dll.DD_key(dd_input.vk[i], 2)

    dd_input.dd_dll.DD_key(dd_input.vk["d"], 1)
    dd_input.dd_dll.DD_key(dd_input.vk["d"], 2)
    dd_input.release()




# encoding: utf-8
"""
--------------------------------------
@describe 某行测试
@version: 1.0
@project: PeopleBankCredit
@file: dirver_test.py
@author: yuanlang 
@time: 2019-07-09 15:01
---------------------------------------
"""
import time
from selenium import webdriver
from pymouse import PyMouse
from spiders.dd_keybored import DDKeyborad



from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
DesiredCapabilities.INTERNETEXPLORER['ignoreProtectedModeSettings'] = True


# 初始化driver
driver=webdriver.Ie(executable_path="C:\\work\\ie\\32\\IEDriverServer.exe")
driver.maximize_window()
# 初始化mouse
m = PyMouse()
# 初始化键盘
dd = DDKeyborad()


# 访问首页
driver.get("https://ipcrs.pbccrc.org.cn/index1.do")
time.sleep(1)
driver.find_element_by_class_name("startBtn").click()
time.sleep(1)

# 过证书验证
confirm=driver.switch_to_alert()
confirm.accept()

# 输入用户名
driver.execute_script('document.getElementById("loginname").focus()')
driver.find_element_by_id("loginname").send_keys("username")
driver.execute_script('document.getElementById("loginname").blur()')

# 输入密码
# driver.execute_script('pgeFocus();')
# 点击密码框
m.click(200, 392, 1)
time.sleep(2)
# 输入密码
for i in 'password':
    dd.down_up(i)
dd.release()
# driver.execute_script('pgeBlur()')


# 输入验证码 提交表单
img=input("输入验证码")
driver.find_element_by_id("_@IMGRC@_").send_keys(img)
driver.execute_script('FormSubmit()')
driver.execute_script('document.getElementsByName("loginForm")[0].submit()')



