from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms

class FormularioRegistro(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget = forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña", widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]
        help_texts = {
            'username': ''
        }
        labels = {
            "username": "Usuario",
            "first_name": "Nombre",
            "last_name": "Apellido",
        }

class FormularioLogin(AuthenticationForm):
    username = forms.CharField(label="Usuario")
    password = forms.CharField(label="Contraseña", widget = forms.PasswordInput)

class FormularioActualizacion(forms.ModelForm):
    username = forms.CharField(label= "Usuario",required = False)
    first_name = forms.CharField(label= "Nombre", required = False)
    last_name = forms.CharField(label= "Apellido", required = False)
    email = forms.EmailField(label= "Email", required = False)

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]
    
   

class FormularioNuevaContraseña(PasswordChangeForm):
    old_password = forms.CharField(label="Contraseña Actual", widget = forms.PasswordInput, help_text='' )
    new_password1 = forms.CharField(label="Contraseña Actual", widget = forms.PasswordInput, help_text='')
    new_password2 = forms.CharField(label="Contraseña Actual", widget = forms.PasswordInput, help_text='')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.help_text = None
            field.error_messages['required'] = ' '


   