from DrissionPage import Chromium
# from DrissionPage.common import Settings
import datetime

# 创建对象
cart = Chromium(9224).latest_tab

# 指定秒杀时间，格式为“时:分:秒.毫秒”，无需设定日期
kill_time = "20:00:00.00000000"

cart.get("https://cart.jd.com/cart_index")
# 等待登录完成，直到购物车全选按钮出现，超时时间我设置为1分钟
cart.wait.ele_displayed('x://*[@id="cart-body"]/div[2]/div[4]/div[1]/div/input',timeout=60)

while(True):
    # 获取当前时间
    now = datetime.datetime.now().strftime('%H:%M:%S.%f')
    print(now) # 打印当前时间测试
    # 判断当前时间是否到达了秒杀时间
    if(now>kill_time):
        try:
            # 判断商品是否全选(京东购物车会记住上次选择的商品)
            while cart.ele('x://*[@id="cart-body"]/div[2]/div[4]/div[1]/div/input').attr('clstag').split('|')[-1].startswith('0'):
                # 没有全选的情况，点击购物车全选按钮
                cart.ele('x://*[@id="cart-body"]/div[2]/div[4]/div[1]/div/input').click()
            # 点击结算按钮
            cart.ele('去结算').click()
            # 开启找不到元素立即抛出异常，用于勾选全选按钮的判断
            # Settings.raise_when_ele_not_found = True
            # if cart.ele('知道了'):# 根据没有选择商品的弹窗来判断是否全选商品
            #     cart.ele('知道了').click()
            #     cart.ele('x://*[@id="cart-body"]/div[2]/div[4]/div[1]/div/input').click()
            #     cart.ele('去结算').click()
            # # 关闭找不到元素立即抛出异常，确保后续页面有足够时间正常加载
            # Settings.raise_when_ele_not_found = False
            # 如果订单结算时要输入密码，可以取消注释下面的代码，并更改123456为你自己的支付密码
            # cart.ele('.quark-pw-result-input').input("123456")
            # 点击提交订单
            cart.wait.ele_displayed('x://*[@id="order-submit"]/b', timeout=60) # 等待提交订单按钮完全加载
            cart.ele('x://*[@id="order-submit"]/b').click()
            # 点击立即支付
            cart.ele('x://*[@id="indexBlurId"]/div[2]/div[1]/div[2]/div/div[2]/div[2]/div[2]/div/div/div[1]').click()
            # 自动填充密码(需要取消注释下面的代码，修改成你自己的支付密码)
            # cart.ele('x://*[@id="validateShortFake"]').input('123456')
            # 点击立即支付(需要取消注释下面的代码)
            # cart.ele('x://*[@id="baseMode"]/div/div[2]/div/div[2]/div/div/div[1]').click()
            break
        except Exception as err:
            # 如果发生任何异常都进行捕捉，防止浏览器退出
            print("%s\n发生了错误，请手动完成后续步骤"%err+input())
    # 判断当前秒数是不是0，实现间隔一分钟刷新页面，防止掉登录(京东购物车会记住上次选择的商品)
    if(datetime.datetime.now().second == 0):
        while(True):
            cart.refresh() # DrissionPage的页面刷新方法，内置了wait.load_start()程序会自动等待加载结束
            try:
                # 等待全选按钮加载
                cart.wait.ele_displayed('x://*[@id="cart-body"]/div[2]/div[4]/div[1]/div/input')
                break # 按钮加载成功说明没有问题，跳出循环
            except:
                # 没有成功加载按钮说明出现了错误，无论什么错误都再次刷新页面
                continue

# 成功的信息输出和测试时的程序暂停
input('恭喜，抢购成功')
