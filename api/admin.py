from django.contrib import admin
from .models import Question,Comment,Vote ,Category ,Profile ,NextQuestion
# Register your models here.
admin.site.register(Question)
admin.site.register(Comment)
admin.site.register(Vote)
admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(NextQuestion)