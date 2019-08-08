from django.urls import path
from . import views


urlpatterns = [
    path("", views.Index_View, name='index page'),
    path("georgian_bank/", views.Georgian_Bank_View, name='georgian bank page'),
    path("tbc_bank/",views.TBC_Bank_View, name='tbc bank page'),
    path("procredit_bank",views.Procredit_Bank_View,name='procredit bank page'),

]
