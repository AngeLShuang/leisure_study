### celery工作流程
```
1、application(task producer)"任务的生产者"，我们通过代码层面，产生任务然后发送给broker(task queue)
2、celery beat(task scheduler)"任务调度器"，常见为生成定时任务
3、broker(task queue)"任务队列",我们需要将任务送往任务队列去，官网强烈推荐的broker有：redis和rabbitmq
4、worker(taks consumer)"任务消费者"，在任务送往broker后，worker从中进行操作，完成任务后生成result
5、result 完成任务后产生的结果
```

### 结果怎么存入redis
```
如果在装饰器上设置参数ignore_result=False,装饰器内部会将执行结果存入settings里配置的CELERY_RESULT_BACKEND地址中
如果不关心任务的结果，确保设置ignore_result，因为存储结果会浪费时间和资源。
默认情况下，在配置结果后端时，任务不会忽略结果（ignore_result=False）。
```