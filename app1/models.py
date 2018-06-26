from django.db import models
from datetime import datetime

# Create your models here.
class Posts(models.Model):
  title = models.CharField(max_length=200)
  body = models.TextField()
  created_at = models.DateTimeField(default=datetime.now, blank=True)
  def __str__(self):
    return self.title
  class Meta:
    verbose_name_plural = "Posts"

class Incidents(models.Model):
	title = models.CharField(max_length=200)
	organisation = models.CharField(max_length=230)
	description = models.TextField()
	created_at = models.DateTimeField(default=datetime.now, blank=True)
	logs = models.FileField(upload_to='logs/%Y/%m/%d/')
	validation = models.BooleanField(default=True)

	class Meta:
		verbose_name_plural= "Incidents"
	def __str__(self):
		return self.title
   