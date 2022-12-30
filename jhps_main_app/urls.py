from django.urls import path
from  . import views


app_name = 'jhps_main_app'
urlpatterns = [
    path("", views.index),
    path('contactUs/', views.contactUs, name='contactUs'),
    path('refer/', views.ReferAStudent, name='ReferAStudent'),
    path('StudentEnquiryForm/', views.StudentEnquiry, name='StudentEnquiry'),
    path('ApplyJob/', views.Applyjob, name='Applyjob'),
    # Pages
    path('about', views.aboutUs, name='aboutUs'),
    path('campus', views.campus, name='campus'),
    path('admissions', views.admissions, name='admissions'),
    path('academics', views.academics, name='academics'),
    path('sportsCSA', views.sportsCSA, name='sportsCSA'),
    path('careers', views.careers, name='careers'),
    path('circulars', views.circulars, name='circulars'),
    path('downloads', views.downloads, name='downloads'),
    path('transport', views.transport, name='transport'),
]