from django import forms

class Formulario(forms.Form):
	nombre = forms.CharField(max_length=100)
	mensaje = forms.CharField()
	mail = forms.EmailField()

class FormularioContacto(forms.Form):
	correo = forms.EmailField()
	mensaje = forms.CharField()