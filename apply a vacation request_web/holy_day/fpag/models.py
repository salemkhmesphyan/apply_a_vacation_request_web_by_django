from django.db import models
import datetime
class Reqi_holy(models.Model):
	name_sir=models.CharField(max_length=50)
	typ_holy=models.CharField(max_length=20)
	reson=models.CharField(max_length=50)
	num_day=models.CharField(max_length=10)
	date_start=models.CharField(max_length=15)
	time1=models.DateTimeField(default=datetime.datetime.now)
	address=models.CharField(max_length=50)
	full_name=models.CharField(max_length=50)
	order=models.CharField(max_length=50)
	signing=models.CharField(max_length=50)
	agree=models.CharField(max_length=1,default="0")
	see=models.CharField(max_length=5,default="جديد")
	def __str__(self):
		return self.typ_holy
	class Meta:
		verbose_name="جدول المعلمين"
