from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.home1,name="home"),
    url(r'^registration$', views.registration),
    url(r'^ivano-frankivsk-national-medical-university$', views.ivano),
    url(r'^gallery$', views.view_gallery),
    url(r'^poltava-state-medical-university$', views.poltava),
    url(r'^lviv-national-medical-university$', views.lviv),
    url(r'^bogomolets-national-medical-university$', views.bogo),
    # url(r'^1',views.data)
    url(r'previous-year-cutoffs',views.predictor),
    url(r'college-predictor',views.college_predictor),
]
