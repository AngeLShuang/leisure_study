```
结果怎么存入redis

如果在装饰器上设置参数ignore_result=False,装饰器内部会将执行结果存入settings里配置的CELERY_RESULT_BACKEND地址中

如果不关心任务的结果，确保设置ignore_result，因为存储结果会浪费时间和资源。

默认情况下，在配置结果后端时，任务不会忽略结果（ignore_result=False）。
```