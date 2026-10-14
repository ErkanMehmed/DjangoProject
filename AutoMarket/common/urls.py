from django.urls import path
from common import views

app_name = 'common'

urlpatterns = [
    path("", views.home_view, name='home'),
    path("about/", views.about_view, name='about'),
]