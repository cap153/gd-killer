from DrissionPage import ChromiumPage
import datetime

# 创建对象
page = ChromiumPage()

# 指定秒杀时间
kill_time = "2024-04-27 11:53:00.00000000"

# 打开京东网页
page.get("https://www.jd.com")
# 点击购物车
cart = page.ele('x://*[@id="settleup"]/div[1]/a').click.for_new_tab()
# 等待登录完成，直到购物车全选按钮出现，超时时间我设置为1分钟
cart.wait.ele_displayed('x://*[@id="cart-body"]/div[2]/div[4]/div[1]/div/input',timeout=60)
# 判断商品是否全选(京东购物车会记住上次选择的商品)
if cart.ele('x://*[@id="cart-body"]/div[2]/div[4]/div[1]/div/input').attr('clstag').split('|')[-1].startswith('0'):
    # 没有全选的情况，点击购物车全选按钮
    cart.ele('x://*[@id="cart-body"]/div[2]/div[4]/div[1]/div/input').click()

while(True):
    # 获取当前时间
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    print(now) # 打印当前时间测试
    # 判断当前时间是否到达了秒杀时间
    if(now>kill_time):
        # 点击结算按钮
        cart.ele('去结算').click()
        # 点击提交订单
        cart.ele('x://*[@id="order-submit"]/b').click()
        # 点击立即支付
        cart.ele('x://*[@id="indexBlurId"]/div[2]/div[1]/div[2]/div/div[2]/div[2]/div[2]/div/div/div[1]').click()
        # 自动填充密码(需要修改成你自己的支付密码)
        # cart.ele('x://*[@id="validateShortFake"]').input('123456')
        # 点击立即支付
        # cart.ele('x://*[@id="baseMode"]/div/div[2]/div/div[2]/div/div/div[1]').click()

        break
    # 判断当前秒数是不是0，实现间隔一分钟刷新页面，防止掉登录(京东购物车会记住上次选择的商品)
    if(datetime.datetime.now().second == 0):
        page.refresh() # DrissionPage的页面刷新方法，内置了wait.load_start()程序会自动等待加载结束

# 测试时的程序暂停
input()
