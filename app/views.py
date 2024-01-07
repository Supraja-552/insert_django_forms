from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.forms import *
from app.models import *
def create_topic(request):
    TO=Topic_form()
    d={'TO':TO}
    if request.method=='POST':
        TOFD=Topic_form(request.POST)
        if TOFD.is_valid():
            tn=TOFD.cleaned_data['topic_name']
            QLTO=Topic.objects.get_or_create(topic_name=tn)[0]
            QLTO.save()
            #d={'QLTO':QLTO}
            return HttpResponse('data is inserted in topic table')
    
    return render(request,'create_topic.html',d)
def create_webpage(request):
    WO=Webpage_form()
    
    d={'WO':WO}
    if request.method=='POST':
        WOFD=Webpage_form(request.POST)
        if WOFD.is_valid():
            tn=Topic.objects.get(topic_name=WOFD.cleaned_data['topic_name'])
            na=WOFD.cleaned_data['name']
            ur=WOFD.cleaned_data['url']
            em=WOFD.cleaned_data['email']
            QLWO=Webpage.objects.get_or_create(topic_name=tn,name=na,url=ur,email=em)[0]
            QLWO.save()
            QLWO=Webpage.objects.all()
            di={'QLWO':QLWO}
            return render(request,'display_webpage.html',di)
    
    return render(request,'craete_webpage.html',d)
def create_access(request):
    AO=Access_form()
    d={'AO':AO}
    if request.method=='POST':
        AFD=Access_form(request.POST)
        if AFD.is_valid():
            name=Webpage.objects.get(pk=AFD.cleaned_data['name'])
            au=AFD.cleaned_data['author']
            da=AFD.cleaned_data['date']
            QLAO=Access_Record.objects.get_or_create(name=name,author=au,date=da)[0]
            QLAO.save()
            return HttpResponse('data is inserted')
            
    return render(request,'create_access.html',d)
def select_multiple_webpage(request):
    TFO=Select_multiple_webpage()
    d={'TFO':TFO}
    if request.method=='POST':
        WFDO=Select_multiple_webpage(request.POST)
        QLWO=Webpage.objects.none()
        if WFDO.is_valid():
            WD=WFDO.cleaned_data['topic_name']
            for i in WD:
                QLWO=QLWO|Webpage.objects.filter(topic_name=i)
            di={'QLWO':QLWO}
            return render(request,'display_webpage.html',di)
    return render(request,'select_multiple_webpage.html',d)
def select_multiple_access(request):
    WFO=Select_multiple_access()
    d={'WFO':WFO}
    if request.method=='POST':
        WFDO=Select_multiple_access(request.POST)
        QLAO=Access_Record.objects.none()
        if WFDO.is_valid():
            WD=WFDO.cleaned_data['name']
            for i in WD:
                QLAO=QLAO|Access_Record.objects.filter(pk=i)
            di={'QLAO':QLAO}
            return render(request,'display_access.html',di)
    return render(request,'select_multiple_access.html',d)
def display_webpage(request):
    
    # QLWO=Webpage.objects.filter(topic_name='cricket')
     #QLWO=Webpage.objects.filter(topic_name='Foot Ball')
    QLWO=Webpage.objects.all().order_by('-topic_name')
   
    
    d={'QLWO':QLWO}
    return render(request,'display_webpage.html',d)