from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from news.models import News
from django.core.paginator import Paginator
from Subscribers.models import Subscriber
# from .forms import usersform
def HomePage(request):
    # for a in servicesData:
    #     print(a.servive_icon)
    # print(Service)
    data={
        'title':"ANVESHAN | NIE College",
        
    }
    # try:
    #     if request.method=="POST":
    #         name=request.POST.get('name'),
    #         email=request.POST.get('email')
    #         cre={
    #             'name':name,
    #             'email':email
    #         }
    #         url="/thankyou/?name={}".format(name)
    #         return HttpResponseRedirect(url)
    # except:
    #     pass
    return render(request,"anveshan.html",data)

def Subscribers(request):
    if request.method=="POST":
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        if name and email:
            en=Subscriber(subscribers_name=name,subscribers_email=email)
            en.save()
            # n='Subscribed..'
    url="/thankyou/?name={}".format(name)
    return HttpResponseRedirect(url)
        # return render(request,"about.html")

def About(request):
    data={
        'title':"ANVESHAN | About"
    }
    return render(request,"about.html")

def Projects(request):
    # servicesData=Service.objects.all().order_by('-service_title')[2:3]    --> ( - )indicates the decending order and after that there is the limit method starting and ending index
    data={
        'title':"ANVESHAN | About",
        # 'servicesData':servicesData 
    }
    return render(request,"projects.html",data)

def Research(request):
    data={
        'title':"ANVESHAN | About"
    }
    return render(request,"research.html")

def Events(request):
    
    data={
        'title':"ANVESHAN | About",
        
    }
    return render(request,"events.html",data)

def Resourse(request):
    data={
        'title':"ANVESHAN | About"
    }
    return render(request,"resourse.html",data)

def Blogs(request):
    newsData=News.objects.all()
    data={
        'title':"ANVESHAN | About",
        'newsData':newsData
    }
    return render(request,"blogs.html",data)

def NewsDetails(request,slug):
    # print(slug)
    NewsDetails=News.objects.get(news_slug=slug)
    data={
        'newsDetails':NewsDetails
    }
    return render(request,"newsdetails.html",data)

def Members(request):
    data={
        'title':"ANVESHAN | About"
    }
    return render(request,"members.html")

def Contacts(request):
    data={
        'title':"ANVESHAN | About"
    }
    return render(request,"contacts.html")

def Newsletter(request):
    data={
        'title':"ANVESHAN | About"
    }
    return render(request,"newsletter.html")

def Thankyou(request):
    if request.method=="GET":
        name=request.GET.get('name','')

        if isinstance(name,tuple):
            name=name[0]
    else:
        name=''
    data={
        'name': name
    }
    return render(request,"thankyou.html",data)

def Submitform(request):
    try:
        if request.method=="POST":
            name=request.POST.get('name')
            email=request.POST.get('email')
            cre={
                'name':name,
                'email':email
            }
            url="/thankyou/?name={}".format(name)
            return HttpResponseRedirect(url)
    except:
        pass
    # return HttpResponse(request)


def Calculator(request):
    m1=''
    m2=''
    m3=''
    m4=''
    m5=''
    m6=''
    total=''
    percentage=''
    grade=''
    try:
        if request.method=="POST":
            if request.POST.get('m1')=="":
                return render(request,"calculator.html",{'error':True})
            m1=eval(request.POST.get('m1'))
            m2=eval(request.POST.get('m2'))
            m3=eval(request.POST.get('m3'))
            m4=eval(request.POST.get('m4'))
            m5=eval(request.POST.get('m5'))
            m6=eval(request.POST.get('m6'))
            total=m1+m2+m3+m4+m5+m6
        print(total)
        percentage=total/6
        if (percentage>90):
            grade="O"
        elif(percentage>80):
            grade="A+"
        elif(percentage>70):
            grade="A"
        elif(percentage>60):
            grade="B+"
        elif(percentage>50):
            grade="B+"
        elif(percentage>40):
            grade="C"
        else:
            grade="Fail"
    except:
        ans="Invalid Operation...!!"
    return render(request,"calculator.html",{'total':total,'m1':m1,'m2':m2,'m3':m3,'m4':m4,'m5':m5,'m6':m6,'percentage':percentage,'grade':grade})

# def anveshan(request):
#     return HttpResponse("Welcome to Anveshan")

# def course(request,courseid):
#     return HttpResponse(courseid)