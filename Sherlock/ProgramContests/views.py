from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from django.middleware import csrf
from django.template import RequestContext
from django.shortcuts import render_to_response,HttpResponseRedirect,render
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,get_user,login,logout
from django.contrib.auth.views import logout_then_login
from Sherlock.ProgramContests.Forms import UserRegistrationForm,CompetitorForm, DocumentForm
from Sherlock.ProgramContests.models import *
from Sherlock import settings
import datetime
#import django.core.files.File
import os

@csrf_protect
def login_fn(request):
    username = password = ""
    print request.session.flush()
    print request
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username,password=password)
        print user
        if user is not None: 
            if user.is_active:
                request.session['userid']=user
                print "from session"
                print request.session['userid']
                print 'user is active'
                login(request,user)
                print user.is_staff
                if user.is_superuser:
                    return HttpResponseRedirect('/admin/')
                elif user.is_staff :
                    print "yes is staff"
                    request.session['judgeid']=user
                    return render_to_response("JudgeWelcome.html",{"form":user},RequestContext(request))
            else:
                state= "User is Inactive. Contact Admin"
                return HttpResponseRedirect('/user/login/')
        else:
            state = 'Your username/ password is incorrect'
            print state
            return HttpResponseRedirect('/user/login/')
    print request.user.id
    form = User.objects.get(username=request.user)
    print form
    return render_to_response('Welcome.html',{'username':username,'form':form},RequestContext(request))
    
@csrf_protect
def createUser(request):
    #form = UserRegistrationForm(request.POST)
    form = CompetitorForm(request.POST)
    print form
    print request.POST.get("username")
    print form.is_valid()
    if form.is_valid():
        print form.auto_id
        print request.POST.get("username")
        return render_to_response('Welcome.html',{'username':'Harish'},context_instance=RequestContext(request))
    else:
        form = UserRegistrationForm()
        print form.fields
    return render_to_response('CreateNewUser.html',{"form":form},context_instance=RequestContext(request))

#create user method
@csrf_protect
def createUserNew(request):
    regForm = UserRegistrationForm(request.POST)
    print regForm
    if regForm.is_valid():
        if regForm.error_messages:
            print "before createNewUser.html"
            regForm.save()
            print "after save"
            return render_to_response('UserCreationSuccess.html',{"form":regForm},context_instance=RequestContext(request))
        else:
            print "before save"
            regForm.save()
            print "before Login.html"
            return render_to_response("login.html",context_instance=RequestContext(request))
    else:
        print "before createNewUser.html1"
        return render_to_response('CreateNewUser.html',{"form":regForm},context_instance=RequestContext(request))
    

#user creation successful. Display the data
@csrf_protect 
def createUserSuccess(request):
    successForm = UserRegistrationForm(request.POST)
    if successForm.is_valid():
        request.session['userName']=request.POST.get("username")
        render_to_response("UserCreationSuccess.html",{"form":successForm})
    else:
        render_to_response("Welcome.html")
#edit profile
@csrf_protect
def editprofile(request):
    print request.POST
    #print request
    print "inside edit profile method"
    userName = request.POST.get("username")
    print userName
    editproform = CompetitorForm(request.POST)
    print editproform
#    print userName
#    user = User.objects.get(username=userName)
#    print user
#    editproform=UserRegistrationForm(request.POST,instance=user)
#    print editproform
   # if editproform.is_valid():
    print "edit profile"
    #    editproform.save()
    print "after edit save"
    return render_to_response('updateUserProfile.html',{"form":editproform,"user":request.user},RequestContext(request))
#    else:
#        editproform.save()
#        print "after edit profile save in case of failure"
#        return render_to_response("login.html",context_instance=RequestContext(request))
#        


#def TakeExam(request):
#    #print request
#    #contest_var = Contests.objects.get()
#    #for row in Contests.objects.all():
#     #   print row.contestName
#    return render_to_response('TakeExam.html',{'contest_var':Contests.objects.all}) # this is working fine.!!
#
#def Inst(request):
#    print 'inside instructions'
#    #c= request.POST.get("startTime")
#    print request.POST
#    print request.POST.get('hiddenContestVar') # all the below statements displayed none..:(
#    print request.POST.get('Contest.hiddenContestVar')
#    print request.POST.get('Contest.row') 
#    #print request
#    return render_to_response('Instructions.html',context_instance=RequestContext(request))

@csrf_protect
#,method to redirect to page for judget to view users
def judgeViewUsers(request):
    print request
    judgeVar = request.session['judgeid']
    print judgeVar
    print "from session variable"
    print request.session['userid']
    
    if judgeVar is not None:
        judgeUserId = User.objects.get(username=judgeVar)
        judgeObj = Judge.objects.get(judgeID=judgeUserId.id)
        print judgeObj
        evaluationObj = ContestParticipation.objects.filter(judgeId=judgeObj.id,status="submitted")
        
        #print evaluationObj.lang_used
        for evalObj in evaluationObj:
            print evalObj.lang_used
            print evalObj.compId
            print evalObj.id
            print evalObj.filepath
    print evalObj
    print "before rendering - before calling function"
    return render_to_response("JudgeDisplayUsersList.html",{"user":request.user,"ContestPart":evaluationObj },RequestContext(request))
        
#method to update user profile
@csrf_protect
def updateUser(request):
    print "inside update profile method"
    user=request.user
    competitorForm = CompetitorForm(request.POST)
    print competitorForm
    print competitorForm.is_valid()
    if competitorForm.is_valid():
        competitorForm.save(commit=True)
    print request
    return render_to_response('Welcome.html',{'user':user},RequestContext(request))

#user home redirection page
@csrf_protect    
def userHome(request):
    print request.user
    return render_to_response("Welcome.html",{"form":request.user},RequestContext(request))

#judge home redirection page
@csrf_protect    
def judgeHome(request):
    print request.user
    return render_to_response("JudgeWelcome.html",{"form":request.user},RequestContext(request))
       
#method to logout a user
def user_logout(request):
    logout(request)
    print "user logged out"
    return HttpResponseRedirect("/user/login/")
    #HttpResponseRedirect("login.html")
    
#code from anupama for user related actions
def TakeExam(request):
     print request.method
     time= datetime.datetime.now()
     print time
     contest_var = Contests.objects.filter(endTime__gte= time)
     return render_to_response('TakeExam.html',{'contest_var':Contests.objects.filter(endTime__gte=time)})
@csrf_protect
def CurrentExam(request):
    #compid='boppana.anupama@gmail.com'
    userid=request.session['userid']
    print 'I am here'
    status='submitted'
    dicarr={}
    list1 = []
    list2 = []
    for p in ContestParticipation.objects.raw('select distinct(id) from programcontests_contestparticipation where compId_id=(select id from auth_user where username=%s)',[userid]):
        '''
        r1= Contests.objects.raw('select * from programcontests_contests where contestName=%s',[p.contestQuestionId.contestId.contestName])
        for r in r1:
            print r1.contestName 
        '''
        for r in Contests.objects.filter(contestName=p.contestQuestionId.contestId.contestName):    
            print r
            list1.append(r)
    for x in list1:
        if x not in list2:
            list2.append(x)    
    print list2
    return render(request,'CurrentExam.html',{'contest_var':list2})
                                              #(ContestParticipation.objects.raw('select distinct(id) from programcontest_contestparticipation where compId_id=(select id from auth_user where username=%s)',[userid]))})
@csrf_protect
def Inst(request):
    if request.method == 'GET':
        contestName=request.GET.get('name')
        response= HttpResponseRedirect("hi")
        response = render_to_response('Instructions.html',{'contest':Contests.objects.get(contestName=contestName)},context_instance=RequestContext(request))
        response.set_cookie('contestName')
        return response              
    else:   
        print 'form invalid so entered here'
        return render_to_response('TakeExam.html',{'contest_var':Contests.objects.all()},context_instance=RequestContext(request))
@csrf_protect
def showQuest(request):
    if request.method == 'POST':
        print request.POST
        f=request.POST.get('hi')
        c=f[6:]
        print c
        print f[6:]
        print 'inside post'
        request.session['contestid']=c
        for d in ContestQuestion.objects.filter(contestId=c):
            print d.questionId
        doc = DocumentForm(request.POST)
        return render_to_response('FileUpload.html', {'form': ContestQuestion.objects.filter(contestId=c),
                                        "docForm":doc,"username":request.session['userid']},context_instance=RequestContext(request))          
    else:    
        print 'error showing questions page' 
@csrf_protect
def viewScore(request):
    uid='Anupama'
    p=ContestParticipation.objects.raw('select score from programcontests_ContestParticipation where compId_id=%s',[uid])
    print p
    return render_to_response('ScoreHistory.html',{'form':p}) 

#code from madhu for file upload
@csrf_protect
def fileupload(request):
    
    #form = UploadFileForm(request.POST,request.FILES)
    if request.method == 'POST':
        
        print "inside if"
        print request.FILES
        form = DocumentForm(request.POST, request.FILES)
        newFile = Filetrial(filecontent=request.FILES['fileField'])
        userVar = User.objects.get(username=request.session['userid'])
        print userVar.id
        newFile.userid = userVar.id
        fileObj = Filetrial(filecontent=request.FILES['fileField'])
        fileObj.userid = userVar
        newFile.save()
        print request.POST.get("question")
        print newFile.filecontent.read()
        str = newFile.filecontent.read()
        print "URL for the file " + newFile.filecontent.url
#        os.mkdir(os.path.join("/",userVar.id))
        print os.path
        print settings.MEDIA_ROOT
        #fileObj.save()
        print newFile
        print request.POST
      ##Save data to Contest Participation Table
        question=request.POST.get("question")
        contest = Contests.objects.get(contestName=request.session['contestid'])
        print userVar.id
        compObj = Competitor.objects.get(compID=userVar)
        print contest.contestName
        questionId = Questions.objects.get(question=question) 
        contQuestion = ContestQuestion.objects.get(contestId=contest,questionId=questionId)
        filepath=newFile.filecontent.url
        lang = request.POST.get("lang_used")
        print lang
        print contQuestion.id
        print compObj.id
        
        contestParticipation = ContestParticipation()
#        
#        try:
#            contestPart = ContestParticipation.objects.get(contestQuestionId=contQuestion,
#                                               compId=compObj)
#            print contestPart
#                                               
##            contestParticipation = ContestParticipation.objects.raw("select id from program_contests.contestparticipaton"+ 
##                            "where contestQuestionId = "+contQuestion.id+"and compId="+compObj.id)
#            
#        except AttributeError:
#            print "object doesnt exist"
#        ##check if there is already an entry in contest participation table
#        ## if yes, update. If no, then create a new entry
#        if contestParticipation is not None:
#            print "inside this"
#        contestParticipation = ContestParticipation.objects.get(contestQuestionId=contQuestion.id,
#                                               compId=compObj.id)
#        contestParticipation.filepath = filepath
#        else:
#            print "inside else - 1"
        contestParticipation = ContestParticipation(contestQuestionId=contQuestion,
                                    compId=compObj,status="submitted",filepath=filepath,lang_used=lang)
        print contestParticipation.contestQuestionId
        contestParticipation.save()
      ##end of action
        
        if form.is_valid():
            print "inside if1"
            newFile = Filetrial(filecontent=request.FILES['fileField'])
            print "inside IF2"
            userVar = User.objects.get(username=request.session['userid'])
            print userVar.id
            newFile.userid = userVar.id
            newFile.save()
            print newFile.filecontent.read()
            str = newFile.filecontent.read()
            
#            '''
           # docForm = Filetrial.objects.all()
#            print newFile.filecontent.read()
#            line=file.readline()
#            destination.write(line)
#            '''
            #handle_uploaded_file(request.FILES['file'])
            #return render_to_response("fileSuccess.html",{"docForm":newFile},RequestContext(request))
            return HttpResponseRedirect("TakeExam/Instructions/ShowQuestions/")
        else:
            print "inside else"
            request.method="POST"
            #return HttpResponseRedirect("/user/TakeExam/Instructions/ShowQuestions/")
            return render_to_response('FileUploadSuccess.html', context_instance=RequestContext(request))
    else:
        form = DocumentForm()
        print form
        return render_to_response('FileUpload.html', {'form': form},context_instance=RequestContext(request))
    
#update user score through judge UI
@csrf_protect
def updateUserScore(request):
    if request.method == 'POST':
        contestPartId = request.POST.get("contPartId")
        print contestPartId
        userName = request.POST.get("userName")
        print userName
        contestParticipationObj = ContestParticipation.objects.get(id=int(contestPartId))
        print contestParticipationObj.filepath
        CQId = contestParticipationObj.contestQuestionId
        print CQId.id
        ContestQuestObj = ContestQuestion.objects.get(id=CQId.id)
        print ContestQuestObj.contestId
        questObj = Questions.objects.get(id=ContestQuestObj.questionId.id)
        print " bvlank "
        print questObj.question
        mainFilePath = settings.MEDIA_ROOT+"/"+contestParticipationObj.filepath
        print mainFilePath
        filePointer = open(mainFilePath,"rb+")
        data = filePointer.read()
        question = questObj.question
        contestName = ContestQuestObj.contestId
        print data
        #return render_to_response("JudgeWelcome.html")
        return render_to_response("FileDisplay.html",{'contPartObj':contestParticipationObj,
                                                  'data':data,'question':question,'contestName':contestName},RequestContext(request))
    
#update user score from file display
@csrf_protect
def updateUserValue(request):
    if request.method=='POST':
        contestPartId = request.POST.get("contPartID")
        score = request.POST.get("score")
        contPartObj =  ContestParticipation.objects.get(id=contestPartId)
        contPartObj.score = score
        contPartObj.status="scored"
        print contPartObj.score
        contPartObj.save()
        
        return HttpResponseRedirect("/user/judge/viewUsers/")
    