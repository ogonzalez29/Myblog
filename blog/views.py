# -*- coding: utf-8 -*-
from django.template import loader, Context
from django.http import HttpResponse
from blog.models import BlogPost
from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from forms import Formulario, FormularioContacto
from django.core.mail import EmailMessage
from django.template import RequestContext
from django.views.generic import TemplateView, ListView

def archive(request):
    posts = BlogPost.objects.all()
    mi_template = loader.get_template("archive.html")
    mi_contexto = Context({'posts':posts})
    return HttpResponse(mi_template.render(mi_contexto))

def contacto(request):
	if request.method == 'POST': #Si el formulario es enviado
		form = Formulario(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('/myblog/blog/gracias/')
	else:
			form = Formulario() #An unbound form

	return render(request, 'contacto.html', {'form':form,})

def gracias(request):
	html = '<html><body>Gracias por enviarnos su comentario...</body></html>'
	return HttpResponse(html)

def contactomail(request):
	if request.method == 'POST':
		formulario = FormularioContacto(request.POST)
		if formulario.is_valid():
			asunto = 'Este es un mensaje de mi blog en DJANGO'
			mensaje = formulario.cleaned_data['mensaje']
			correo = formulario.cleaned_data['correo']
			mail = EmailMessage(asunto, mensaje, to=[correo], cc=['contacto@servitalleres.com'])
			mail.send()
		return HttpResponseRedirect('/')

	else:
		pass
		formulario = FormularioContacto()

	return render_to_response('contacto_mail.html', {'formulario': formulario},
		                      context_instance=RequestContext(request))

def index(request):
	return HttpResponseRedirect('/')

