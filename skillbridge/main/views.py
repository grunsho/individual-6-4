from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from .forms import RegistroUsuariosForm

# Create your views here.

def index(request):
    return render(request, 'landing.html')

class UsuariosView(TemplateView):
    template_name = 'usuarios.html'
    
    def get(self, request):
        usuarios = User.objects.all()
        context = {'usuarios': usuarios}
        return render(request, 'usuarios.html', context)

class RegistroUsuariosView(View):
    def get(self, request):
        form = RegistroUsuariosForm()
        context = {'form': form}
        return render(request, 'registro_usuarios.html', context)
    def post(self, request):
        form = RegistroUsuariosForm(request.POST)
        if form.is_valid():
            try:
                usuario = User.objects.create_user(
                    username = request.POST['username'],
                    password = request.POST['password1'],
                    first_name = request.POST['first_name'],
                    last_name = request.POST['last_name'],
                    email = request.POST['email']
                )
                usuario.save()
                # login(request, 'usuarios')
                return redirect('usuarios')
            except Exception:
                context = {'form': form, 'error': 'El nombre de usuario ya existe'}
                return render(request, 'registro_usuarios.html', context)
        else:
            context = {'form': form }
            return render(request, "registro_usuarios.html", context)