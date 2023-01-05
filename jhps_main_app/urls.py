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
    path('vision_mission', views.vision_mission, name='vision_mission'),
    path('awards', views.awards, name='awards'),
    path('presidential_visit', views.presidential_visit, name='presidential_visit'),
    path('SMCommittee', views.SMCommittee, name='SMCommittee'),
    
    path('campus', views.campus, name='campus'),
    path('ClassRoom', views.ClassRoom, name='ClassRoom'),
    path('Library', views.Library, name='Library'),
    path('Auditorium', views.Auditorium, name='Auditorium'),
    path('InformaryRoom', views.InformaryRoom, name='InformaryRoom'),
    path('Canteen', views.Canteen, name='Canteen'),
    path('Stationary', views.Stationary, name='Stationary'),
    path('TeacherWelfare', views.TeacherWelfare, name='TeacherWelfare'),

    path('admissions', views.admissions, name='admissions'),
    path('FeeStructure', views.FeeStructure, name='FeeStructure'),
    path('academics', views.academics, name='academics'),
    path('ELearning', views.ELearning, name='ELearning'),
    path('CurriculumSyllabus', views.CurriculumSyllabus, name='CurriculumSyllabus'),
    path('Faculty', views.Faculty, name='Faculty'),

    path('sportsCSA', views.sportsCSA, name='sportsCSA'),
    path('CSA', views.CSA, name='CSA'),
    path('ECA', views.ECA, name='ECA'),
    path('HouseAactivities', views.HouseAactivities, name='HouseAactivities'),
    path('EducationalTours', views.EducationalTours, name='EducationalTours'),

    path('careers', views.careers, name='careers'),
    path('circulars', views.circulars, name='circulars'),
    path('downloads', views.downloads, name='downloads'),
    path('transport', views.transport, name='transport'),
    path('gallery', views.gallery, name='gallery'),
    path('noticeboard', views.noticeboard, name='noticeboard'),
    path('videogallery', views.videogallery, name='videogallery'),
]