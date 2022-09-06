"""ProyectoDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ProyectoDjango.views import despedida, saludo_plantilla_base, saludo_plantilla_variable, despedida, dame_fecha, calcula_edad

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo1/', saludo_plantilla_base),
    path('saludo2/', saludo_plantilla_variable),
    path('nosveremos/', despedida),
    path('fecha/', dame_fecha),
    path('edades/<int:edad>/<int:agno>', calcula_edad)
]
