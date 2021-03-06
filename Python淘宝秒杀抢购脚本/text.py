import datetime #模块
import time
#全自动化Python代码操作
from selenium import webdriver

now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
times = "2021-12-31 15:00:00.00000000"
#browser = webdriver.Chrome("https://www.taobao.com")
"""
加载Chrome驱动，具体下载根据chrome浏览器版本下载，
http://npm.taobao.org/mirrors/chromedriver/找到对应的版本，下载并解压到自己想放的路径中
"""
browser = webdriver.Chrome(executable_path="D:\hromedriver\chromedriver.exe") #加载Chrome驱动
browser.get("https://www.taobao.com")
time.sleep(3)                               #点击
browser.find_element_by_link_text("亲，请登录").click()

print(f"请尽快扫码登录")
time.sleep(10)
browser.get("https://cart.taobao.com/cart.htm")
time.sleep(5)

# 是否全选购物车
while True:
    try:
        if browser.find_element_by_id("J_SelectAll1"):
            browser.find_element_by_id("J_SelectAll1").click()
            break
    except:
        print(f"找不到购买按钮")

while True:
    #获取电脑现在的时间,                      year month day
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    # 对比时间，时间到的话就点击结算
    print(now)
    #判断是不是到了秒杀时间?
    if now > times:
        # 点击结算按钮
        while True:
            try:
                if browser.find_element_by_link_text("结 算"):
                    print("here")
                    browser.find_element_by_link_text("结 算").click()
                    print(f"主人,程序锁定商品,结算成功")
                    break
            except:
                pass
        # 点击提交订单按钮
        while True:
            try:
                if browser.find_element_by_link_text('提交订单'):
                    browser.find_element_by_link_text('提交订单').click()
                    print(f"抢购成功，请尽快付款")
            except:
                print(f"主人,我已帮你抢到商品啦,您来支付吧")
                break
        time.sleep(0.01)
