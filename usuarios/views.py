from django.shortcuts import render, redirect
from django.contrib.auth import login
from usuarios.forms import FormularioRegistro, FormularioLogin, FormularioActualizacion, FormularioNuevaContraseña
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash

def login_view(request):

    if request.method == "POST":
        formulario = FormularioLogin(request, data = request.POST)
        if formulario.is_valid():
            usuario = formulario.get_user()

            login(request, usuario)
            return redirect('inicio')
    else:
        formulario = FormularioLogin()

    return render(request, 'login.html', {'formulario': formulario}) 

def register_view(request):

    if request.method == "POST":
        formulario = FormularioRegistro(request.POST)
        if formulario.is_valid():
            formulario.save()

            return redirect('login')
    else:
        formulario = FormularioRegistro()

    return render(request, 'register.html', {'formulario': formulario})

def profile_view(request):
    return render(request, 'profile.html')

@login_required
def update_data(request):
    usuario = request.user
    form_contraseña = FormularioNuevaContraseña(user=request.user, data=request.POST)

    if 'actualizar_datos' in request.POST:
        form_usuario = FormularioActualizacion(request.POST, instance=usuario)
        if form_usuario.is_valid():
            for campo in form_usuario.cleaned_data:
                valor = form_usuario.cleaned_data[campo]
                if valor:
                    setattr(usuario, campo, valor)
            usuario.save()
            return redirect('profile')
    
    elif 'cambiar_contraseña' in request.POST:
         if form_contraseña.is_valid():
             usuario = form_contraseña.save()
             update_session_auth_hash(request, usuario)
             return redirect('profile')
    
    else:
        form_usuario = FormularioActualizacion(instance=usuario)
        form_contraseña  = FormularioNuevaContraseña(user=request.user)

    return render(request, 'update_data.html', {'form_user': form_usuario, 'form_pass': form_contraseña})