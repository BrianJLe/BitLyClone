from django.db import models
 
# Create your models here.
class Urls(models.Model):
	# Storage for shorten urls
    short_id = models.SlugField(max_length=6,primary_key=True)
    # Storage for urls
    httpurl = models.URLField(max_length=200)
    pub_date = models.DateTimeField(auto_now=True)
    # Visit count
    count = models.IntegerField(default=0)
 
    def __str__(self):
        return self.httpurl