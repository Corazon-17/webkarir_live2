from django.urls import path
from . import views
app_name="webkarirApp"

urlpatterns = [
    path('', views.index, name="index"),
    path('karir', views.getKarir, name="karir"),
    path('lowongan/<int:id>', views.getDetail.as_view(), name="detail"),
    path('lamaran/<int:id>', views.getLamaran.as_view(), name="lamaran"),
    path('magang', views.getMagang, name="magang"),
    path('formulir/<str:nama>', views.getFormulir.as_view(), name="formulir"),
    path('login', views.getLogin.as_view(), name="login"),
    path('logout', views.getLogout, name="logout"),
    path('register', views.getRegister, name="register")
]
