from celery_app import task1
from celery_app import task2

task1.add.apply_async(args=[3, 9])
print("[INFO] add")
task2.multiply.apply_async(args=[34, 10])
print("[INFO] multiply")

print("Celery Done!")