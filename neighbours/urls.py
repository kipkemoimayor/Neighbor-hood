from django.conf.urls import url
from . import views
user="collo"
urlpatterns=[
    url(r'^$',views.index,name="index"),
    url(r'^profile/',views.profile,name='profile'),
    url(r"^edit/",views.edit,name="edit"),

]
