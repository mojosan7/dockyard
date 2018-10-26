from django.urls import path
from . import views
from .views import ComputecalcList

app_name = 'computecalc'
urlpatterns = [
    path('', ComputecalcList.as_view()),
]
