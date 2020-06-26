from django.db import models
from django.utils import timezone
import datetime

class A(models.Model):
    name = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    start = models.DateTimeField('since')
    def __str__(self):
        return self.name
    def was(self):
        return self.start >=timezone.now() - datetime.timedelta(days=1)

class B(models.Model):
    co = models.ForeignKey(A, on_delete=models.CASCADE)
    st = models.CharField(max_length=300)
    cd = models.BooleanField(default=False)
    def __str__(self):
        return str(self.st)




# Create your models here.
