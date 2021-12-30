from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_job
from umeo_site2022.models import Stock
import random 
#https://www.pythonf.cn/read/149094
#django_apschedulerの使い方

scheduler = BackgroundScheduler()


@register_job(scheduler, 'interval', days=1)
def task():
    stock = Stock()
    stock_before = Stock.objects.all().order_by('-created_at')[0]
    rand = random.randint(-2000, 2000)
    if random.randint(1, 100) <= 10:
        rand *= 10
    stock.value = stock_before.value + rand
    if stock.value < 1000:
        stock.value = 1000 + random.randint(-500, 500)
    if stock.value > 100000:
        stock.value = 100000 + random.randint(-1000, 1000)
    stock.save()


try:
    scheduler.start()
except Exception as e:
    print(e)
    scheduler.shutdown()
