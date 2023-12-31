from django.db import models

from django.contrib.auth.models import User #auth
import datetime
import os

# Create your models here.

#images
def get_file_path(request, filename):
    orginal_filename = filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (nowTime, orginal_filename)
    return os.path.join('uploads/', filename)

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)#join
    full_name = models.CharField(max_length=150, null=False)
    phone = models.CharField(max_length=50, null=False)
    bio = models.TextField(null=False)
    image = models.ImageField( upload_to=get_file_path, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   
    def __str__(self):
        return self.user.username
    
class SavePredict(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)#join
    symptoms_input = models.TextField(null=False)
    symptoms_result = models.CharField(max_length=150, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   
    def __str__(self):
        return self.user.username