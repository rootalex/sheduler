from apscheduler.schedulers.blocking import BlockingScheduler
import urllib.request
import datetime

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=10)
def timed_job():
    # print('This job is run every three minutes.')
    webUrl = urllib.request.urlopen('https://etcet-test.herokuapp.com/done_to_todo')
    # print("result code: " + str(webUrl.getcode()))
    print(webUrl.read() , datetime.datetime.now())


'''
@sched.scheduled_job('cron', day_of_week='mon-fri', hour=19, minute=37)
def scheduled_job():
    print('This job is run every weekday at 5pm.')
'''
sched.start()
