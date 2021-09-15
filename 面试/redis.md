## redis

```
默认支持16个数据库,在配置文件的databases可以进行修改 
客户端与Redis建立连接后会自动选择0号数据库，可以使用SELECT命令更换数据库
```

### 数据类型使用场景

```
字符串:计数
hash:每人每天的提现次数
列表:消息队列
无序集合:判断用户是否在列表中
有序集合:排行榜
```

### 数据类型的实现

```
字符串:常规key_value
hash:hash对应内部value实际就是一个HashMap。当hash的成员较少时，Redis为了节省内存会采用类似一维数组的方式来紧凑存储，当成员增大时会转为HashMap。
列表:列表的实现是一个双向链表，每个元素都是String，可以通过push和pop操作从列表的头部或尾部添加或删除元素，既可以作为栈，也可以作为队列。
无序列表：set的内部是value永远为null的HashMap，通过计算hash的方式来快速排重
有序列表：内部使用HashMap和跳跃表来保证数据的存储和有序
         HashMap里放的是成员到score的映射，跳跃表里放的是所有成员，排序依据是HashMap里存的score
         使用跳跃表的结构可以获得比较高的查找效率
```

### Redis高可用

```
1.数据持久化
    RDB：将Reids在内存中的数据库记录定时dump到磁盘上的RDB持久化
         占用空间小，有更快的重启恢复能力，但有数据丢失的风险
         操作：save 900 1：表示900 秒内如果至少有 1 个 key 的值变化，则保存
    AOF：将Reids的操作日志以追加的方式写入文件
         存储频率更高，丢失数据的风险低，不是二进制存储，可读性高，占用空间大，恢复速度较慢
         操作：appendonly yes
2.主从复制
    可以实现数据读写分离，把写操作分发到主节点，读分到从节点，提高了redis的整体运行速度。
    宕机后，可以迅速把从节点升为主节点，降低了数据丢失的风险，数据是完整拷贝在多台服务器上的。
    主节点宕机后，必须人工介入手动恢复
    开启主从  从节点slaveof 127.0.0.1 6379 # 开启主从复制   slaveof no one # 断开复制
3.哨兵机制
    监视主从服务器
    哨兵以1/s的频率向主和从发送ping，如果回复超过配置的最大下线时间，会被标记为主观下线，那么所有的哨兵节点会以1/s进行确认，标为客观下线，哨兵投票选出新的主节点并切换。
4.Redis集群：Redis3.0推出
    有多个主节点，同时每个主节点有多个从节点，将数据分布在不同的主服务器上，以此来降低系统对单主节点的依赖，提高Redis服务的读写性能
```

### Redis持久化

```
由于Redis的数据都存放在内存中，如果没有配置持久化，redis重启后数据就全丢失了，于是需要开启redis的持久化功 能，将数据保存到磁盘上，当redis重启后，可以从磁盘中恢复数据。 
redis提供两种方式进行持久化，一种是RDB持久化,另外一种是AOF持久化。

一、RDB持久化
1. 原理
    RDB持久化是指在指定的时间间隔内通过save命令将内存中的数据生成RDB快照文件
    RDB文件是经过压缩的二进制文件，这个文件被保存在硬盘中，redis可以通过这个文件还原数据库当时的状态。
2. 过程
    Redis调用fork()，产生一个子进程。子进程把数据写到一个临时的RDB文件。当子进程写完新的RDB文件后，把旧的RDB文件替换掉
3. 优点
    RDB文件是一个很简洁的单文件，它保存了某个时间点的Redis数据，很适合用于做备份。你可以设定一个时间点对RDB文件进行归档，这样就能在需要的时候很轻易的把数据恢复到不同的版本。比起AOF，在数据量比较大的情况下，RDB的启动速度更快。
4. 缺点
    RDB容易造成数据的丢失。假设每5分钟保存一次快照，如果Redis因为某些原因不能正常工作，那么从上次产生快照到Redis出现问题这段时间的数据就会丢失了。RDB使用fork()产生子进程进行数据的持久化，如果数据比较大的话可能就会花费点时间，造成Redis停止服务几毫秒。如果数据量很大且CPU性能不是很好的时候，停止服务的时间甚至会到1秒。

二、AOF持久化
1. 原理
    AOF持久化以日志的形式记录服务器所处理的每一个写、删除操作，查询操作不会记录，生成AOF文件，重启Redis时，AOF里的命令会被重新执行一次，重建数据。
2. 过程
    Redis调用fork()，产生一个子进程。子进程把新的AOF写到一个临时文件里。主进程持续把新的变动写到内存里的buffer，同时也会把这些新的变动写到旧的AOF里，这样即使重写失败也能保证数据的安全。当子进程完成文件的重写后，主进程会获得一个信号，然后把内存里的buffer追加到子进程生成的那个新AOF里
3. 优点
    比RDB可靠。你可以制定不同的fsync策略：不进行fsync、每秒fsync一次和每次查询进行fsync。默认是每秒fsync一次。这意味着你最多丢失一秒钟的数据
4. 缺点
    在相同的数据集下，AOF文件的大小一般会比RDB文件大。
    
总结：
rdb：基于快照的持久化，速度更快，一般用作备份，主从复制也是依赖于rdb持久化功能 
aof：以追加的方式记录redis操作日志的文件。可以最大程度的保证redis数据安全，类似于mysql的binlog
```

### 主从复制连接建立阶段

```
1. 保存主节点信息:从节点服务器内部维护了两个字段，即masterhost和masterport字段，用于存储主节点的ip和port信息。
    需要注意的是，slaveof是异步命令，从节点完成主节点ip和port的保存后，向发送slaveof命令的客户端直接返回OK，实际的复制操作在这之后才开始进行。
2. 建立socket连接
3. 发送ping命令
4. 身份验证:如果从节点中设置了masterauth选项，则从节点需要向主节点进行身份验证；没有设置该选项，则不需要验证。
5. 发送从节点端口信息:身份验证之后，从节点会向主节点发送其监听的端口号（前述例子中为6380），主节点将该信息保存到该从节点对应的客户端的slave_listening_port字段中
```

### redis sentinel三个定时任务

```
1.每10秒每一个sentienl对master和salve执行info
	发现salve节点
	确定主从关系
2.每2秒每个sentinel通过master节点的channel交换信息
	通过__sentinel__:hello频道交互
3.每一秒每一个sentinel 对其他sentinel和redis执行ping
```

### redis做异步队列

```
一般使用list结构作为队列，rpush生产消息，lpop消费消息。当lpop没有消息的时候，要适当sleep一会再重试。
不用sleep的话：list还有个指令叫blpop，在没有消息的时候，它会阻塞住直到消息到来。
生产一次消费多次：使用pub/sub主题订阅者模式，可以实现1:N的消息队列。
```

### redis分布式锁

```
先拿setnx来争抢锁，抢到之后，再用expire给锁加一个过期时间防止锁忘记了释放。
```

### redis中的删除策略

```
惰性删除：服务器不会主动删除数据，只有当客户端查询某个数据时，服务器判断该数据是否过期，如果过期则删除。
定期删除：服务器执行定时任务删除过期数据，但是考虑到内存和CPU的折中（删除会释放内存，但是频繁的删除操作对CPU不友好），该删除的频率和执行时间都受到了限制。
在主从复制场景下，为了主从节点的数据一致性，从节点不会主动删除数据，而是由主节点控制从节点中过期数据的删除。由于主节点的惰性删除和定期删除策略，都不能保证主节点及时对过期数据执行删除操作，因此，当客户端通过Redis从节点读取数据时，很容易读取到已经过期的数据。
Redis 3.2中，从节点在读取数据时，增加了对数据是否过期的判断：如果该数据已过期，则不返回给客户端；将Redis升级到3.2可以解决数据过期问题。
```

### redis读写分离中的问题

```
1. 延迟与不一致问题
2. 数据过期问题
3. 故障切换问题
4. 主从配置不一致
	maxmemroy不一致:丢失数据
5.尽量规避全量复制
解决办法：将redis的版本升为3.2以上
```

### 数据同步

```
在Redis2.8以前，从节点向主节点发送sync命令请求同步数据，此时的同步方式是全量复制
全量复制：用于初次复制或其他无法进行部分复制的情况，将主节点中的所有数据都发送给从节点，是一个非常重型的操作。
部分复制：用于网络中断等情况后的复制，只将中断期间主节点执行的写命令发送给从节点，与全量复制相比更加高效。需要注意的是，如果网络中断时间过长，导致主节点没有能够完整地保存中断期间执行的写命令，则无法进行部分复制，仍使用全量复制。
```

### 部分复制

```
1. master将数据写入到缓冲区中 write send_buffer repl_back_buffer
2. salve connection to master pysnc {offset} {runid} 携带着本地的偏移量,连接数据库
3. 如果offset在master的缓冲区中,master send partial message
4. 否则进行全量复制
```

### 全量复制

```
Redis通过psync命令进行全量复制的过程如下：
1. 从节点判断无法进行部分复制，向主节点发送全量复制的请求；或从节点发送部分复制的请求，但主节点判断无法进行全量复制
2. 主节点收到全量复制的命令后，执行bgsave，在后台生成RDB文件，并使用一个缓冲区（称为复制缓冲区）记录从现在开始执行的所有写命令
3. 主节点的bgsave执行完成后，将RDB文件发送给从节点；从节点首先清除自己的旧数据，然后载入接收的RDB文件，将数据库状态更新至主节点执行bgsave时的数据库状态
4. 主节点将前述复制缓冲区中的所有写命令发送给从节点，从节点执行这些写命令，将数据库状态更新至主节点的最新状态
5. 如果从节点开启了AOF，则会触发bgrewriteaof的执行，从而保证AOF文件更新至主节点的最新状态
```

### 全量复制开销

```
1. bgsave时间
2. rdb文件网络传输时间
3. 从节点清空数据
4. 从节点加载rdb时间
```

### save命令和bgsave

```
save命令会阻塞redis服务器进程,直到rdb文件创建完毕,服务器阻塞期间,不能处理任何请求
bgsave创建子进程,由子进程负责创建rdb文件,父进程继续处理请求
```

### bgsave执行流程

```
1. Redis父进程首先判断：当前是否在执行save，或bgsave/bgrewriteaof（后面会详细介绍该命令）的子进程，如果在执行则bgsave命令直接返回。bgsave/bgrewriteaof的子进程不能同时执行，主要是基于性能方面的考虑：两个并发的子进程同时执行大量的磁盘写操作，可能引起严重的性能问题。
2. 父进程执行fork操作创建子进程，这个过程中父进程是阻塞的，Redis不能执行来自客户端的任何命令
3. 父进程fork后，bgsave命令返回”Background saving started”信息并不再阻塞父进程，并可以响应其他命令
4. 子进程创建RDB文件，根据父进程内存快照生成临时快照文件，完成后对原有文件进行原子替换
5. 子进程发送信号给父进程表示完成，父进程更新统计信息
```

### redis通用命令

```
keys [pattern] #慎用时间复杂度o(n)
	keys *
	keys he*
	keys he[h-1]*
	keys ph? #代表一位
dbsize: # 算出键值总数
exists key: # 查看key是否存在
	key hh
del key #删除指定key-value
expire key seconds
ttl key # 查看key 剩余的过期时间
persist key # 去掉key的过期时间
ttl key # -1 代表key存在,并且没有过期时间
```

### 字符串操作

```
get 
set 
del 

incr key # key 自增1 ,如果key不存在,自增后get key =1
decr key # key 自减1 ,如果key不存在,自增后 get key =-1
incrby key k # key 自增k,如果key不存在,自增后为k
decrby key k # key 自增k,如果key不存在,自增后为k

set key value # 不管key是否存在,都设置
setnx key value # key 不存在,才设置

mget key1 key2 key3 
mset key1 value1 key2 value2

getset key newvalue # 设置新值,返回旧值
append key value # 将value 追加到就的value后面
strlen key # 返回字符串的长度
```

### hash操作

```
# field不能相同,value 可以相同
hget key field
hset key field value 
hdel key field

hexists key field # 判断hash key 是否有field字段
hlen key # 获取 hash key field的数量

hmget key field1 field2 #获取多个字符串
hmset key field1 value1 field2 value2

hgetall key
hvals key # 返回hash key 对应的所有的field的value
hkeys key # 返回hahs key 对应的所有field

hsetnx key field value 
```

### 列表操作

```
rpush key value1 value2 # 右边插入
lpush key value1 value2 # 左边插入

linsert key before|after value newValue #在指定的key后面或者前面插入新值
rpop key # 从右边弹出一个值
lpop key # 从左边弹出一个值

lrem key count value 
	根据count的值,从列表中删除所有value 相等的值
	count > 0 从左到右,删除最多count个相等的项
	count < 0 从右到左,删除最多count个相等的项
	count = 0 删除所有value相等的项
ltrim key start end #按照所有范围修剪列表
	ltrim listkey 1 4 # 保留中间的内容
lrange key start end(包含end) # 获取指定索引范围内的元素
lindex key index #获取列表指定索引的item
llen # 获取列表长度
lset key index newValue # 设置列表指定索引位值位newValue

blpop key timeout 
lpop 阻塞版本,timeout是阻塞超时时间,timeout=0 表示永远不阻塞
brpop key timeout 

lpush +lpop = stack
lpush + rpop = queue
lpush + ltrim capped collection
lpush + brpop = message queue
```

### 集合操作

```
sadd key element # 向集合中key中添加element(如果存在,则添加失败)
srem key element # 将集合key中的elemetn移除掉
scard # 元素个数
sismember key value # 判断it是否存在集合中
srandmember key count # 从集合中随机取出 count个元素
spop key #从集合中随机弹出一个元素
smembers key #返回所有的元素

sinter #交集
sdiff # 差集
sunion # 并集

sdiff|sinter|sunion +store destkey #保存到destkey中
```

### 有序集合操作

```
zadd key score element #添加元素
zrem key element #删除元素,可以是多个element
zscore key element # 返回元素的分数
zincrby key increScore element # 增加或者减少increScore的分数
zcard key #返回元素的个数
zrank key element #获取排名,从小到大排名
zrem key element #
zrange key start end withscores #带着分数进行打印
zrangebyscore key minScore maxScore #返回升序元素
zcount key minScore maxScore #返回指定分数的个数
```

### Redis的应用Key很大，如何取出特定的key呢？

```
# 通过scan_iter分片取，减少内存压力，增量式迭代获取redis里匹配的的值
scan_iter(match=None, count=None)
# match，匹配指定key count，每次分片最少获取个数
r = redis.Redis(connection_pool=pool)
for key in r.scan_iter(match='PREFIX_*', count=100000):
    print(key)
```

### 如何高效的找到redis中所有以 oldboy开头的key?

```
keys命令：返回与指定模式相匹配的所用的keys。

该命令所支持的匹配模式如下： 
1. ?：用于匹配单个字符。例如，h?llo可以匹配hello、hallo和hxllo等； 
2. *：用于匹配零个或者多个字符。例如，h*llo可以匹配hllo和heeeello等； 
3. []：可以用来指定模式的选择区间。例如h[ae]llo可以匹配hello和hallo，但是不能匹配hillo。同时，可以使 用“/”符号来转义特殊的字符

注意 KEYS的速度非常快，但如果数据太大，内存可能会崩掉，如果需要从一个数据集中查找特定的key，最好还是用Redis的集合结构(set)来代替。
```

### 在项目中遇到redis性能问题？

```
我的项目中暂时没有遇到性能问题，不过我在学习Redis的时候有看到过： 
1. Master最好不要做任何持久化工作，如RDB内存快照和AOF日志文件
   Master调用BGREWRITEAOF重写AOF文件，AOF在重写的时候会占大量的CPU和内存资源，导致服务load过高，出现短暂服务暂停现象。 
2. 如果数据比较重要，某个Slave开启AOF备份数据，策略设置为每秒同步一次
3. 为了主从复制的速度和连接的稳定性，Master和Slave最好在同一个局域网内 
4. 尽量避免在压力很大的主库上增加从库 
5、主从复制不要用图状结构，用单向链表结构更为稳定，即：Master <- Slave1 <- Slave2 <-Slave3… 
   这样的结构方便解决单点故障问题，实现Slave对Master的替换。如果Master挂了，可以立刻启用Slave1做Master，其他不变。
```

### Redis缓存穿透、缓存雪崩和缓存击穿

```
1.缓存穿透 
    缓存穿透，是指查询一个数据库一定不存在的数据。
    正常的使用缓存流程大致是，数据查询先进行缓存查询，如果key不存在或者key已经过期，再对数据库进行查询，并把查询到的对象，放进缓存。如果数据库查询对象为空，则不放进缓存。
    而每次查询都是空，每次又都不会进行缓存。
    假如有恶意攻击，就可以利用这个漏洞，对数据库造成压力，甚至压垮数据库。即便是采用UUID，也是很容易找到一个不存在的KEY，进行攻击。
    
    如果从数据库查询的对象为空，也放入缓存，只是设定的缓存过期时间较短，比如设置为60秒。
2.缓存雪崩 
    缓存雪崩，是指在某一个时间段，缓存集中过期失效。
    产生雪崩的原因之一，比如在写本文的时候，马上就要到双十二零点，很快就会迎来一波抢购，这波商品时间比较集中的放入了缓存，假设缓存一个小时。
    那么到了凌晨一点钟的时候，这批商品的缓存就都过期了。而对这批商品的访问查询，都落到了数据库上，对于数据库而言，就会产生周期性的压力波峰。
    
    一般是采取不同分类商品，缓存不同周期。在同一分类中的商品，加上一个随机因子。这样能尽可能分散缓存过期时间，而且，热门类目的商品缓存时间长一些，冷门类目的商品缓存时间短一些，也能节省缓存服务的资源。
3.缓存击穿 
    缓存击穿，是指一个key非常热点，在不停的扛着大并发，大并发集中对这一个点进行访问，当这个key在失效的瞬间，持续的大并发就穿破缓存，直接请求数据库，就像在一个屏障上凿开了一个洞。
    其实，大多数情况下这种爆款很难对数据库服务器造成压垮性的压力。达到这个级别的公司没有几家的。所以，务实主义的小编对主打商品都是早早的做好了准备，让缓存永不过期。即便某些商品自己发酵成了爆款，也是直接设为永不过期就好了。
```

### redis watch

```
假设我们通过WATCH命令在事务执行之前监控了多个Keys，倘若在WATCH之后有任何Key的值发生了变化，EXEC命令执行的事务都将被放弃，同时返回Null

面试题：你如何控制剩余的数量不会出问题？ 
1.通过redis的watch实现 2.数据库锁

import redis conn = redis.Redis(host='127.0.0.1', port=6379)
val = conn.get('count')
with conn.pipeline(transaction=True) as pipe:
    # 先监视，自己的值没有被修改过 
    conn.watch('count')
    # 事务开始 
    pipe.multi()
    old_count = conn.get('count')
    count = int(old_count)
    print('现在剩余的商品有:%s', count)
    pipe.set('count', count - 1)
    # 执行，把所有命令一次性推送过去 
    pipe.execute()
```

### Redis过期策略

```
volatile-lru：从已设置过期时间的数据集（server.db[i].expires）中挑选最近最少使用的数据淘汰 
volatile-ttl：从已设置过期时间的数据集（server.db[i].expires）中挑选将要过期的数据淘汰 
volatile-random：从已设置过期时间的数据集（server.db[i].expires）中任意选择数据淘汰 
allkeys-lru：从数据集（server.db[i].dict）中挑选最近最少使用的数据淘汰 
allkeys-random：从数据集（server.db[i].dict）中任意选择数据淘汰 
no-enviction（驱逐）：禁止驱逐数据,不删除策略。当达到最大内存限制时,如果需要使用更多内存,则直接返回错误信息。

MySQL里有2000w数据, redis中只存20w的数据,如何保证 redis中都是热点数据?

方案： 限定Redis占用的内存，Redis会根据自身数据淘汰策略，留下热数据到内存。所以，计算一下50W数据大约占用的内存，然后设置一下Redis内存限制即可，并将淘汰策略为volatile-lru或者allkeys-lru。
设置Redis最大占用内存： 打开redis配置文件，设置maxmemory参数，maxmemory是bytes字节类型 设置过期策略： maxmemory-policy volatile-lru
```