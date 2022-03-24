from django.db import models


# Create your models here.
class Task(models.Model):
    id = models.AutoField(primary_key=True, unique=True, verbose_name='ID')
    number = models.CharField(max_length=20, blank=True, null=True, verbose_name='编号')
    class Meta:
        verbose_name = "任务"
        verbose_name_plural = "任务"