# gd-killer

一个基于DrissionPage的京东秒杀python脚本

# 安装环境

1. 自行安装谷歌浏览器，如果已安装谷歌浏览器还是运行不了，又或者想使用edge等其他谷歌内核浏览器，可以手动设置浏览器路径，详见[https://www.drissionpage.cn/get_start/before_start](https://www.drissionpage.cn/get_start/before_start)
2. 自行安装最新版python
3. 使用 pip 安装 DrissionPage：`pip install DrissionPage`，如果安装失败，可以尝试换国内的源试试，对应命令如下`pip install -i  http://mirrors.aliyun.com/pypi/simple/ DrissionPage --trusted-host mirrors.aliyun.com --user`

# 使用

修改变量`killer_time`为你的秒杀时间，直接用python运行即可(需要提前选择好你要购买的商品型号并添加到京东购物车以及设置好默认的发货地址等信息)

```python
python gd_killer.py
```

【京东抢购秒杀，基于DrissionPage的python脚本】 https://www.bilibili.com/video/BV1wJ4m1P7ky/?share_source=copy_web&vd_source=d34abe3786a6b85ecc07875a85795885
