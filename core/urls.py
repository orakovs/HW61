from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(template_name='login.html'), name='login_url'),
    path('logout/', LogoutView.as_view(), name='logout_url'),
    path('store/', include('store_app.urls')),
]
