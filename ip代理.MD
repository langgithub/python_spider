# proxy_server

在大规模抓取的时候需要大量 proxy 的支持，为了方便管理做成了一个服务。参考 [IPProxyPool](https://github.com/qiyeboy/IPProxyPool) 的API部分， 但是它在实际工作中不是很方便，我对此做了改动。

使用的框架是 Flask。现在已经完成了 mongodb 实现，其他数据库可以自行实现。

proxy_helper.py 是我封装的获取 proxy 和删除 proxy 的函数，可以直接使用。

## 零、安装运行

```
pip install -r requirements.txt

# 运行接口服务
python proxy_server.py
gunicorn --config gunicorn_config_proxy.py proxy_server:app
# 运行获取讯代理
python get_proxy_from_api_xdaili.py
python sched_check_adsl_proxys.py
python run_adsl_helper.py
python run_toproxy.py
```

## 一、功能

#### 1、获取代理
按照来源分为两种：
##### 1、自己搭建的代理
##### 2、网上采集的免费代理
按照获取分为三种：
##### 1、直接脚本导入，参考
##### 2、使用[IPProxyPool](https://github.com/qiyeboy/IPProxyPool)的方式获取
##### 3、购买网上的代理服务，参考

#### 2、对外提供代理服务
具体参考API



## 二、API

最近发现了一个很好用的API管理网站[eolinker](https://www.eolinker.com)，界面好看、功能好用，还开源，强烈推荐一下。

本项目的接口已经移到了上面，访问地址是: [proxy_server API in echolinker](https://sp.eolinker.com/lf75YR) 。

# 三、demo

参考demo文件夹下的ip4_demo.py

运行 python ip4_demo.py

我们现在使用的代理是[讯代理](http://www.xdaili.cn/buyproxy)的混拨代理，其特点是
