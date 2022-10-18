from django.urls import path,include
from . import views
urlpatterns = [
    path("",views.IndexView,name="index"),
    path("forms/",views.htmlform,name="htmlform"),
    path("insert/",views.InsertPageView,name="insertpage"),
    path("insertdata/",views.InsertData,name="insertdata"),
]
