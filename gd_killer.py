from DrissionPage import ChromiumPage
import datetime

# 创建对象
page = ChromiumPage(9224)

# 指定秒杀时间
kill_time = "2024-05-31 21:25:00.00000000"

# 打开京东网页
page.get("https://www.jd.com")
# 点击购物车
cart = page.ele('x://*[@id="settleup"]/div[1]/a').click.for_new_tab()
# 等待登录完成，直到购物车全选按钮出现，超时时间我设置为1分钟
cart.wait.ele_displayed('x://*[@id="cart-body"]/div[2]/div[4]/div[1]/div/input',timeout=60)

while(True):
    # 获取当前时间
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    print(now) # 打印当前时间测试
    # 判断当前时间是否到达了秒杀时间
    if(now>kill_time):
        try:
            # 判断商品是否全选(京东购物车会记住上次选择的商品)
            if cart.ele('x://*[@id="cart-body"]/div[2]/div[4]/div[1]/div/input').attr('clstag').split('|')[-1].startswith('0'):
                # 没有全选的情况，点击购物车全选按钮
                cart.ele('x://*[@id="cart-body"]/div[2]/div[4]/div[1]/div/input').click()
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
        except Exception as err:
            # 如果发生任何异常都进行捕捉，防止浏览器退出
            print("%s\n发生了错误，请手动完成后续步骤"%err+input())
    # 判断当前秒数是不是0，实现间隔一分钟刷新页面，防止掉登录(京东购物车会记住上次选择的商品)
    if(datetime.datetime.now().second == 0):
        cart.refresh() # DrissionPage的页面刷新方法，内置了wait.load_start()程序会自动等待加载结束
        while(True):
            try:
                # 等待全选按钮加载
                cart.wait.ele_displayed('x://*[@id="cart-body"]/div[2]/div[4]/div[1]/div/input')
                break
            except:
                # 没有成功加载按钮说明出现了错误，无论什么错误都再次刷新页面
                cart.refresh() # DrissionPage的页面刷新方法，内置了wait.load_start()程序会自动等待加载结束

# 成功的信息输出和测试时的程序暂停
input('恭喜，抢购成功')
