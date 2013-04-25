from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.utils.regex_helper import Choice
from django.contrib.auth.forms import UserCreationForm

class Judge(models.Model):
    judgeID= models.ForeignKey(User)
    fname = models.CharField(max_length=15,null=False)
    minit = models.CharField(max_length=1)
    lname = models.CharField(max_length=15,null=False)
    ssn = models.PositiveIntegerField(max_length=9)
    bdate = models.DateField()
    streetAddr1 = models.CharField(max_length=20)
    streetAddr2 = models.CharField(max_length=20)
    city = models.CharField(max_length=15)
    state = models.CharField(max_length=20)
    zip = models.PositiveIntegerField(max_length=5)
    gender = models.CharField(max_length=1)
    yearsOfExperience = models.PositiveIntegerField()
    skills = models.CharField(max_length=50)

class Competitor(models.Model):
    compID= models.ForeignKey(User)
    fname = models.CharField(max_length=15,null=False)
    minit = models.CharField(max_length=1)
    lname = models.CharField(max_length=15,null=False)
    ssn = models.PositiveIntegerField(max_length=9)
    bdate = models.DateField()
    streetAddr1 = models.CharField(max_length=20)
    streetAddr2 = models.CharField(max_length=20)
    city = models.CharField(max_length=15)
    state = models.CharField(max_length=20)
    zip = models.PositiveIntegerField(max_length=5)
    gender = models.CharField(max_length=1)
    educationLevel = models.CharField(max_length=20)
    
class Questions(models.Model):
    question =models.CharField(max_length=400,null=False)
    duration=models.PositiveIntegerField(default=0,blank=True,null=True)
    maxscore=models.PositiveIntegerField(default=0,blank=True,null=True)
    def __unicode__(self):
       return self.question

class Contests(models.Model):
    contestName  = models.CharField(max_length=50)
    choiceType={
                ('ol','online'),
                ('of','offline')
                }
    contestType= models.CharField(max_length=10,choices=choiceType)
    startTime  = models.DateTimeField()
    endTime = models.DateTimeField()
        
class ContestQuestion(models.Model):
    contestId = models.ForeignKey(Contests)
    questionId =models.ForeignKey(Questions)

class ContestParticipation(models.Model):
    contestId = models.ForeignKey(Contests)
    userId = models.ForeignKey(User)
    judgeId = models.ForeignKey(Judge)
    score = models.PositiveIntegerField(default=0,blank=True,null=True) 
    status = models.CharField(max_length=10)

class ContestFeedback(models.Model):
    contestId = models.ForeignKey(Contests)
    userId = models.ForeignKey(User)
    judgeId = models.ForeignKey(Judge)
    feedback = models.CharField(max_length=40)

class News(models.Model):
    content = models.CharField(max_length=300)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    adminId = models.ForeignKey(User)
    

class UserRegistrationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = {'username','password1','password2','first_name','last_name','email'}
        
    def save(self,commit=True):
        user = super(UserRegistrationForm,self).save(commit=False)
        print "inside save() method"
        #user.email = self.cleaned_data("email")
        if commit:
            print "inside commit statement"
            user.save()
        return user
