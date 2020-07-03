from datetime import timedelta
from celery.schedules import crontab

BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/1'

CELERY_TIMEZONE = 'Asia/Shanghai'

# 指定导入的任务模块
CELERY_IMPORTS = (
    'celery_app.task1',
    'celery_app.task2'
)

# 定时任务
CELERYBEAT_SCHEDULE = {
    'add-every-30-seconds':{
        'task':'celery_app.task1.add',
        'schedule': timedelta(seconds=30),
        'args': (5, 8)
    },
    'multiply-at-some-time':{
        'task':'celery_app.task2.multiply',
        'schedule': crontab(hour=15,minute=15),
        'args': (3, 7)
    }
}