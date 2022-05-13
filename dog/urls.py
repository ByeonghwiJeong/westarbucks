

from django.urls import path
from .views import DogsView, OwnersView

urlpatterns =[
  path("", DogsView.as_view()),
  path("owner/", OwnersView.as_view())

]