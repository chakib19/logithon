from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from .models import Posts
from.models import Incidents


# Create your views here.
def index(request):

  
  #return HttpResponse('HELLO FROM POSTS')

  posts = Posts.objects.all()[:10]

  context = {
    'title': 'Latest Posts',
    'posts': posts
  }


  return render(request, 'app1/index.html', context)

def details(request, id):
  post = Posts.objects.get(id=id)

  context = {
    'post': post
  }

  return render(request, 'app1/details.html', context)
"""
def attaque(request):
	incidents = Incidents.objects.all()
	context = {
	  'title': 'Latest Posts',
      'incidents': incidents
  }

     return render(request, 'app1/incident.html', context)
  #return HttpResponse('HELLO FROM POSTS')

class Incidents(ModelForm):
    class Meta:
        model = attaque
"""
def attaque(request):

  
  #return HttpResponse('HELLO FROM POSTS')

  incidents = Incidents.objects.all()[:10]

  context = {
    'title': 'Liste des attaques',
    'incidents': incidents
  }


  return render(request, 'app1/incident.html', context)

def detaille(request, id):

  incidents = Incidents.objects.get(id=id)
  context = {
     'incidents': incidents
  }
    
  return render(request, 'app1/detaille.html', context)

class IncidentsForm(ModelForm):
    class Meta:
        model = Incidents
        fields = '__all__'

def attaque_create(request):
    if request.POST:
        form = IncidentsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app1/details.html')
    else:
        form = IncidentsForm()
    return render(request, 'attaque_create.html', {'form': form})
 

def attaque_update(request, id_attaque):
    attaque = get_object_or_404(attaque, id=id_attaque)
    form = IncidentsForm(request.POST or None, instance=attaque)
    if form.is_valid():
        form.save()
        return redirect(app1.views.attaque)
    return render(request, "attaque_create.html", {'form': form})
 

"""
def attaque_delete(request, id_attaque):
    attaque = attaque.objects.get(id=id_attaque)
    attaque.delete()
    return redirect('webgui.views.attaque_list')
"""