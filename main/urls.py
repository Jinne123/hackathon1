from . import views
from django.urls import path

urlpatterns = [
    path('', views.begin_scherm, name="begin_scherm"),
    path('ingelogd', views.home_page, name="home_page"),
    path('annuleer_abonnement', views.annuleer_abonnement, name="annuleer_abonnement"),
    path('personal_trainer', views.personal_trainer, name="personal_trainer"),
    path('koop_cursus', views.koop_cursus, name="koop_cursus"),
    path('koop_cursus2/<str:cursus>/', views.koop_cursus2, name="koop_cursus2"),
    path('pas_aanvragen', views.pas_aanvragen, name="pas_aanvragen"),
]
