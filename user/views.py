from django.shortcuts import render, redirect
from user.models import *
from site_admin.models import *
import datetime
from django.http import JsonResponse
from django.contrib import messages

# Create your views here.
def register(request):
    countries = country_table.objects.all()
    hobbies = hobby_table.objects.all()
    return render(request, "user/register.html", {
        "countries": countries,
        "hobbies": hobbies
    })

def getstate(request):
    country_id = request.GET['co']
    states = state_table.objects.filter(country_id_id=country_id) 
    return render(request,'user/getstate.html', {'states': states})
def registeraction(request):
     name=request.POST['name']
     dob=request.POST['dob']
     address=request.POST['address']
     gender=request.POST['gender']
     country=request.POST['country']
     state=request.POST['state']
     phone=request.POST['phone']
     username=request.POST['username']
     password=request.POST['password']
     secuirityquestion=request.POST['secuirityquestion']
     answer=request.POST['answer']
     
     user=register_table(name=name,address=address,dob=dob,gender=gender,country_id_id=country,
                         state_id_id=state,phone=phone,username=username,password=password,
                         securityquestion=secuirityquestion,answer=answer)
     
     user.save()
     hobby=request.POST.getlist('hobby')
     for h in hobby:
        hobbie=hobbie_table(userid_id=user.id,hobbyid_id=h)
        hobbie.save()
     messages.add_message(request,messages.INFO,"registration was successfull")
     return redirect("register")
 
def sendmessage(request):
    return render(request,'user/sendmessage.html') 


def checkuser(request):
    recivername=request.GET['uid']
    user=register_table.objects.filter(username=recivername)
    if len(user)>0:
        msg="exist"
    else:
        msg="notexist"
    return JsonResponse({'valid':msg})    

def sendmessageaction(request):
    recivername=request.POST['recivername']
    subject=request.POST['subject']
    message=request.POST['message']
    date=datetime.date.today()
    time=datetime.datetime.now().strftime("%H:%M") 
    senderid=request.session['userid']
    reciver=register_table.objects.filter(username=recivername)
    reciverid=reciver[0].id
    message=message_table(reciverid_id=reciverid,subject=subject,message=message,date=date,time=time
                          ,senderid_id=senderid)
    message.save()
    messages.add_message(request,messages.INFO,"message send successfully")
    return render(request,'user/sendmessage.html') 

def viewrecivedmessage(request):
    userid=request.session['userid']
    message=message_table.objects.filter(reciverid_id=userid)
    return render(request,'user/viewrecivedmessage.html',{'viewmessage':message})

def movetotrash(request):
    userid=request.session['userid']
    date=datetime.date.today()
    time=datetime.datetime.now().strftime("%H:%M") 
    check=request.POST.getlist('checkbox')
    for msg in check:
      user=trash_table(userid_id=userid,date=date,time=time,msgid_id=msg)
      user.save()
    return redirect("viewrecivedmessage")

def forwardmessage(request,id):
    user=message_table.objects.filter(id=id)
    message=user[0].message
    return render(request,'user/forwardmessage.html',{'views':user})

def forwardmessageaction(request):
    senderid=request.session['userid']
    subject=request.POST['forwardsubject']
    message=request.POST['forwardmessage']
    recivername=request.POST['username']
    reciver=register_table.objects.filter(username=recivername)
    reciverid=reciver[0].id
    date=datetime.date.today()
    time=datetime.datetime.now().strftime("%H:%M") 
    forward=message_table(senderid_id=senderid,subject=subject,message=message,reciverid_id=reciverid
                          ,date=date,time=time)
    forward.save()
    return redirect("viewmessage")

def viewsendmessage(request):
    userid=request.session['userid']
    message=message_table.objects.filter(senderid_id=userid)
    return render(request,'user/viewsendmessage.html',{'viewmessage':message})
