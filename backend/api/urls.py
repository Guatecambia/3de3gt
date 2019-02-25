from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^candidatos/exige', views.CandidatoAsk.as_view(), name='candidato-ask'),
]
