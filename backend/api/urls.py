from django.conf.urls import url
from . import views
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token


urlpatterns = [
    url(r'^candidatos/exige', views.CandidatoAsk.as_view(), name='candidato-ask'),
    url(r'^candidato/patrimonial/(?P<pk>[0-9]+)', views.CandidatoPatrimonial.as_view(), name="candidato-patrimonial"),
    url(r'^candidato/intereses/(?P<pk>[0-9]+)', views.CandidatoInterests.as_view(), name="candidato-interests"),
    url(r'^candidatos/presentados/$', views.PresentedAsk.as_view(), name='presented-ask'),
    url(r'^candidatos/presentados/(?P<aspirantType>[A-Z]+)', views.PresentedAsk.as_view(), name='presented-ask'),
    url(r'^candidatos/counts/', views.CandidatoStatisticsView.as_view(), name='presented-statistics'),
    url(r'^candidatos/presentar/$', views.PresentedForm.as_view(), name='present'),
    url(r'^generico/distritos/', views.DistrictListById.as_view(), name='district-simple-list'),
    url(r'^generico/municipios/', views.MunicipalityList.as_view(), name='muni-simple-list'),
    url(r'^generico/partidos/', views.PartyListOnlyPP.as_view(), name='pp-simple-list'),
    url(r'^generico/comites/', views.PartyListOnlyCC.as_view(), name='cc-simple-list'),
    url(r'^generico/partidosycomites/', views.PartyList.as_view(), name='pp-cc-simple-list'),
    url(r'^generico/estadisticas/', views.StatisticsView.as_view(), name='statistics-frontend'),
    url(r'^3de3-admin/distritos/$', views.DistrictList.as_view(), name='district-admin'),
    url(r'^3de3-admin/distrito/(?P<pk>[0-9]+)', views.DistrictEdit.as_view(), name='district-admin-edit'),
    url(r'^3de3-admin/presentados/(?P<status>[A-Z]+)', views.PresentadoList.as_view(), name='presentado-admin'),
    url(r'^3de3-admin/presentado/(?P<pk>[0-9]+)', views.PresentadoEdit.as_view(), name='presentado-admin-edit'),
    url(r'^3de3-admin/candidatos/$', views.CandidatoAdminList.as_view(), name='candidato-admin-create'),
    url(r'^3de3-admin/partidos/$', views.PartyAdminList.as_view(), name='partido-admin-create'),
    url(r'^3de3-admin/partido/(?P<pk>[0-9]+)', views.PartyAdminEdit.as_view(), name='partido-admin-edit'),
    url(r'^3de3-admin/munis/$', views.MunicipalityAdminList.as_view(), name='partido-admin-create'),
    url(r'^3de3-admin/muni/(?P<pk>[0-9]+)', views.MunicipalityEdit.as_view(), name='municipality-admin-edit'),
    url(r'^3de3-admin/candidatos/$', views.CandidatoAdminList.as_view(), name='candidato-admin'),
    url(r'^3de3-admin/candidatos/(?P<status>[A-Z]+)', views.CandidatoAdminList.as_view(), name='candidato-admin'),
    url(r'^3de3-admin/candidato/(?P<pk>[0-9]+)', views.CandidatoAdminEdit.as_view(), name='candidato-admin-edit'),
    url(r'^3de3-admin/selectcandidatos', views.CandidatoSelectList.as_view(), name='candidato-admin-select-list'),
    url(r'^3de3-admin/estadisticas/', views.StatisticsAdminView.as_view(), name='statistics-backend'),
    url('api/token/', obtain_jwt_token),
    url('api/token/refresh/', refresh_jwt_token)
]
