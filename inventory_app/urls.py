from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('dashboard/', views.index, name='inventory_app-index'),
    path('users/', views.users, name='inventory_app-users'),
    path('available_ports/', views.available_ports, name='inventory_app-available_ports'),
    path('reservations/', views.reservation, name='inventory_app-reservation'),
    path('cgw/', views.cgw, name='inventory_app-cgw'),
    path('cgw_json/', cgw_json, name='inventory_app-cgw_json'),
    path('cgw_form/', cgw_form, name='inventory_app-cgw_form'),
    path('csde/', views.csde, name='inventory_app-csde'),
    path('csde_json/', csde_json, name='inventory_app-csde_json'),
    path('csde_form/', csde_form, name='inventory_app-csde_form'),
    path('dgw/', views.dgw, name='inventory_app-dgw'),
    path('dgw_json/', dgw_json, name='inventory_app-dgw_json'),
    path('dgw_form/', dgw_form, name='inventory_app-dgw_form'),
    path('dsde/', views.dsde, name='inventory_app-dsde'),
    path('dsde_json/', dsde_json, name='inventory_app-dsde_json'),
    path('dsde_form/', dsde_form, name='inventory_app-dsde_form'),
    path('igw/', views.igw, name='inventory_app-igw'),
    path('mx/', views.mx, name='inventory_app-mx'),
    path('sigr/', views.sigr, name='inventory_app-sigr'),
    path('was/', views.was, name='inventory_app-was'),
    path('wgr/', views.wgr, name='inventory_app-wgr'),
    path('wpr/', views.wpr, name='inventory_app-wpr'),
    path('wrs/', views.wrs, name='inventory_app-wrs'),
    path('igw_json/', igw_json, name='inventory_app-igw_json'),
    path('mx_json/', mx_json, name='inventory_app-mx_json'),
    path('sigr_json/', sigr_json, name='inventory_app-sigr_json'),
    path('was_json/', was_json, name='inventory_app-was_json'),
    path('wgr_json/', wgr_json, name='inventory_app-wgr_json'),
    path('wpr_json/', wpr_json, name='inventory_app-wpr_json'),
    path('wrs_json/', wrs_json, name='inventory_app-wrs_json'),
    path('igw_form/', igw_form, name='inventory_app-igw_form'),
    path('mx_form/', mx_form, name='inventory_app-mx_form'),
    path('sigr_form/', sigr_form, name='inventory_app-sigr_form'),
    path('was_form/', was_form, name='inventory_app-was_form'),
    path('wgr_form/', wgr_form, name='inventory_app-wgr_form'),
    path('wpr_form/', wpr_form, name='inventory_app-wpr_form'),
    path('wrs_form/', wrs_form, name='inventory_app-wrs_form'),
    path('wpr_details/', views.wpr_details, name='inventory_app-wpr_details'),



]

handler500 = 'inventory_app.views.error_500'
