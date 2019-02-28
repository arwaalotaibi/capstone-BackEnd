from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta, tzinfo
from django.utils.timezone import utc

# TYPE_CHOICES = (
#    ('---','__'),
#    ('c1','C1'),
#    ('c2','C2'),
#    ('c3','C3'),
#    ('c4','C4'),
#    )

class Category(models.Model):
  name = models.CharField(max_length=120)
  backgroundImage = models.ImageField(null=True, blank=True)

  def __str__(self):
       return self.name

class Profile(models.Model):
   username =  models.CharField(max_length=50)
   first_name = models.CharField(max_length=50)
   last_name = models.CharField(max_length=50)
   dategenerated = models.DateField(auto_now_add=True)
   image = models.ImageField(default="pro.png",blank=True, null=True)


class Question(models.Model):
   # user = models.ForeignKey(User,on_delete=models.CASCADE)
   question = models.TextField()
   date = models.DateField(auto_now_add=True)
   time = models.TimeField(auto_now_add=True)
   date2 = models.DateTimeField(auto_now_add=True)
   # _type = models.CharField(max_length=33,choices=TYPE_CHOICES,default='---')

class NextQuestion(models.Model):
   question = models.TextField()
   status = models.BooleanField(default=False)
   
class Comment(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.CharField(max_length=240)
    dategenerated = models.DateField(auto_now_add=True)
    dategenerated2 = models.DateTimeField(auto_now_add=True)
    datenow= models.DateField(default=datetime.now)
    time = models.TimeField(auto_now_add=True)
    like = models.BooleanField(default=False)

    

class Vote(models.Model):
    comment = models.ForeignKey(Comment,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    # like = models.BooleanField(default=False)



