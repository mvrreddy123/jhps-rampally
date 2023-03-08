from django.urls import path
from  . import views



app_name = 'jhps_main_app'
urlpatterns = [
    path("", views.index),
    path('contactUs/', views.contactUs, name='contactUs'),
    path('StudentEnquiryForm/', views.StudentEnquiry, name='StudentEnquiry'),
    path('ApplyJob/', views.Applyjob, name='Applyjob'),
    # Pages
    path('about', views.aboutUs, name='aboutUs'),
    path('vision_mission', views.vision_mission, name='vision_mission'),
    path('awards', views.awards, name='awards'),
    path('SMCommittee', views.SMCommittee, name='SMCommittee'),
    
    path('campus', views.campus, name='campus'),
    path('ClassRoom', views.ClassRoom, name='ClassRoom'),
    path('Laboratories', views.Laboratories, name='Laboratories'),
    path('Auditorium', views.Auditorium, name='Auditorium'),
    path('Library', views.Library, name='Library'),
    path('Safety', views.Safety, name='Safety'),
    path('InformaryRoom', views.InformaryRoom, name='InformaryRoom'),
    path('Canteen', views.Canteen, name='Canteen'),
    path('TeacherWelfare', views.TeacherWelfare, name='TeacherWelfare'),

    path('admissions', views.admissions, name='admissions'),
    path('FeeStructure', views.FeeStructure, name='FeeStructure'),

    path('academics', views.academics, name='academics'),
    path('LearningProcess', views.LearningProcess, name='LearningProcess'),
    path('ELearning', views.ELearning, name='ELearning'),
    path('CurriculumSyllabus', views.CurriculumSyllabus, name='CurriculumSyllabus'),
    path('SchoolTimings', views.SchoolTimings, name='SchoolTimings'),
    path('Faculty', views.Faculty, name='Faculty'),
 
    path('sportsCSA', views.sportsCSA, name='sportsCSA'),
    path('CarromBoard', views.CarromBoard, name='CarromBoard'),
    path('Chess', views.Chess, name='Chess'),
    path('Badminton', views.Badminton, name='Badminton'),
    path('TableTennis', views.TableTennis, name='TableTennis'),
    path('FootBall', views.FootBall, name='FootBall'),
    path('Cricket', views.Cricket, name='Cricket'),
    path('ThrowBall', views.ThrowBall, name='ThrowBall'),
    path('Tennis', views.Tennis, name='Tennis'),
    path('VolleyBall', views.VolleyBall, name='VolleyBall'),
    path('Kabaddi', views.Kabaddi, name='Kabaddi'),
    path('KoKo', views.KoKo, name='KoKo'),
    path('CSA', views.CSA, name='CSA'),
    path('ECA', views.ECA, name='ECA'),
    path('HouseAactivities', views.HouseAactivities, name='HouseAactivities'),
    path('EducationalTours', views.EducationalTours, name='EducationalTours'),

    path('careers', views.careers, name='careers'),
    path('circulars', views.circulars, name='circulars'),
    path('downloads', views.downloads, name='downloads'),
    path('transport', views.transport, name='transport'),
    path('gallery', views.gallery, name='gallery'),
    path('<int:id>/', views.galleryDetail, name='galleryDetail'),
    path('noticeboard', views.noticeboard, name='noticeboard'),
    path('events', views.events, name='events'),
    path('<int:id>/', views.eventDetail, name='eventDetail'),
    path('videogallery', views.videogallery, name='videogallery'),
    
    path('uc', views.uc, name='uc'),
]