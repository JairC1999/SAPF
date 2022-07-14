from django.urls import path
from .views import IndexView

urlpatterns = [
    #path('endereço/', IndexView.as_view(), name='Nome da url'),
    path('', IndexView.as_view(), name='Consegui'), 
]