from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.utils.regex_helper import Choice

class Judge(models.Model):
    judgeID= models.ForeignKey(User)
    judgeFname = models.CharField(max_length=20)
    minit = models.CharField(max_length=1,blank=True)
    judgeLname = models.CharField(max_length=30)
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
    security1= {
    ('1','What was your childhood nickname?'),
    ('2','What is the name of the company of your first job?'),
    ('3','What is the name of your favorite childhood friend?'),
    ('4','What street did you live on in third grade?')
    }
    secquestion1=models.CharField(max_length=50,choices=security1)
    answer1 = models.CharField(max_length=15,null=False)
    security2={
    ('5','What is the middle name of your oldest child?'),
    ('6','What is your oldest siblings middle name?'),
    ('7','What school did you attend for sixth grade?'),
    ('8','What was your childhood phone number including area code?')         
    }
    secquestion2=models.CharField(max_length=50,choices=security2)
    answer2 = models.CharField(max_length=15,null=False)
    security3={
    ('9','What time of the day were you born?'),
    ('10','What was your dream job as a child?'),
    ('11','What is your maternal grandmothers name?'),
    ('12','In what city or town was your first job?')
     }    
    
    secquestion3=models.CharField(max_length=50,choices=security3)
    answer3 = models.CharField(max_length=15,null=False)
    def __unicode__(self):
        field = self.judgeLname+" , "+self.judgeFname
        return field
        
    
class Competitor(models.Model):
    compID= models.ForeignKey(User)
    compFname = models.CharField(max_length=30)
    minit = models.CharField(max_length=1,blank=True)
    compLname =models.CharField(max_length=30)
    ssn = models.PositiveIntegerField(max_length=9)
    bdate = models.DateField()
    streetAddr1 = models.CharField(max_length=20)
    streetAddr2 = models.CharField(max_length=20)
    city = models.CharField(max_length=15)
    state = models.CharField(max_length=20)
    zip = models.PositiveIntegerField(max_length=5)
    gender = models.CharField(max_length=1)
    educationLevel = models.CharField(max_length=20)
    security1= {
    ('1','What was your childhood nickname?'),
    ('2','What is the name of the company of your first job?'),
    ('3','What is the name of your favorite childhood friend?'),
    ('4','What street did you live on in third grade?')
    }
    secquestion1=models.CharField(max_length=50,choices=security1)
    answer1 = models.CharField(max_length=15,null=False)
    security2={
    ('5','What is the middle name of your oldest child?'),
    ('6','What is your oldest siblings middle name?'),
    ('7','What school did you attend for sixth grade?'),
    ('8','What was your childhood phone number including area code?')         
    }
    secquestion2=models.CharField(max_length=50,choices=security2)
    answer2 = models.CharField(max_length=15,null=False)
    security3={
    ('9','What time of the day were you born?'),
    ('10','What was your dream job as a child?'),
    ('11','What is your maternal grandmothers name?'),
    ('12','In what city or town was your first job?')
     }    
    
    secquestion3=models.CharField(max_length=50,choices=security3)
    answer3 = models.CharField(max_length=15,null=False)
    
    def __unicode__(self):
        field = self.compLname+" , "+self.compFname
        return field
    
class Questions(models.Model):
    question =models.CharField(max_length=400,null=False)
    #duration=models.PositiveIntegerField(default=0,blank=True,null=True)
    #maxscore=models.PositiveIntegerField(default=0,blank=True,null=True)
    def __unicode__(self):
        field = self.question
        return field
    

class GroupTable(models.Model):
    groupTableId = models.ForeignKey(User)
    groupName = models.CharField(max_length=40)
    contactPerson = models.ForeignKey(Competitor)
class GroupMember(models.Model):
    groupTableid = models.ForeignKey(GroupTable)
    memberId = models.ForeignKey(Competitor)
class Contests(models.Model):
    contestName  = models.CharField(primary_key=True,max_length=50)
    choiceType={
                ('ol','online'),
                ('of','offline')
                }
    contestType= models.CharField(max_length=10,choices=choiceType)
    startTime  = models.DateTimeField()
    endTime = models.DateTimeField()
    rules=models.CharField(max_length=500)
    def __unicode__(self):
        field = self.contestName
        return field
        
    
class ContestQuestion(models.Model):
    contestId = models.ForeignKey(Contests)
    questionId = models.ForeignKey(Questions)
    maxscore=models.PositiveIntegerField(default=0,blank=True,null=True)
    
#    def __unicode__(self):
#        contestVar = Contests.objects.get(pk=self.contestId)
#        ContDisp = contestVar.contestName
##        questionVar = Questions.objects.get(pk=self.questionId)
##        QuestDisp = questionVar.question
##        print QuestDisp
#        print self.questionId 
#        QuestionVar = Questions.objects.get(question=self.questionId)
#        print QuestionVar.id
#        field = ContDisp + " - " +QuestionVar.question#" , " +self.questionId
#        #field = self.contestId + ","+self.questionId
#        return field
     
class ContestParticipation(models.Model):
    contestQuestionId = models.ForeignKey(ContestQuestion)
    compId = models.ForeignKey(Competitor)
    judgeId = models.ForeignKey(Judge)
    score = models.PositiveIntegerField(default=0,blank=True,null=True) 
    status = models.CharField(max_length=10,null=True)
    langType={
                ('j','Java'),
                ('c','C'),
                ('cpp','C++')
                }
    lang_used= models.CharField(max_length=10,choices=langType)
    filepath = models.CharField(max_length=200,null=True)
    
#    def __unicode__(self):
#       
#       field = self.contestQuestionId+" - "+self.compId+" - " +self.judgeId
#       print field
#       return self.compId

class ContestFeedback(models.Model):
    contestId = models.ForeignKey(Contests)
    compId = models.ForeignKey(Competitor)
    judgeId = models.ForeignKey(Judge)
    feedback = models.CharField(max_length=100)

class News(models.Model):
    content = models.CharField(max_length=300)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()

#code from madhu for integration


class Filetrial(models.Model):
    userid = models.CharField(max_length=20)
#    def changeFilePath(self,instance):
#        filepath = generate_folder_name(self.userid)
#        print filepath
#        return filepath
    filecontent=models.FileField(upload_to="User")
    