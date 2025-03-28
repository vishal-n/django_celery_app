import time
from celery import shared_task


@shared_task
def square_number(x):
    time.sleep(5)
    return x * x 
