from DrissionPage import ChromiumPage
import datetime

# 创建对象
page = ChromiumPage(9223)

# 指定秒杀时间
kill_time = "2024-05-31 21:25:00.00000000"

# 打开淘宝网页
page.get("https://www.taobao.com")
# 点击购物车
page.ele('x://*[@id="J_MiniCart"]/div[1]/a/span[2]').click()
# 等待登录完成，直到购物车全选按钮出现，超时时间我设置为1分钟
page.wait.ele_displayed('x://*[@id="J_SelectAll1"]/div/label',timeout=60)
# 点击购物车全选按钮
page.ele('x://*[@id="J_SelectAll1"]/div/label').click()

while(True):
    # 获取当前时间
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    print(now) # 打印当前时间测试
    # 判断当前时间是否到达了秒杀时间
    if(now>kill_time):
        try:
            # 点击结算按钮
            page.ele('x://*[@id="J_Go"]/span').click()
            # 下单商品
            page.ele('提交订单').click()
            # 自动填充密码(需要修改成你自己的支付密码)
            # page.ele('x://*[@id="payPassword_rsainput"]').input("123456")
            # 确定
            # page.ele('x://*[@id="validateButton"]').click()
            break
        except Exception as err:
            # 如果发生任何异常都进行捕捉，防止浏览器退出
            print("%s\n发生了错误，请手动完成后续步骤"%err+input())
    # 判断当前秒数是不是0，实现间隔一分钟刷新页面，防止掉登录
    if(datetime.datetime.now().second == 0):
        page.refresh() # DrissionPage的页面刷新方法，内置了wait.load_start()程序会自动等待加载结束
        while(True):
            try:
                # 等待全选按钮加载
                page.wait.ele_displayed('x://*[@id="J_SelectAll1"]/div/label')
                break
            except:
                # 没有成功加载按钮说明出现了错误，无论什么错误都再次刷新页面
                page.refresh() # DrissionPage的页面刷新方法，内置了wait.load_start()程序会自动等待加载结束
        # 再次全选购物车
        page.ele('x://*[@id="J_SelectAll1"]/div/label').click()

# 成功的信息输出和测试时的程序暂停
input('恭喜，抢购成功')
