'''
Created on Nov 28, 2012

@author: Amriga Maaplai
'''
from django.contrib import admin
from Sherlock.ProgramContests.models import *

 
admin.site.register(Judge)
admin.site.register(Competitor)
admin.site.register(Questions)
admin.site.register(Contests)
admin.site.register(ContestQuestion)
admin.site.register(ContestParticipation)
admin.site.register(GroupTable)
admin.site.register(GroupMember)
admin.site.register(ContestFeedback)
admin.site.register(News)