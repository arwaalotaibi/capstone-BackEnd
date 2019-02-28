from django_cron import CronJobBase, Schedule
from .models import Question ,NextQuestion

class MyCronJob(CronJobBase):
    # ALLOW_PARALLEL_RUNS = True
    #120 every 2 hours
    # RUN_EVERY_MINS = 1
    # schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    RUN_AT_TIMES = ['18:33']
    schedule = Schedule(run_at_times=RUN_AT_TIMES)
    code = 'api.cron.MyCronJob' # a unique code
    ALLOW_PARALLEL_RUNS = True 

    def do(self):
       print("cron")
       print(8888)
       m = NextQuestion.objects.filter(status=False).first()
       T = m.question 
       print(m.id)
       print(T)
       NextQuestion.objects.filter(id=m.id).update(status=True)
       Question.objects.create(question=T)
       

# class MyCronJob(CronJobBase):
#     RUN_EVERY_MINS = 120 # every 2 hours

#     schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
#     code = 'api.MyCronJob'    # a unique code

#     def do(self):
#         print("ugygy")    # do your thing here