from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time

url="https://thos.tsinghua.edu.cn/"

chrome_opt = Options()      # 创建参数设置对象.

#如果希望无界面化, 请取消以下两行代码的注释

#chrome_opt.add_argument('--headless')   # 无界面化.
#chrome_opt.add_argument('--disable-gpu')    # 配合上面的无界面化.

driver = webdriver.Chrome(options=chrome_opt)
driver.implicitly_wait("10")
driver.get(url)

#登录
driver.find_element_by_id("i_user").send_keys("your_id") #请将引号内的内容更改为你的学号
driver.find_element_by_id("i_pass").send_keys("your_passwd") #请将引号内的内容更改为你的密码
driver.find_element_by_link_text("登录").click()
driver.implicitly_wait("20")

#日报
driver.find_element_by_name("【日报】学生健康和出行情况报告").click()

#提交
time.sleep(15)
driver.find_element_by_id("commit").click()

driver.quit()
print("提交成功")
