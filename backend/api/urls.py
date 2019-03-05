from django.conf.urls import url
from . import views
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token


urlpatterns = [
    url(r'^candidatos/exige', views.CandidatoAsk.as_view(), name='candidato-ask'),
    url(r'^candidatos/presentados/$', views.PresentedAsk.as_view(), name='presented-ask'),
    url(r'^candidatos/presentados/(?P<aspirantType>[A-Z]+)', views.PresentedAsk.as_view(), name='presented-ask'),
    url(r'^candidatos/presentar/$', views.PresentedForm.as_view(), name='present'),
    url(r'^3de3-admin/distritos/$', views.DistrictList.as_view(), name='district-admin'),
    url(r'^3de3-admin/distrito/(?P<pk>[0-9]+)', views.DistrictEdit.as_view(), name='district-admin-edit'),
    url(r'^3de3-admin/presentados/$', views.PresentadoList.as_view(), name='presentado-admin'),
    url(r'^3de3-admin/presentados/(?P<status>[A-Z]+)', views.PresentadoList.as_view(), name='presentado-admin'),
    url(r'^3de3-admin/presentado/(?P<pk>[0-9]+)', views.PresentadoEdit.as_view(), name='presentado-admin-edit'),
    url(r'^3de3-admin/candidatos/$', views.CandidatoAdminList.as_view(), name='candidato-admin'),
    url(r'^3de3-admin/candidatos/(?P<status>[A-Z]+)', views.CandidatoAdminList.as_view(), name='candidato-admin'),
    url(r'^3de3-admin/candidato/(?P<pk>[0-9]+)', views.CandidatoAdminEdit.as_view(), name='candidato-admin-edit'),
    url('api/token/', obtain_jwt_token),
    url('api/token/refresh/', refresh_jwt_token)
]
