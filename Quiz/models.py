from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class QuesModel(models.Model):
    writer = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    question = models.CharField(max_length=200,null=True)
    question2 = models.CharField(max_length=200,null=True)
    question3 = models.CharField(max_length=200,null=True)
    question4 = models.CharField(max_length=200,null=True)
    question5 = models.CharField(max_length=200,null=True)
    question6 = models.CharField(max_length=200,null=True)
    question7 = models.CharField(max_length=200,null=True)
    # question8 = models.CharField(max_length=200,null=True)

    

    
    
    ans = models.CharField(max_length=200,null=True)
    ans2 = models.CharField(max_length=200,null=True)
    ans3 = models.CharField(max_length=200,null=True)
    ans4 = models.CharField(max_length=200,null=True)
    ans5 = models.CharField(max_length=200,null=True)
    ans6 = models.CharField(max_length=200,null=True)
    ans7 = models.CharField(max_length=200,null=True)
    # ans8 = models.CharField(max_length=200,null=True)
    
class Visitor(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=200,null=True)
    gender = models.CharField(max_length=200,null=True)
    date = models.CharField(max_length=200,null=True)
    score = models.PositiveIntegerField(default=0, null=True)
    

