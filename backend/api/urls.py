from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^candidatos/exige', views.CandidatoAsk.as_view(), name='candidato-ask'),
    url(r'^candidatos/presentados/$', views.PresentedAsk.as_view(), name='presented-ask'),
    url(r'^candidatos/presentados/(?P<aspirantType>[A-Z]+)', views.PresentedAsk.as_view(), name='presented-ask'),
    url(r'^candidatos/presentar/$', views.PresentedForm.as_view(), name='presented-ask'),
]
