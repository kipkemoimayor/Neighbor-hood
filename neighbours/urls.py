from django.conf.urls import url
from django.conf.urls.static import static
from . import views
from django.conf import settings
user="collo"
urlpatterns=[
    url(r'^$',views.index,name="index"),
    url(r'^profile/',views.profile,name='profile'),
    url(r"^edit/",views.edit,name="edit"),
    url(r"^add/business/$",views.business,name='busi'),
    url(r'^feeds/neighbour/$',views.feeds,name="feeds"),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
