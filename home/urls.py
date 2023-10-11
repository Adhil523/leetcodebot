from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('chat/<int:id>',views.chatbot),
    path('chat/suggest',views.suggest)
]