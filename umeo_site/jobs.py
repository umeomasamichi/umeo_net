from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_job
from umeo_site.models import Stock
import random 
#https://www.pythonf.cn/read/149094
#django_apschedulerの使い方

scheduler = BackgroundScheduler()


@register_job(scheduler, 'interval', minutes=1)
def task():
    stock = Stock()
    stock_before = Stock.objects.all().order_by('-created_at')[0]
    stock.value = stock_before.value + random.randint(-200, 200)
    if stock.value < 1000:
        stock.value = 1000 + random.randint(-200, 200)
    stock.save()


try:
    scheduler.start()
except Exception as e:
    print(e)
    scheduler.shutdown()
