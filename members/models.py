from django.db import models

# Create your models here.
class Members(models.Model):
    member_image=models.FileField(upload_to="members/",max_length=250,null=True,default=None)
    member_name=models.CharField(max_length=50)
    member_linkedin=models.CharField(max_length=100)
    member_git=models.CharField(max_length=100)