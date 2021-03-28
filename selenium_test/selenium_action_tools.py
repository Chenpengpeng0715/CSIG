# -*- coding:utf-8 -*-
# author:
# datetime:2019/12/5 11:00
import os
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
from time import ctime, sleep


class SeleniumTools(object):

    # 初始化浏览器驱动
    def __init__(self):
        self.device = webdriver.Chrome(r'D:\faceid\chromedriver.exe')

    # 元素定位
    def find_element(self):
        # 通过id定位:
        self.device.find_element_by_id("kw")
        # 通过name定位:
        self.device.find_element_by_name("wd")
        # 通过class name定位:
        self.device.find_element_by_class_name("s_ipt")
        # 通过tag name定位:
        self.device.find_element_by_tag_name("input")
        # 通过xpath定位，xpath定位有N种写法，这里列几个常用写法:
        self.device.find_element_by_xpath("//*[@id='kw']")
        # 通过css定位，css定位有N种写法，这里列几个常用写法:
        self.device.find_element_by_css_selector("#kw")
        # 通过link text定位:
        self.device.find_element_by_link_text("新闻")
        # 通过link text定位:
        self.device.find_element_by_partial_link_text("新")

    # 浏览器控制
    def control_webdriver(self):
        # 访问百度首页
        first_url = "http://www.baidu.com"
        self.device.get(first_url)

        # 访问新闻页面
        second_url = 'http://news.baidu.com'
        print("now access %s" % second_url)
        self.device.get(second_url)

        # 返回（后退）到百度首页
        print("back to %s" % first_url)
        self.device.back()

        # 前进到新闻页
        print("forward to %s" % second_url)
        self.device.forward()

        # 参数数字为像素点
        print("设置浏览器宽480、高800显示")
        self.device.set_window_size(480, 800)

        # 浏览器最大化
        self.device.maximize_window()

        # 刷新当前页面
        self.device.refresh()

        # 截取当前窗口，并指定截图图片的保存位置
        self.device.get_screenshot_as_file("D:\\baidu_img.jpg")

        # 关闭单个窗口
        self.device.close()

        # 关闭所有窗口
        self.device.quit()

    # webdriver常用方法
    def action_tool(self):
        self.device.get("https://www.baidu.com")
        # 清除文本
        self.device.find_element_by_id("kw").clear()
        # 模拟按键输入
        self.device.find_element_by_id("kw").send_keys("selenium")
        # 模拟点击
        self.device.find_element_by_id("su").click()
        # 提交表单
        search_text = self.device.find_element_by_id('kw')
        search_text.send_keys('selenium')
        search_text.submit()

        # 获得输入框的尺寸
        size = self.device.find_element_by_id('kw').size
        print(size)

        # 返回百度页面底部备案信息
        text = self.device.find_element_by_id("cp").text
        print(text)

        # 返回元素的属性值， 可以是 id、 name、 type 或其他任意属性
        attribute = self.device.find_element_by_id("kw").get_attribute('type')
        print(attribute)

        # 返回元素的结果是否可见， 返回结果为 True 或 False
        result = self.device.find_element_by_id("kw").is_displayed()
        print(result)

        self.device.quit()

    # 鼠标事件
    def mouse_action(self):
        self.device.get("https://www.baidu.cn")

        # 定位到要悬停的元素
        above = self.device.find_element_by_link_text("设置")
        # 定位到需要拖动到的目标元素
        target = self.device.find_element_by_link_text("新闻")
        # 对定位到的元素执行鼠标悬停操作
        ActionChains(self.device).move_to_element(above).perform()
        # 对定位到的元素执行鼠标点击操作
        ActionChains(self.device).click(above).perform()
        # 对定位到的元素执行鼠标双击操作
        ActionChains(self.device).double_click(above).perform()
        # 对定位到的元素执行鼠标右键操作
        ActionChains(self.device).context_click(above).perform()
        # 对定位到的元素执行鼠标拖动操作
        ActionChains(self.device).drag_and_drop(above, target).perform()

    # 键盘事件
    def keyboard_action(self):
        
        self.device.get("http://www.baidu.com")

        # 输入框输入内容
        self.device.find_element_by_id("kw").send_keys("seleniumm")

        # 删除多输入的一个 m
        self.device.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)

        # 输入空格键+“教程”
        self.device.find_element_by_id("kw").send_keys(Keys.SPACE)
        self.device.find_element_by_id("kw").send_keys("教程")

        # ctrl+a 全选输入框内容
        self.device.find_element_by_id("kw").send_keys(Keys.CONTROL, 'a')

        # ctrl+x 剪切输入框内容
        self.device.find_element_by_id("kw").send_keys(Keys.CONTROL, 'x')

        # ctrl+v 粘贴内容到输入框
        self.device.find_element_by_id("kw").send_keys(Keys.CONTROL, 'v')

        # 通过回车键来代替单击操作
        self.device.find_element_by_id("su").send_keys(Keys.ENTER)
        self.device.quit()
        '''
        send_keys(Keys.BACK_SPACE) 删除键（BackSpace）

        send_keys(Keys.SPACE) 空格键(Space)
        
        send_keys(Keys.TAB) 制表键(Tab)
        
        send_keys(Keys.ESCAPE) 回退键（Esc）
        
        send_keys(Keys.ENTER) 回车键（Enter）
        
        send_keys(Keys.CONTROL,'a') 全选（Ctrl+A）
        
        send_keys(Keys.CONTROL,'c') 复制（Ctrl+C）
        
        send_keys(Keys.CONTROL,'x') 剪切（Ctrl+X）
        
        send_keys(Keys.CONTROL,'v') 粘贴（Ctrl+V）
        
        send_keys(Keys.F1) 键盘 F1
        
        ……
        
        send_keys(Keys.F12) 键盘 F12
        '''

    # 断言
    def check_result(self):
        self.device.get("https://www.baidu.com")

        print('Before search================')

        # 打印当前页面title
        title = self.device.title
        print(title)

        # 打印当前页面URL
        now_url = self.device.current_url
        print(now_url)

        self.device.find_element_by_id("kw").send_keys("selenium")
        self.device.find_element_by_id("su").click()
        time.sleep(1)

        print('After search================')

        # 再次打印当前页面title
        title = self.device.title
        print(title)

        # 打印当前页面URL
        now_url = self.device.current_url
        print(now_url)

        # 获取结果数目
        user = self.device.find_element_by_class_name('nums').text
        time.sleep(5)
        print(user)

        self.device.quit()
        
    # 等待
    def element_wait(self):
        # 显式等待使WebdDriver等待某个条件成立时继续执行，否则在达到最大时长时抛出超时异常（TimeoutException）
        '''
        WebDriverWait类是由WebDirver 提供的等待方法。在设置时间内，默认每隔一段时间检测一次当前页面元素是否存在，如果超过设置时间检测不到则抛出异常。具体格式如下：

        WebDriverWait(driver, timeout, poll_frequency=0.5, ignored_exceptions=None)
        driver ：浏览器驱动。

        timeout ：最长超时时间，默认以秒为单位。

        poll_frequency ：检测的间隔（步长）时间，默认为0.5S。

        ignored_exceptions ：超时后的异常信息，默认情况下抛NoSuchElementException异常。
        WebDriverWait()一般由until()或until_not()方法配合使用，下面是until()和until_not()方法的说明。

        until(method, message=‘’)
        调用该方法提供的驱动程序作为一个参数，直到返回值为True。

        until_not(method, message=‘’)
        调用该方法提供的驱动程序作为一个参数，直到返回值为False。

        在本例中，通过as关键字将expected_conditions 重命名为EC，并调用presence_of_element_located()方法判断元素是否存在。
        :return:
        '''

        self.device.get("http://www.baidu.com")
        # 等待5s直到找到ID为'kw'的元素才开始下一步
        element = WebDriverWait(self.device, 5, 0.5).until(
            EC.presence_of_element_located((By.ID, "kw"))
        )
        element.send_keys('selenium')

        # WebDriver提供了implicitly_wait()方法来实现隐式等待，默认设置为0。它的用法相对来说要简单得多。
        # 设置隐式等待为10秒
        self.device.implicitly_wait(10)
        self.device.get("http://www.baidu.com")

        try:
            print(ctime())
            self.device.find_element_by_id("kw22").send_keys('selenium')
        except NoSuchElementException as e:
            print(e)
        finally:
            print(ctime())
            self.device.quit()
        
        '''
        implicitly_wait()默认参数的单位为秒，本例中设置等待时长为10秒。首先这10秒并非一个固定的等待时间，它并不影响脚本的执行速度。
        其次，它并不针对页面上的某一元素进行等待。当脚本执行到某个元素定位时，如果元素可以定位，则继续执行；
        如果元素定位不到，则它将以轮询的方式不断地判断元素是否被定位到。假设在第6秒定位到了元素则继续执行，
        若直到超出设置时长（10秒）还没有定位到元素，则抛出异常。
        '''
        self.device.quit()
        
    # 表单切换
    def frame_change(self):
        self.device.get("http://www.126.com")
        # 根据ID选择表单进行操作
        self.device.switch_to.frame('x-URS-iframe')
        self.device.find_element_by_name("email").clear()
        self.device.find_element_by_name("email").send_keys("username")
        self.device.find_element_by_name("password").clear()
        self.device.find_element_by_name("password").send_keys("password")
        self.device.find_element_by_id("dologin").click()
        self.device.switch_to.default_content()
        # 如果id和name是随机的，可以直接定位frame(0)即第一个frame
        self.device.switch_to.frame(0)

        self.device.quit()

        # switch_to.frame()默认可以直接取表单的id或name属性。如果iframe没有可用的id和name属性，则可以通过下面的方式进行定位。

        # 先通过xpth定位到iframe
        xf = self.device.find_element_by_xpath('//*[@id="x-URS-iframe"]')

        # 再将定位对象传给switch_to.frame()方法
        self.device.switch_to.frame(xf)
        self.device.switch_to.parent_frame()
        # 除此之外，在进入多级表单的情况下，还可以通过switch_to.default_content()跳回最外层的页面。
    
    # 窗口切换
    def window_change(self):
        self.device.implicitly_wait(10)
        self.device.get("http://www.baidu.com")

        # 获得百度搜索窗口句柄
        sreach_windows = self.device.current_window_handle

        self.device.find_element_by_link_text('登录').click()
        self.device.find_element_by_link_text("立即注册").click()

        # 获得当前所有打开的窗口的句柄
        all_handles = self.device.window_handles

        # 进入注册窗口
        for handle in all_handles:
            if handle != sreach_windows:
                self.device.switch_to.window(handle)
                print('now register window!')
                self.device.find_element_by_name("account").send_keys('username')
                self.device.find_element_by_name('password').send_keys('password')
                time.sleep(2)
                # ……

        self.device.quit()
        '''
        在本例中所涉及的新方法如下：

        current_window_handle：获得当前窗口句柄。

        window_handles：返回所有窗口的句柄到当前会话。

        switch_to.window()：用于切换到相应的窗口，与上一节的switch_to.frame()
        类似，前者用于不同窗口的切换，后者用于不同表单之间的切换。
        '''

    # 警告框处理
    def message_action(self):
        # 通过switch_to_alert()方法获取当前页面上的警告框，并使用accept()方法接受警告框。
        self.device.switch_to.alert.accept()
        # 通过switch_to_alert()方法获取当前页面上的警告框，并使用text方法返回警告内容。
        self.device.switch_to.alert.text()
        # 通过switch_to_alert()方法获取当前页面上的警告框，并使用dismiss()方法解散警告框。
        self.device.switch_to.alert.dismiss()
        # 通过switch_to_alert()方法获取当前页面上的警告框，并使用send_keys()方法发送文本至警告框。
        self.device.switch_to.alert.send_keys("")

        self.device.quit()

    # 下拉框
    def select(self):
        self.device.implicitly_wait(10)
        self.device.get('http://www.baidu.com')

        # 鼠标悬停至“设置”链接
        self.device.find_element_by_link_text('设置').click()
        time.sleep(1)
        # 打开搜索设置
        self.device.find_element_by_link_text("搜索设置").click()
        time.sleep(2)

        # 搜索结果显示条数
        sel = self.device.find_element_by_xpath("//select[@id='nr']")
        Select(sel).select_by_value('50')  # 显示50条
        # driver.quit()Select类用于定位select标签。
        # select_by_value()方法用于定位下接选项中的value值。

    # 文件上传
    def file_pull(self):
        # 打开文件上传网页
        file_path = 'file:///' + os.path.abspath('upfile.html')
        self.device.get(file_path)

        # 定位上传按钮，添加本地文件，通过send_keys()方法来实现文件上传
        self.device.find_element_by_name("file").send_keys('D:\\upload_file.txt')

        self.device.quit()

    # cookie操作
    def cookie_action(self):
        '''
        WebDriver操作cookie的方法：

        get_cookies()： 获得所有cookie信息。

        get_cookie(name)： 返回字典的key为“name”的cookie信息。

        add_cookie(cookie_dict) ： 添加cookie。“cookie_dict”指字典对象，必须有name 和value 值。

        delete_cookie(name,optionsString)：删除cookie信息。“name”是要删除的cookie的名称，“optionsString”是该cookie的选项，目前支持的选项包括“路径”，“域”。

        delete_all_cookies()： 删除所有cookie信息。
        :return:
        '''
        # 获取cookie信息
        self.device.get("http://www.youdao.com")

        # 获得cookie信息
        cookie = self.device.get_cookies()
        # 将获得cookie的信息打印
        print(cookie)

        # 向cookie的name 和value中添加会话信息
        self.device.add_cookie({'name': 'key-aaaaaaa', 'value': 'value-bbbbbb'})

        # 遍历cookies中的name 和value信息并打印，当然还有上面添加的信息
        for cookie in self.device.get_cookies():
            print("%s -> %s" % (cookie['name'], cookie['value']))
        self.device.quit()