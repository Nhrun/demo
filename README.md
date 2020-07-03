# demo
demo collections

# 项目根目录下执行：启动Worker命令
celery -A celery_app worker --loglevel=info

# 项目根目录下执行：启动beat命令
celery beat -A celery_app
