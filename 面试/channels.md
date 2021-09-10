### 心跳检测机制
```
前端周期性的向后端发送一个固定格式的heartbeat_keyword，
后端收到消息后回复一个固定格式的消息，如果长时间没收到，则认为当前连接失效，将其断开。

```
### channels介绍
```
WebSockets:一种提供全双工通信的协议——一个持久的，允许任何时间发送数据的客户端和服务器之间的连接。

Channels允许Django以非常类似于传统HTTP的方式支持WebSockets。
Channels基本上就是任务队列：消息被生产商推到通道，然后传递给监听通道的消费者之一(通道设计时使用Redis作为其首选通道层)。

https://www.oschina.net/translate/in_deep_with_django_channels_the_future_of_real_time_apps_in_django
```
### channels流程
```
1.安装Channels后，允许Django以“通道模式”运行来完成请求/响应的循环。
2.定义一个通道层(Redis)  CHANNEL_LAYERS配置redis连接url
3.在routing.py中定义通道路由  path(r'wx/ws/pair/', consumers.PairConsumer)
    每个通道连接到对应的处理函数。按照惯例会将这些函数放到一个consumers.py文件里。
4.运行（基于新兴标准ASGI（异步服务器网关接口）） 


# Channels (websocket)
ASGI_APPLICATION = 'chatroom.routing.application'
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": ["redis://:lemuel@127.0.0.1:9000/11"],
        },
    },
}
```