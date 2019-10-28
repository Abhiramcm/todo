from django.db import models
from django.contrib.auth.models import User

class TodoItem(models.Model):
    user = models.ForeignKey(User,default='',on_delete=models.CASCADE)
    contents = models.TextField(max_length=40)
    complete = models.BooleanField(default=False)



    def __str__(self):
        return self.contents,self.user
