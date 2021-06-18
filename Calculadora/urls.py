"""Calculadora URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from .views import pagina1, solve, biseccion, falsa, punto, newton, secante, muller #unidad 2
from .views import diffDivididas, hermite, lagrange, polNewton  #unidad 3
from .views import derivacion, integracion, richardson, rosemberg   #unidad 4
from .views import adaptativo, euler, runge, taylor #unidad 5

#Direcciones web de la pagina

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path("", pagina1),
    #unidad 2:
    path("biseccion/", biseccion),
    path("falsa/", falsa),
    path("punto/", punto),
    path("newton/", newton),
    path("secante/", secante),
    path("muller/", muller),

    #unidad 3:
    path("diffDivididas/", diffDivididas),
    path("hermite/", hermite),
    path("lagrange/", lagrange),
    path("polNewton/", polNewton),

    #unidad 4:
    path("derivacion/", derivacion),
    path("integracion/", integracion),
    path("richardson/", richardson),
    path("rosemberg/", rosemberg),

    #unidad 5:
    path("adaptativo/", adaptativo),
    path("euler/", euler),
    path("runge/", runge),
    path("taylor/", taylor),

    path("solve/", solve),
]

#handler404 = 'Calculadora.views.pag_404_not_found'
#handler500 = 'Calculadora.views.pag_500_error_server'