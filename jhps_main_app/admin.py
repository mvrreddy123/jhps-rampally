from django.contrib import admin
from .models import Admission_Enquiry, Student_Enquiry,Notice_Board, Refer_A_Student, About_us, Campus, Admission, Academics, Sports_CSA, Management, Faculty,Events, EventImages, Student_Events, Staff_Events, Staff_Video_Events, Student_Video_Events, Testimonials, Circulars, Press_Media, Careers, Downloads, School_Magazines, Scroll_text, ApplyJob

# Register your models here.
class Admission_EnquiryAdmin(admin.ModelAdmin):
    list_display = ('enq_name', 'mobile_No', 'email','message')
class Student_EnquiryAdmin(admin.ModelAdmin):
    list_display = ('academic_year','first_name','middle_name','last_name','date_of_birth','gender','relation','local_type','transfer_from','mobile_No','email','message','mother_name','mother_organization','mother_designation','mother_income','mother_mobile_No','mother_email','father_name','father_orgnization','father_designation','father_income','father_mobile_No','father_email','reference_name','reference_designation','reference_department','reference_company','reference_mobile_No','reference_email','remarks')
class Refer_A_StudentAdmin(admin.ModelAdmin):
    list_display = ('child_name','parent_name','mobile_No','email','referee_parent_name','referee_child_name','referee_mobile_No','referee_email','Note')
class About_usAdmin(admin.ModelAdmin):
    list_display = ('select_page','title','paragraph_data','upload_image')
class CampusAdmin(admin.ModelAdmin):
    list_display = ('select_page','title','paragraph_data','upload_image')
class AdmissionAdmin(admin.ModelAdmin):
    list_display = ('select_page','title','paragraph_data','upload_image')
class AcademicsAdmin(admin.ModelAdmin):
    list_display = ('select_page','title','paragraph_data','upload_image')
class Sports_CSAAdmin(admin.ModelAdmin):
    list_display = ('select_page','title','paragraph_data','upload_image')
class ManagementAdmin(admin.ModelAdmin):
    list_display = ('member_name','designation')
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('staff_name','staff_designation')
    
class EventImagesAdmin(admin.StackedInline):
    model = EventImages
    # list_display = ('title','paragraph_data','upload_image')
@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    inlines = [EventImagesAdmin]
 
    class Meta:
       model = Events
    # list_display = ('title','paragraph_data','upload_image')
@admin.register(EventImages)
class EventImagesAdmin(admin.ModelAdmin):
    pass
 
class Student_EventsAdmin(admin.ModelAdmin):
    list_display = ('title','date','upload_image')
class Staff_EventsAdmin(admin.ModelAdmin):
    list_display = ('title','date','upload_image')
class Staff_Video_EventsAdmin(admin.ModelAdmin):
    list_display = ('title','date','video_URL')
class Student_Video_EventsAdmin(admin.ModelAdmin):
    list_display = ('title','date','video_URL')
class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ('title','paragraph_data','upload_image')
class Notice_BoardAdmin(admin.ModelAdmin):
    list_display = ('title','paragraph_data')
class Press_MediaAdmin(admin.ModelAdmin):
    list_display = ('title','date','upload_image')
class CircularsAdmin(admin.ModelAdmin):
    list_display = ('title','date','upload_pdf')
class DownloadsAdmin(admin.ModelAdmin):
    list_display = ('title','date','upload_pdf')
class CareersAdmin(admin.ModelAdmin):
    list_display = ('title','paragraph_data')
class School_MagazinesAdmin(admin.ModelAdmin):
    list_display = ('date','upload_pdf')
class Scroll_textAdmin(admin.ModelAdmin):
    list_display = ('text',)
class ApplyJobAdmin(admin.ModelAdmin):
    list_display = ('Post_Applying_For', 'Name_of_the_Candidate', 'Residential_Address', 'Own_house_rented', 'Mother_Tongue', 'date_of_birth', 'Caste_Category_Religion', 'Email_ID', 'Telephone_No', 'Qualifications', 'Last_Worked', 'Reasons', 'Any_friends', 'Have_you_worked', 'Present_Salary', 'Expected_Salary', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'nsc1', 'nsc2', 'nsc3', 'nsc4', 'nsc5', 'nsc6', 'u1', 'u2', 'u3', 'u4', 'u5', 'u6', 'pos1', 'pos2', 'pos3', 'pos4', 'pos5', 'pos6', 'yp1', 'yp2', 'yp3', 'yp4', 'yp5', 'yp6', 'm1', 'm2', 'm3', 'm4', 'm5', 'm6', 'rc1', 'rc2',
                  'rc3', 'rc4', 'rc5', 'rc6', 'sec1', 'sec2', 'sec3', 'sec4', 'sec5', 'sec6', 'no1', 'no2', 'no3', 'no4', 'no5', 'no6', 'deg1', 'deg2', 'deg3', 'deg4', 'deg5', 'deg6', 'yow1', 'yow2', 'yow3', 'yow4', 'yow5', 'yow6', 'sal1', 'sal2', 'sal3', 'sal4', 'sal5', 'sal6', 'skill1', 'skill2', 'Sp_Name', 'Sp_DOB', 'Sp_Qul', 'Sp_Occ', 'Sp_Deg', 'Sp_Inc', 'F_Name', 'F_DOB', 'F_Qul', 'F_Occ', 'F_Deg', 'F_Inc', 'M_Name', 'M_DOB', 'M_Qul', 'M_Occ', 'M_Deg', 'M_Inc', 'C1_Name', 'C1_DOB', 'C1_St', 'C1_PSN', 'C2_Name', 'C2_DOB', 'C2_St', 'C2_PSN', 'Ref1', 'Ref2', 'upload_cv'
                )



admin.site.register(Admission_Enquiry, Admission_EnquiryAdmin)
admin.site.register(Student_Enquiry, Student_EnquiryAdmin)
admin.site.register(Refer_A_Student, Refer_A_StudentAdmin)
admin.site.register(About_us, About_usAdmin)
admin.site.register(Campus, CampusAdmin)
admin.site.register(Admission, AdmissionAdmin)
admin.site.register(Academics, AcademicsAdmin)
admin.site.register(Sports_CSA, Sports_CSAAdmin)
admin.site.register(Management, ManagementAdmin)
admin.site.register(Faculty, FacultyAdmin)
# admin.site.register(Events, EventsAdmin)
admin.site.register(Student_Events, Student_EventsAdmin)
admin.site.register(Staff_Events, Staff_EventsAdmin)
admin.site.register(Staff_Video_Events, Staff_Video_EventsAdmin)
admin.site.register(Student_Video_Events, Student_Video_EventsAdmin)
admin.site.register(Testimonials, TestimonialsAdmin)
admin.site.register(Circulars, CircularsAdmin)
admin.site.register(Press_Media, Press_MediaAdmin)
admin.site.register(Careers, CareersAdmin)
admin.site.register(Notice_Board, Notice_BoardAdmin)
admin.site.register(Downloads, DownloadsAdmin)
admin.site.register(School_Magazines, School_MagazinesAdmin)
admin.site.register(Scroll_text, Scroll_textAdmin)
admin.site.register(ApplyJob, ApplyJobAdmin)