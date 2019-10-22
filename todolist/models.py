from django.db import models

class TodoItem(models.Model):
    contents = models.TextField()
    complete = models.BooleanField(default=False)


    def __str__(self):
        return self.contents
