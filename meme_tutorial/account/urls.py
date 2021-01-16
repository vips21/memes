from django.urls import path
from django.contrib.auth import views as auth_views
from .views import home, sign_up


urlpatterns = [
    # path('admin/', admin.site.urls)
    path('', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
    path('home', home, name='home'),
    path('sign_up', sign_up, name='sign_up'),
    path('logout', auth_views.LogoutView.as_view(next_page='login'), name='logout')
]