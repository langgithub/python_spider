
# 爬虫知识梳理

### 爬虫开发环境介绍 
爬虫开发环境.md (https://github.com/langgithub/python_spider/blob/master/%E7%88%AC%E8%99%AB%E5%BC%80%E5%8F%91%E7%8E%AF%E5%A2%83.MD）

### 爬虫系统涉及知识
1. http协议 与 https协议 （https://langgithub.github.io/2019/06/13/http%E4%B8%8Ehttps/）
2. Cookie池
3. User-Agent池 查看文件 （https://github.com/langgithub/python_spider/blob/master/User-Agent.txt）
4. ip代理池
短效代理=>站大爷
长效代理=>购买服务器，装adsl服务
5. DNS缓存 爬虫框架会涉及
6. 抓包 fiddler,charles

### 按照业务爬虫分类：
1. 在线爬虫 （淘宝，运营商）
![在线爬虫](在线爬虫设计.png)
    * 后台控制逻辑
    * 单独启动线程轮询完成爬虫任务（读取与修改redis中存放爬虫阶段）
    * 主线程修改爬虫阶段，轮询等待结果（读取与修改redis中存放爬虫阶段）
2. 离线爬虫 （requests模块，scrapy模块）

### 按照难度爬虫分类
1. 接口爬虫 （抓取破解）
2. selenium自动化爬虫
    * 启动hub集群（需要其他参数自行看）
    > java -jar selenium-server-standalone-3.8.1.jar -role hub -browserTimeout 60
    
    * 启动node节点
    > 1. node 是firfox。注意webdriver.gecko.driver路径
    java -jar selenium-server-standalone-3.8.1.jar -role node  -hub http://192.168.176.1:4444/grid/register  -browser  "browserName=firefox,webdriver.gecko.driver=/usr/local/bin/geckodriver"
    
    > 2. node 是chrome。注意Dwebdriver.chrome.driver路径
    java  -Dwebdriver.chrome.driver=/Users/yuanlang/work/javascript/chromedriver -jar selenium-server-standalone-3.8.1.jar -role node  -hub http://192.168.176.1:4444/grid/register  -browser  browserName=chrome
    
    > 3. node 是IE。注意Dwebdriver.ie.driver路径
    java  -Dwebdriver.ie.driver=D:/IEDrvierServer.ext -jar selenium-server-standalone-3.8.1.jar -role node  -hub http://192.168.176.1:4444/grid/register  -browser  browserName=ie

