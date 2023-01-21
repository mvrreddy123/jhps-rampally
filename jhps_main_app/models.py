from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from phonenumber_field.modelfields import PhoneNumberField
from .validators import validate_file_size
# Create your models here.


class Admission_Enquiry (models.Model):
    enq_name = models.CharField(max_length=255)
    mobile_No = PhoneNumberField()
    email = models.EmailField(max_length=255)
    message = models.CharField (null=True, blank=True, max_length=255)

class Student_Enquiry (models.Model):
    year1 = 0
    year2 = 1
    YEAR_CHOICES = [(year1, '2022-23'), (year2, '2023-24')]
    academic_year = models.IntegerField(null=True, blank=True, choices=YEAR_CHOICES)
    first_name = models.CharField(null=True, blank=True, max_length=100)
    middle_name = models.CharField(null=True, blank=True, max_length=100)
    last_name = models.CharField(null=True, blank=True, max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    GENDER_MALE = 0
    GENDER_FEMALE = 1
    GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female')]
    gender = models.IntegerField(null=True, blank=True, choices=GENDER_CHOICES)
    ch1 = 0
    ch2 = 1
    REL_CHOICES = [(ch1, 'FATHER'), (ch2, 'MOTHER')]
    relation = models.IntegerField(null=True, blank=True, choices=REL_CHOICES)
    L1 = 0
    L2 = 1 
    LOCAL_CHOICES = [(L1, 'Local'), (L2, 'Non-Local')]
    local_type = models.IntegerField(null=True, blank=True, choices=LOCAL_CHOICES)
    transfer_from = models.CharField(null=True, blank=True, max_length=150)
    mobile_No = PhoneNumberField(null=True, blank=True, max_length=50)
    email = models.EmailField(null=True, blank=True, max_length=150)
    message = models.TextField(null=True, blank=True, max_length=500)
    mother_name = models.CharField(null=True, blank=True, max_length=150)
    mother_organization = models.CharField(null=True, blank=True, max_length=150)
    mother_designation = models.CharField(null=True, blank=True, max_length=50)
    mother_income = models.CharField(null=True, blank=True, max_length=12)
    mother_mobile_No = PhoneNumberField(null=True, blank=True, max_length=50)
    mother_email = models.EmailField(null=True, blank=True, max_length=150)
    father_name = models.CharField(null=True, blank=True, max_length=150)
    father_orgnization = models.CharField(null=True, blank=True, max_length=150)
    father_designation = models.CharField(null=True, blank=True, max_length=50)
    father_income = models.CharField(null=True, blank=True, max_length=12)
    father_mobile_No = PhoneNumberField(null=True, blank=True, max_length=50)
    father_email = models.EmailField(null=True, blank=True, max_length=150)
    reference_name = models.CharField(null=True, blank=True, max_length=150)
    reference_designation = models.CharField(null=True, blank=True, max_length=50)
    reference_department = models.CharField(null=True, blank=True, max_length=50)
    reference_company = models.CharField(null=True, blank=True, max_length=50)
    reference_mobile_No = PhoneNumberField(null=True, blank=True, max_length=50)
    reference_email = models.EmailField(null=True, blank=True, max_length=150)
    remarks = models.TextField(null=True, blank=True, max_length=500)



class ApplyJob (models.Model):
   
    Post_Applying_For = models.CharField(max_length=150)
    Name_of_the_Candidate = models.CharField(max_length=100)
    Residential_Address = models.CharField(max_length=255)
    Own_house_rented = models.CharField(max_length=50)
    Mother_Tongue = models.CharField(max_length=25)
    date_of_birth = models.DateField()
    g1, g2, g3, g4, g5, g6 = 0,1,2,3,4,5
    CATEGORY_CHOICES = [(g1, 'SC'), (g2, 'ST'), (g3, 'BC'), (g4, 'OBC'), (g5, 'General'), (g6, 'Others')]
    Caste_Category_Religion = models.IntegerField(choices=CATEGORY_CHOICES)
    Email_ID = models.EmailField(max_length=150)
    Telephone_No = PhoneNumberField()
    Qualifications = models.CharField(max_length=150)
    Last_Worked  = models.CharField(max_length=150)
    Reasons = models.CharField(null=True, blank=True, max_length=150)
    Any_friends = models.CharField(null=True, blank=True, max_length=50)
    Have_you_worked  = models.CharField(null=True, blank=True, max_length=12)
    Present_Salary = models.CharField(max_length=10)
    Expected_Salary = models.CharField(null=True, blank=True, max_length=10)
    c1 = models.CharField(null=True, blank=True, max_length=55) 
    c2 = models.CharField(null=True, blank=True, max_length=55) 
    c3 = models.CharField(null=True, blank=True, max_length=55) 
    c4 = models.CharField(null=True, blank=True, max_length=55) 
    c5 = models.CharField(null=True, blank=True, max_length=55) 
    c6 = models.CharField(null=True, blank=True, max_length=55) 

    nsc1 = models.CharField(null=True, blank=True, max_length=100) 
    nsc2 = models.CharField(null=True, blank=True, max_length=100) 
    nsc3 = models.CharField(null=True, blank=True, max_length=100) 
    nsc4 = models.CharField(null=True, blank=True, max_length=100) 
    nsc5 = models.CharField(null=True, blank=True, max_length=100) 
    nsc6 = models.CharField(null=True, blank=True, max_length=100) 

    u1 = models.CharField(null=True, blank=True, max_length=100) 
    u2 = models.CharField(null=True, blank=True, max_length=100) 
    u3 = models.CharField(null=True, blank=True, max_length=100) 
    u4 = models.CharField(null=True, blank=True, max_length=100) 
    u5 = models.CharField(null=True, blank=True, max_length=100) 
    u6 = models.CharField(null=True, blank=True, max_length=100) 

    pos1 = models.CharField(null=True, blank=True, max_length=50) 
    pos2 = models.CharField(null=True, blank=True, max_length=50) 
    pos3 = models.CharField(null=True, blank=True, max_length=50) 
    pos4 = models.CharField(null=True, blank=True, max_length=50) 
    pos5 = models.CharField(null=True, blank=True, max_length=50) 
    pos6 = models.CharField(null=True, blank=True, max_length=50) 

    yp1 = models.CharField(null=True, blank=True, max_length=10) 
    yp2 = models.CharField(null=True, blank=True, max_length=10) 
    yp3 = models.CharField(null=True, blank=True, max_length=10) 
    yp4 = models.CharField(null=True, blank=True, max_length=10) 
    yp5 = models.CharField(null=True, blank=True, max_length=10) 
    yp6 = models.CharField(null=True, blank=True, max_length=10)

    m1 = models.CharField(null=True, blank=True, max_length=10) 
    m2 = models.CharField(null=True, blank=True, max_length=10) 
    m3 = models.CharField(null=True, blank=True, max_length=10) 
    m4 = models.CharField(null=True, blank=True, max_length=10) 
    m5 = models.CharField(null=True, blank=True, max_length=10) 
    m6 = models.CharField(null=True, blank=True, max_length=10)

    rc1 = models.CharField(null=True, blank=True, max_length=10) 
    rc2 = models.CharField(null=True, blank=True, max_length=10) 
    rc3 = models.CharField(null=True, blank=True, max_length=10) 
    rc4 = models.CharField(null=True, blank=True, max_length=10) 
    rc5 = models.CharField(null=True, blank=True, max_length=10) 
    rc6 = models.CharField(null=True, blank=True, max_length=10)

    sec1 = models.CharField(null=True, blank=True, max_length=10) 
    sec2 = models.CharField(null=True, blank=True, max_length=10) 
    sec3 = models.CharField(null=True, blank=True, max_length=10) 
    sec4 = models.CharField(null=True, blank=True, max_length=10) 
    sec5 = models.CharField(null=True, blank=True, max_length=10) 
    sec6 = models.CharField(null=True, blank=True, max_length=10)

    no1 = models.CharField(null=True, blank=True, max_length=100) 
    no2 = models.CharField(null=True, blank=True, max_length=100) 
    no3 = models.CharField(null=True, blank=True, max_length=100) 
    no4 = models.CharField(null=True, blank=True, max_length=100) 
    no5 = models.CharField(null=True, blank=True, max_length=100) 
    no6 = models.CharField(null=True, blank=True, max_length=100)

    deg1 = models.CharField(null=True, blank=True, max_length=100) 
    deg2 = models.CharField(null=True, blank=True, max_length=100) 
    deg3 = models.CharField(null=True, blank=True, max_length=100) 
    deg4 = models.CharField(null=True, blank=True, max_length=100) 
    deg5 = models.CharField(null=True, blank=True, max_length=100) 
    deg6 = models.CharField(null=True, blank=True, max_length=100)

    yow1 = models.CharField(null=True, blank=True, max_length=10) 
    yow2 = models.CharField(null=True, blank=True, max_length=10) 
    yow3 = models.CharField(null=True, blank=True, max_length=10) 
    yow4 = models.CharField(null=True, blank=True, max_length=10) 
    yow5 = models.CharField(null=True, blank=True, max_length=10) 
    yow6 = models.CharField(null=True, blank=True, max_length=10)

    sal1 = models.CharField(null=True, blank=True, max_length=10) 
    sal2 = models.CharField(null=True, blank=True, max_length=10) 
    sal3 = models.CharField(null=True, blank=True, max_length=10) 
    sal4 = models.CharField(null=True, blank=True, max_length=10) 
    sal5 = models.CharField(null=True, blank=True, max_length=10) 
    sal6 = models.CharField(null=True, blank=True, max_length=10)

    skill1 = models.CharField(null=True, blank=True, max_length=100)
    skill2 = models.CharField(null=True, blank=True, max_length=100)

    Sp_Name = models.CharField(null=True, blank=True, max_length=100)
    Sp_DOB = models.DateField()
    Sp_Qul = models.CharField(null=True, blank=True, max_length=50)
    Sp_Occ = models.CharField(null=True, blank=True, max_length=50)
    Sp_Deg = models.CharField(null=True, blank=True, max_length=50)
    Sp_Inc = models.CharField(null=True, blank=True, max_length=10)

    F_Name = models.CharField(null=True, blank=True, max_length=100)
    F_DOB = models.DateField()
    F_Qul = models.CharField(null=True, blank=True, max_length=50)
    F_Occ = models.CharField(null=True, blank=True, max_length=50)
    F_Deg = models.CharField(null=True, blank=True, max_length=50)
    F_Inc = models.CharField(null=True, blank=True, max_length=10)

    M_Name = models.CharField(null=True, blank=True, max_length=100)
    M_DOB = models.DateField()
    M_Qul = models.CharField(null=True, blank=True, max_length=50)
    M_Occ = models.CharField(null=True, blank=True, max_length=50)
    M_Deg = models.CharField(null=True, blank=True, max_length=50)
    M_Inc = models.CharField(null=True, blank=True, max_length=10)

    C1_Name = models.CharField(null=True, blank=True, max_length=100)
    C1_DOB = models.DateField()
    C1_St = models.CharField(null=True, blank=True, max_length=50)
    C1_PSN = models.CharField(null=True, blank=True, max_length=50)

    C2_Name = models.CharField(null=True, blank=True, max_length=100)
    C2_DOB = models.DateField()
    C2_St = models.CharField(null=True, blank=True, max_length=50)
    C2_PSN = models.CharField(null=True, blank=True, max_length=50)
    
    Ref1 = models.CharField(null=True, blank=True, max_length=255)
    Ref2 = models.CharField(null=True, blank=True, max_length=255)
    upload_cv = models.FileField(upload_to='cv/', validators=[validate_file_size]) 



class Refer_A_Student (models.Model):
    child_name = models.CharField(max_length=100)
    parent_name = models.CharField(max_length=100)
    mobile_No = PhoneNumberField(max_length=150)
    email = models.EmailField(null=True, blank=True, max_length=150)
    referee_parent_name = models.CharField(max_length=100)
    referee_child_name = models.CharField(max_length=100)
    referee_mobile_No = PhoneNumberField()
    referee_email = models.EmailField(null=True, blank=True, max_length=150)
    Note = models.TextField(null=True, blank=True, max_length=255)

        
class About_us (models.Model):
    p1, p2, p3, p4 = 0, 1, 2, 3
    ABOUT_CHOICES = [(p1, 'About Us'), (p2, 'Vision & Mission'), (p3, 'Awards'), (p4, 'Presidential Visit')]
    select_page = models.IntegerField(choices=ABOUT_CHOICES)
    title = models.CharField(null=True, blank=True, max_length=255)
    paragraph_data = RichTextField()
    upload_image = models.ImageField(null=True, blank=True, upload_to='about_images/') 

class Campus (models.Model):
    p1, p2, p3, p4, p5, p6, p7, p8 = 0, 1, 2, 3, 4, 5, 6, 7
    CAMPUS_CHOICES = [(p1, 'Campus'), (p2, 'Class Rooms'), (p3, 'Library'), (p4, 'Auditorium'), (p5, 'Informary Room'), (p6, 'Canteen'), (p7, 'Stationary'), (p8, 'Teacher Welfare')]
    select_page = models.IntegerField(choices=CAMPUS_CHOICES)
    title = models.CharField(null=True, blank=True, max_length=255)
    paragraph_data = RichTextField()
    upload_image = models.ImageField(null=True, blank=True, upload_to='campus_images/') 

 
class Admission (models.Model):
    p1, p2 = 0, 1
    ADMISSION_CHOICES = [(p1, 'Admission Policy and Procedure'), (p2, 'Fee Structure')]
    select_page = models.IntegerField(choices=ADMISSION_CHOICES)
    title = models.CharField(null=True, blank=True, max_length=255)
    paragraph_data = RichTextField()
    upload_image = models.ImageField(null=True, blank=True, upload_to='admission_images/') 

class Academics (models.Model):
    p1, p2, p3 = 0, 1, 2
    ACADEMICS_CHOICES = [(p1, 'Class Room Learning'), (p2, 'E-Learning'), (p3, 'Curriculum Syllabus')]
    select_page = models.IntegerField(choices=ACADEMICS_CHOICES)
    title = models.CharField(null=True, blank=True, max_length=255)
    paragraph_data = RichTextField()
    upload_image = models.ImageField(null=True, blank=True, upload_to='academics_images/') 

class Sports_CSA (models.Model):
    p1, p2, p3, p4, p5 = 0, 1, 2, 3, 4
    SPORTS_CHOICES = [(p1, 'SPORTS'), (p2, 'CSA'), (p3, 'ECA'), (p4, 'HOUSE ACTIVITIES'), (p5, 'EDUCATIONAL TOURS')]
    select_page = models.IntegerField(choices=SPORTS_CHOICES)
    title = models.CharField(null=True, blank=True, max_length=255)
    paragraph_data = RichTextField()
    upload_image = models.ImageField(null=True, blank=True, upload_to='sports_images/') 

class Management (models.Model):
    member_name = models.CharField(max_length=150)
    designation = models.CharField(max_length=150)
    
class Faculty (models.Model):
    staff_name = models.CharField(max_length=150)
    staff_designation = models.CharField(max_length=150)

class Events (models.Model):
    title = models.CharField(null=True, blank=True, max_length=255)
    paragraph_data = RichTextField(null=True, blank=True)
    upload_image = models.ImageField(null=True, blank=True, upload_to='events_images/') 

class Student_Events (models.Model):
    title = models.CharField(null=True, blank=True, max_length=255)
    date = models.DateField()
    upload_image = models.ImageField(null=True, blank=True, upload_to='student_images/') 

class Staff_Events (models.Model):
    title = models.CharField(null=True, blank=True, max_length=255)
    date = models.DateField()
    upload_image = models.ImageField(null=True, blank=True, upload_to='staff_images/') 

class Student_Video_Events (models.Model):
    title = models.CharField(null=True, blank=True, max_length=255)
    date = models.DateField()
    video_URL = models.URLField()

class Staff_Video_Events (models.Model):
    title = models.CharField(null=True, blank=True, max_length=255)
    date = models.DateField()
    video_URL = models.URLField()

class Testimonials (models.Model):
    title = models.CharField(null=True, blank=True, max_length=255)
    paragraph_data = RichTextField()
    upload_image = models.ImageField(null=True, blank=True, upload_to='testimonials_images/') 

class Notice_Board (models.Model):
    title = models.CharField(null=True, blank=True, max_length=255)
    paragraph_data = RichTextField()

class Press_Media (models.Model):
    title = models.CharField(null=True, blank=True, max_length=255)
    date = models.DateField()
    upload_image = models.ImageField(null=True, blank=True, upload_to='press_images/') 

class Circulars (models.Model):
    title = models.CharField(null=True, blank=True, max_length=255)
    date = models.DateField()
    upload_pdf = models.FileField(upload_to='circulars_pdf/') 

class Downloads (models.Model):
    title = models.CharField(null=True, blank=True, max_length=255)
    date = models.DateField()
    upload_pdf = models.FileField(upload_to='downloads_pdf/') 

class Careers (models.Model):
    title = models.CharField(null=True, blank=True, max_length=255)
    paragraph_data = RichTextField()

class School_Magazines (models.Model):
    date = models.DateField()
    upload_pdf = models.FileField(upload_to='Magazines_pdf/') 

class Scroll_text (models.Model):
    text = models.TextField()

    
