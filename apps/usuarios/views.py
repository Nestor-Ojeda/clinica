from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator #para medida de seguridad
from django.views.decorators.cache import never_cache # seguridad. para que no se guarde
from django.views.decorators.csrf import csrf_protect #Seguridad
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from .forms import FormularioLogin


class Inicio(TemplateView):
    template_name = 'index.html'

class Login(FormView):
    template_name = 'login.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('index')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self,request, *args, **kwargs):
        if request.user.is_authenticated: #verifica si ya está logueado lo manda al index(pincipal)
            return HttpResponseRedirect(self.get_success_url())
        else: #si no está logueado lo manda al login
            return super(Login, self).dispatch(request, *args, **kwargs)

    # valido el formulario que se utiliza en esta vista
    def form_valid(self, form):
        login(self.request,form.get_user())
        return super(Login, self).form_valid(form)

def logoutUsuario(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login')
