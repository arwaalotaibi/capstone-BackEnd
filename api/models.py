from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta, tzinfo
from django.utils.timezone import utc

TYPE_CHOICES = (
   ('---','__'),
   ('c1','C1'),
   ('c2','C2'),
   ('c3','C3'),
   ('c4','C4'),
   )

class Question(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE)
   question = models.TextField()
   date = models.DateField(auto_now_add=True)
   time = models.TimeField(auto_now_add=True)
   date2 = models.DateTimeField(auto_now_add=True)
   _type = models.CharField(max_length=33,choices=TYPE_CHOICES,default='---')

   
class Comment(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.CharField(max_length=240)
    dategenerated = models.DateField(auto_now_add=True)
    dategenerated2 = models.DateTimeField(auto_now_add=True)
    datenow= models.DateField(default=datetime.now)
    time = models.TimeField(auto_now_add=True)
    n_vote = models.IntegerField(default=0)

    

class Vote(models.Model):
    comment = models.ForeignKey(Comment,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    # like = models.BooleanField(default=False)

class Category(models.Model):
 name = models.CharField(max_length=120)
 backgroundImage = models.ImageField(null=True, blank=True)

 def __str__(self):
      return self.name



