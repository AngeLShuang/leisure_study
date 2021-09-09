## HTTP相关

### HTTP与HTTPS区别

```
HTTP明文传输，数据都是未加密的，安全性较差，HTTPS（SSL+HTTP）数据传输过程是加密的，安全性较好。
使用HTTPS协议需要到CA（Certificate Authority，数字证书认证机构）申请证书，一般免费证书较少，因而需要一定费用。证书颁发机构如：Symantec、Comodo、GoDaddy和GlobalSign等。
HTTP页面响应速度比HTTPS快，主要是因为HTTP使用TCP三次握手建立连接，客户端和服务器需要交换3个包，而HTTPS除了TCP的三个包，还要加上ssl握手需要的9个包，所以一共是12个包。
HTTP和HTTPS使用的是完全不同的连接方式，用的端口也不一样，前者是80，后者是443。
HTTPS其实就是建构在SSL/TLS之上的HTTP协议，所以，要比较HTTPS比HTTP要更耗费服务器资源。
```