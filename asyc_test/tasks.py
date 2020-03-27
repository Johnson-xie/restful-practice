from celery import Celery

# app = Celery('test_tasks', 'redis://localhost')
app = Celery('tasks', broker='redis://localhost//')

@app.task(name='my_reverse')
def my_reverse(s):
    return s[::-1]


my_reverse.delay('hello world')
# app模块需要单独放一个包里
