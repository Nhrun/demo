from celery import Celery

# 创建Celery实例
app = Celery('Demo')

# 通过Celery实例加载配置模块
app.config_from_object('celery_app.celeryconfig')