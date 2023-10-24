from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Comunicado, Entidad
from django.http import HttpResponse

# Create your views here.

def index(request, entidad_id=None):
  comunicados = Comunicado.objects.order_by('-fecha_publicacion')
  entidades = Entidad.objects.all()
    
  if entidad_id:
    comunicados = comunicados.filter(entidad =entidad_id)
  return render(request,'myapp/index.html',{'comunicados': comunicados, 'entidades': entidades} )




