from django.urls import path
from usuarios.views import login_view, register_view, profile_view, update_data
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_view, name = 'login'),
    path('register/', register_view, name = 'register'),
    path('logout/', LogoutView.as_view(template_name="logout.html"), name = 'logout'),
    path('profile/', profile_view, name = 'profile'),
    path('update_data/', update_data, name = 'update_data'),
]
