from django.urls import path
from .views import skaneeri_qr, skaneerimise_logi, eksport_csv, eksport_pdf
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('tooted/', views.tooted, name='tooted'),
    path('skaneeri/', views.qr_scan, name='qr_scan'),
    path('eksport_csv/', eksport_csv, name='eksport_csv'),
    path('eksport_pdf/', eksport_pdf, name='eksport_pdf'),
    path('api/skaneeri_qr/<str:qr_kood>/', skaneeri_qr, name='skaneeri_qr'),
    path('skaneerimise_logi/', skaneerimise_logi, name='skaneerimise_logi'),
    path('api/skaneeri_qr/<str:qr_kood>/', skaneeri_qr, name='skaneeri_qr'),
]
