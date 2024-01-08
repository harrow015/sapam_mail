from django.shortcuts import render,redirect
from site_admin.models import *
from user.models import *
# Create your views here.
def index(request):
    return render(request,"common/index.html")
def login(request):
    return render(request,"common/login.html")

def loginaction(request):
    username=request.POST['username']
    password=request.POST['password']
    admin=admin_table.objects.filter(username=username,password=password)
    if(admin.count()>0):
        request.session['adminid']=admin[0].id
        return render(request,'site_admin/adminhome.html')
    
    user=register_table.objects.filter(username=username,password=password)
    if(user.count()>0):
        request.session['userid']=user[0].id
        return render(request,'user/userhome.html')
    else:
        return redirect("index")


def addhobby(request):
    return render(request,'site_admin/addhobby.html')    

def addhobbyaction(request):
    hobbyname=request.POST['hobbyname']
    hobby=hobby_table(hobbyname=hobbyname)
    hobby.save()
    return redirect('addhobby')

def addfactor(request):
    hobbies = hobby_table.objects.all()
    return render(request,'site_admin/addfactor.html', {'hobbies': hobbies}) 


def addfactoraction(request):
    factor=request.POST['hfactor']
    hobbie=request.POST['hobby']
    hfactor=hobbyfactor_table(factor_name=factor,hobbyid_id=hobbie)
    hfactor.save()
    return redirect('addfactor')

def addseason(request):
    return render(request,'site_admin/addseason.html')

def addseasonaction(request):
    season=request.POST['season']
    addseason=season_table(season_name=season)
    addseason.save()
    return redirect('addseason')

def addseasonfactor(request):
    season = season_table.objects.all()
    return render(request,'site_admin/addseasonfactor.html', {'seasons': season}) 

def addseasonfactoraction(request):
    seasonfactor=request.POST['sfactor']
    season=request.POST['season']
    sfactor=seasonfactor_table(factor_name=seasonfactor,seasonid_id=season)
    sfactor.save()
    return redirect('addseasonfactor')



