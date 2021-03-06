from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r"^scraper/(?P<urlToScrap>.+)$", views.scraper_launch, name='scraperLaunch'),
    url(r"^testretrieve/(?P<urlToScrap>.+)$", views.test_retrieve, name='test_retrieve')
]