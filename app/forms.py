from django import forms
from app.models import *
class Topic_form(forms.Form):
    topic_name=forms.CharField()
class Webpage_form(forms.Form):
    TO=Topic.objects.all()
    l=[]
    for i in TO:
         l.append([i.topic_name,i.topic_name])
    
    topic_name=forms.ChoiceField(choices=l)
    name=forms.CharField()
    url=forms.URLField()
    email=forms.EmailField()
class Access_form(forms.Form):
    WO=Webpage.objects.all()
    l= [(i.pk,i.name) for i in WO]
    name=forms.ChoiceField(choices=l)
    author=forms.CharField()
    date=forms.DateField()
class Select_multiple_webpage(forms.Form):
    l=[(i.topic_name,i.topic_name) for i in Topic.objects.all() ]
    topic_name=forms.MultipleChoiceField(choices=l)
class Select_multiple_access(forms.Form):
    l=[(i.pk,i.name) for i in Webpage.objects.all()]
    name=forms.MultipleChoiceField(choices=l)
   