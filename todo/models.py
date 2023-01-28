from django.db import models
from django.conf import settings
from django.utils import timezone 

# Create your models here.
class Todo(models.Model):
    task= models.CharField(max_length=255)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
    created_on= models.DateTimeField(default=timezone.now)
    accomplished_on=models.DateTimeField(blank=True, null=True)
    accomplished = models.BooleanField(default=False)
    
    def accomplished_list(self):
        self.accomplished_on = timezone.now()
        self.accomplished = True
        self.save()
    

    def __str__(self):
        return self.task