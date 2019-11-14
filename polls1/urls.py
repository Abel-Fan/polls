from django.urls import path
from . import views

app_name = "polls1"
urlpatterns=[
    path("",views.index),
    path("question/<int:id>", views.question,name="question"),
    path("detail/<int:id>", views.detail,name="detail"),
]