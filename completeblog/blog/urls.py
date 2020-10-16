from django.urls import path
from . import  views
from django.conf.urls.static import static
from completeblog.settings import MEDIA_ROOT,MEDIA_URL
urlpatterns = [
    path('',views.index,name="index"),
    path('blog/',views.blog,name="blog"),
    path('search/',views.search,name="search"),
    path('about/',views.about,name="about")
]+static(MEDIA_URL,document_root=MEDIA_ROOT)
