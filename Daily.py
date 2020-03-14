from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

url="https://thos.tsinghua.edu.cn/"

#edge_opt = Options()      # 创建参数设置对象.
#edge_opt.add_argument('--headless')   # 无界面化.
#edge_opt.add_argument('--disable-gpu')    # 配合上面的无界面化.
driver = webdriver.Edge()
driver.implicitly_wait("10")
driver.get(url)

#登录
#driver.find_element_by_id('i_user').send_keys("你的学号")
#driver.find_element_by_id('i_pass').send_keys("你的密码")
driver.find_element_by_link_text("登录").click()
driver.implicitly_wait("20")

#日报
driver.find_element_by_name("【日报】学生健康和出行情况报告").click()

#提交
time.sleep(15)
driver.find_element_by_id("commit").click()

driver.quit()
