# scalpels项目学习(代码业务流程)
## 一 启动rpcserver
    这个服务器运行在每个节点上，它接受client的请求，然后负责管理tracer

## 1 通过命令直接运行agent.py
## 2 在agent.py
    调用server.start

    调用server.wait

#### 2.1 rpc server
    最后在来理解来开，这里rcpserver主要是注册好了一些方法 以及这些方法的定义
server的声明
    oslo_messaging.get_rpc_server(transport, target, endpoints,executor='blocking', serializer=None):
这里讲述了oslo.messaging的用法：
https://wiki.openstack.org/wiki/Oslo/Messaging#oslo.messaging.rpc

在这里只关注rpc的部分：
##### 2.1.1 一些概念
- Exchange：包含了每个项目的topics范围的容器
- Topic： RPC接口的id
- NameSpace：一个topic可以有多个method，每个method都在一个namesapce下
- Method：一个方法有一个方法名和多个命名参数（keyword）
- API version：
- Transport：一个潜在的消息系统，在server和client之间传递消息
##### 2.1.2 endpoints
包含一个target以及一些方法，Methods are invoked on targets.
    target的属性：exchange topic server（可选） fanout namesapce（可选） API version（可选）


## 二 创建服务DB
    初始化DB，建立各种表
    命令为 sca-manage db-create -f
它会调用db_api
db_api会调用真正实现的dbapi--achemy
最后会通过models中定义的模型来创建DB
各个DB表和表中的内容如下：

Task表<br>
id,uuid,results,pids

result表<br>
    id,uuid,data,unit,name,rtype

setup表<br>
    id,config

tracer表<br>
    id,name,template,is_runing,results,pid

## 三 注册tracer
    sca-manage setup -t name=mysql -t tpl="bash %(tracer_path)s/mysql-live.sh"
实际上就是把信息在数据库中进行配置
   配置信息包括 tracer的名字，tracer的运行模式，tracer的参数
## 四 运行tracer
sca start -a rpc -a rabbit -a traffic
### 4.1 client 调用start
从配置信息和文件中加载加载agents，将所有agent添加到一个列表中，然后调用本地的api
### 4.2本地api调用rpcapi
### 4.2通过向server发送远程调用请求
```
def start_tracers(self, ctxt={}, tracers=None):
        self._client.cast(ctxt, "start_tracers", tracers=tracers)
```
### 4.3rpc服务起收到rpc请求，调用start_tracers方法
- 从tracer_list中获取tracer的运行情况
- 创建task
- 运行tracer
- 更新task信息

### 4.4运行tracer
以 sca-tracer task_uuid agname 的命令启动tracer
它会启动一个子进程，运行cmd.tracer.main程序

### 4.5 cmd.tracer.main
真正启动tracer的是这个组件，他做了下面这些事情
- 注册信号处理函数，一旦tracer.py被干掉它会做下面这些事：
    - 向tracer发送SIGINT 停止tracer的运行
    - 将out中信息写到数据库中
    - 更新tracer表的pid项和runing项
- 检查是否存在这个tracer(从数据库中)
- 通过子进程的方式运行tracer
while True：
  - 不断的读入tracer产生的数据

## 五 stop
sca stop xxx

可以停止一个tracer，也可以停止一个task

（通过uuid）停止一个task，向task的pids发送信号-2 <br>
停止一个tracer,向trace.main发送信号-2


## 六 report  result
report 报告一个
result 报告去全部
