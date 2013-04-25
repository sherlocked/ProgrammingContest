'''
Created on Dec 3, 2012

@author: Jay
'''
from django.forms import ModelForm,forms
from Sherlock.ProgramContests.models import *
from django.contrib.auth.forms import UserCreationForm


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

class JudgeForm(ModelForm):
    class Meta:
        model = Judge

class CompetitorForm(ModelForm):
    class Meta:
        model = Competitor
        

class ContestsForm(ModelForm):
    class Meta:
        model = Contests         

class QuestionsForm(ModelForm):
    class Meta:
        model = Questions

class ContestQuestionForm(ModelForm):
    class Meta:
        model = ContestQuestion

class ContestFeedbackForm(ModelForm):
    class Meta:
        model = ContestFeedback
class ContestParticipationForm(ModelForm):
    class Meta:
        model = ContestParticipation
        
class NewsForm(ModelForm):
    class Meta:
        model = News
class DocumentForm(ContestParticipationForm):
    fileField = forms.FileField(label="FileNo")
    
    

