from django.conf.urls.defaults import *

urlpatterns = patterns("",
                       (r'^login/','django.contrib.auth.views.login',{'template_name':'login.html'}),
                       (r'^check/','Sherlock.ProgramContests.views.login_fn'),
                       (r'^create/','Sherlock.ProgramContests.views.createUser'),
                       (r'^createNew/','Sherlock.ProgramContests.views.createUserNew'),
                       (r'^logout/','Sherlock.ProgramContests.views.user_logout'),
                       (r'^edit/','Sherlock.ProgramContests.views.editprofile'),
                       (r'^updateUser/','Sherlock.ProgramContests.views.updateUser'),
                       (r'^judge/viewUsers/','Sherlock.ProgramContests.views.judgeViewUsers'),
                       (r'^judge/home/','Sherlock.ProgramContests.views.judgeHome'),
                       url(r'^TakeExam/$', 'Sherlock.ProgramContests.views.TakeExam'),
                       url(r'^Participation/$', 'Sherlock.ProgramContests.views.viewScore'),
                       url(r'^TakeExam/Instructions/$','Sherlock.ProgramContests.views.Inst'),
                       url(r'^TakeExam/Instructions/ShowQuestions/$','Sherlock.ProgramContests.views.showQuest'),
                       url(r'^CurrentExam/$', 'Sherlock.ProgramContests.views.CurrentExam'),
                       url(r'^FileUpload/$', 'Sherlock.ProgramContests.views.fileupload'),
                       url(r'^home/$', 'Sherlock.ProgramContests.views.userHome'),
                       url(r'^judge/updateUserScore/$', 'Sherlock.ProgramContests.views.updateUserScore'),
                       url(r'^judge/updateUserVal/$', 'Sherlock.ProgramContests.views.updateUserValue'),
                        )
                       
