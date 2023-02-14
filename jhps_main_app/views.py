from django.shortcuts import render
from .models import About_us, Campus, Admission, Academics, Sports_CSA, Careers, Circulars, Downloads, Management
from .forms import AdmissionEnquiryForm, ReferAStudentForm, StudentEnquiryForm, ApplyJobForm
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings
# import io
# from django.http import FileResponse
# from reportlab.pdfgen import canvas
# Create your views here.
toEmailId1 = 'mvr.9441088048@gmail.com'
def index(request):
    return render(request, 'index.html')

def aboutUs(request):
    aboutData = About_us.objects.all()
    args = {'aboutData': aboutData}
    return render(request, 'aboutus.html', args)
def vision_mission(request):
    aboutDataVM = About_us.objects.filter(select_page = 1)
    args = {'aboutDataVM': aboutDataVM}
    return render(request, 'aboutusVM.html', args)
def awards(request):
    aboutDataAw = About_us.objects.filter(select_page = 2)
    args = {'aboutDataAw': aboutDataAw}
    return render(request, 'aboutusAw.html', args)
def presidential_visit(request):
    aboutDataPV = About_us.objects.filter(select_page = 3)
    args = {'aboutDataPV': aboutDataPV}
    return render(request, 'aboutusPV.html', args)
def SMCommittee(request):
    SMCommittee = Management.objects.all()
    args = {'SMCommitteeData': SMCommittee}
    return render(request, 'SMCommittee.html', args)


def campus(request):
    campusData = Campus.objects.all()
    args = {'campusData': campusData}
    return render(request, 'campus.html', args)
def ClassRoom(request):
    ClassRoomData = Campus.objects.filter(select_page = 1 )
    args = {'ClassRoomData': ClassRoomData}
    return render(request, 'ClassRoom.html', args)
def Library(request):
    LibraryData = Campus.objects.filter(select_page = 2)
    args = {'LibraryData': LibraryData}
    return render(request, 'Library.html', args)
def Auditorium(request):
    AuditoriumData = Campus.objects.filter(select_page = 3 )
    args = {'AuditoriumData': AuditoriumData}
    return render(request, 'Auditorium.html', args)
def InformaryRoom(request):
    InformaryRoomData = Campus.objects.filter(select_page = 4 )
    args = {'InformaryRoomData': InformaryRoomData}
    return render(request, 'InformaryRoom.html', args)
def Canteen(request):
    CanteenData = Campus.objects.filter(select_page = 5)
    args = {'CanteenData': CanteenData}
    return render(request, 'Canteen.html', args)
def Stationary(request):
    StationaryData = Campus.objects.filter(select_page = 6 )
    args = {'StationaryData': StationaryData}
    return render(request, 'Stationary.html', args)
def TeacherWelfare(request):
    TeacherWelfareData = Campus.objects.filter(select_page = 7 )
    args = {'TeacherWelfareData': TeacherWelfareData}
    return render(request, 'TeacherWelfare.html', args)

def admissions(request):
    admissionsData = Admission.objects.all()
    args = {'admissionsData': admissionsData}
    return render(request, 'admissions.html', args)
def FeeStructure(request):
    return render(request, 'FeeStructure.html')

def academics(request):
    academicsData = Academics.objects.all()
    args = {'academicsData': academicsData}
    return render(request, 'academics.html', args)
def LearningProcess(request):
    LearningProcessData = Academics.objects.filter(select_page = 0 )
    args = {'LearningProcessData': LearningProcessData}
    return render(request, 'LearningProcess.html', args)
def ELearning(request):
    ELearningData = Academics.objects.filter(select_page = 1 )
    args = {'ELearningData': ELearningData}
    return render(request, 'ELearning.html', args)
def CurriculumSyllabus(request):
    CurriculumSyllabusData = Academics.objects.filter(select_page = 2 )
    args = {'CurriculumSyllabusData': CurriculumSyllabusData}
    return render(request, 'CurriculumSyllabus.html', args)
def SchoolTimings(request):
    return render(request, 'timings.html')

def Faculty(request):
    return render(request, 'Faculty.html')

def sportsCSA(request):
    sportsCSAData = Sports_CSA.objects.all()
    args = {'sportsCSAData': sportsCSAData}
    return render(request, 'sportsCSA.html', args)
def CSA(request):
    CSAData = Sports_CSA.objects.filter(select_page = 1 )
    args = {'CSAData': CSAData}
    return render(request, 'csa.html', args)
def ECA(request):
    ECAData = Sports_CSA.objects.filter(select_page = 2 )
    args = {'ECAData': ECAData}
    return render(request, 'eca.html', args)
def HouseAactivities(request):
    HOUSEACTIVITIESData = Sports_CSA.objects.filter(select_page = 3 )
    args = {'HOUSEACTIVITIESData': HOUSEACTIVITIESData}
    return render(request, 'HOUSEACTIVITIES.html', args)
def EducationalTours(request):
    EDUCATIONAL_TOURSData = Sports_CSA.objects.filter(select_page = 4 )
    args = {'EDUCATIONAL_TOURSData': EDUCATIONAL_TOURSData}
    return render(request, 'EducationalTours.html', args)

def careers(request):
    career = Careers.objects.all()
    args = {'career': career}
    return render(request, 'careers.html', args)

def circulars(request):
    circular = Circulars.objects.all()
    args = {'circular': circular}
    return render(request, 'circular.html', args)

def downloads(request):
    download = Downloads.objects.all()
    args = {'download': download}
    return render(request, 'downloads.html', args)

def transport(request):
    # download = Downloads.objects.all()
    # args = {'download': download}
    return render(request, 'transport.html')

def gallery(request):
    # download = Downloads.objects.all()
    # args = {'download': download}
    return render(request, 'imageGall.html')
def videogallery(request):
    # download = Downloads.objects.all()
    # args = {'download': download}
    return render(request, 'videoGall.html')
def noticeboard(request):
    # download = Downloads.objects.all()
    # args = {'download': download}
    return render(request, 'noticeboard.html')
def events(request):
    # download = Downloads.objects.all()
    # args = {'download': download}
    return render(request, 'events.html')

# start Forms
def contactUs(request):
    submitted = False
    if request.method == 'POST':
        form = AdmissionEnquiryForm(request.POST)
        if form.is_valid():
            enq_name = form['enq_name'].value()
            mobile_No = form['mobile_No'].value()
            email = form['email'].value()
            message = form['message'].value()
        
            send_mail(
                f'Enquiry from: {enq_name}, phone: {mobile_No}',
                f'Enquiry from: {enq_name}, phone: {mobile_No}, \n{message}',
                settings.EMAIL_HOST_USER,
                [toEmailId1,],
            )
            form.save()
            return HttpResponseRedirect('?submitted=True')
    else:
        form = AdmissionEnquiryForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'contactUs.html', {'form':form, 'submitted':submitted })


def ReferAStudent(request):
    # return HttpResponse('Hi JHPS')
    submitted = False
    if request.method == 'POST':
        form = ReferAStudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('?submitted=True')
    else:
        form = ReferAStudentForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'ReferStudentForm.html', {'form':form, 'submitted':submitted })
    

def StudentEnquiry(request):
    submitted = False
    if request.method == 'POST':
        form = StudentEnquiryForm(request.POST)
        if form.is_valid():
            academic_year = form['academic_year'].value() 
            first_name = form['first_name'].value() 
            middle_name = form['middle_name'].value() 
            last_name = form['last_name'].value() 
            date_of_birth = form['date_of_birth'].value() 
            gender = form['gender'].value() 
            relation = form['relation'].value() 
            local_type = form['local_type'].value() 
            transfer_from = form['transfer_from'].value() 
            mobile_No = form['mobile_No'].value() 
            email = form['email'].value() 
            message = form['message'].value() 
            mother_name = form['mother_name'].value() 
            mother_organization = form['mother_organization'].value() 
            mother_designation = form['mother_designation'].value() 
            mother_income = form['mother_income'].value() 
            mother_mobile_No = form['mother_mobile_No'].value()
            mother_email = form['mother_email'].value() 
            father_name = form['father_name'].value() 
            father_orgnization = form['father_orgnization'].value() 
            father_designation = form['father_designation'].value() 
            father_income = form['father_income'].value() 
            father_mobile_No = form['father_mobile_No'].value() 
            father_email = form['father_email'].value() 
            reference_name = form['reference_name'].value() 
            reference_designation = form['reference_designation'].value() 
            reference_department = form['reference_department'].value() 
            reference_company = form['reference_company'].value() 
            reference_mobile_No = form['reference_mobile_No'].value() 
            reference_email = form['reference_email'].value() 
            remarks = form['remarks'].value() 
        
            send_mail(
                f'Enquiry from {mother_name} phone {mobile_No}',
                f"""
                Academic Year : {academic_year},
                First Name : {first_name},
                Middle Name : {middle_name},
                Last Name : {last_name},
                Date_of_Birth : {date_of_birth},
                gender : {gender},
                relation : {relation},
                local_type : {local_type},
                transfer_from : {transfer_from},
                mobile_No : {mobile_No},
                email : {email},
                message : {message},
                mother_name : {mother_name},
                mother_organization : {mother_organization},
                mother_designation : {mother_designation},
                mother_income : {mother_income},
                mother_mobile_No : {mother_mobile_No},
                mother_email : {mother_email},
                father_name : {father_name},
                father_orgnization : {father_orgnization},
                father_designation : {father_designation},
                father_income : {father_income},
                father_mobile_No : {father_mobile_No},
                father_email : {father_email},
                reference_name : {reference_name},
                reference_designation : {reference_designation},
                reference_department : {reference_department},
                reference_company : {reference_company},
                reference_mobile_No : {reference_mobile_No},
                reference_email : {reference_email},
                remarks : {remarks},
                """,
                settings.EMAIL_HOST_USER,
                [toEmailId1,],
            )
            form.save()
            return HttpResponseRedirect('?submitted=True')
    else:
        form = StudentEnquiryForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'StudentEnquiryForm.html', {'form':form, 'submitted':submitted })


def Applyjob(request):
    submitted = False
    if request.method == 'POST':
        form = ApplyJobForm(request.POST)
        if form.is_valid():
            Post_Applying_For = form['Post_Applying_For'].value()
            Name_of_the_Candidate = form['Name_of_the_Candidate'].value()
            Residential_Address = form['Residential_Address'].value()
            Own_house_rented = form['Own_house_rented'].value()
            Mother_Tongue = form['Mother_Tongue'].value()
            date_of_birth = form['date_of_birth'].value()
            Caste_Category_Religion = form['Caste_Category_Religion'].value()
            Telephone_No = form['Telephone_No'].value()
            Email_ID = form['Email_ID'].value()
            Qualifications = form['Qualifications'].value()
            Last_Worked  = form['Last_Worked'].value()
            Reasons = form['Reasons'].value()
            Any_friends = form['Any_friends'].value()
            Have_you_worked  = form['Have_you_worked'].value()
            Present_Salary = form['Present_Salary'].value()
            Expected_Salary = form['Expected_Salary'].value()
            c1 = form['c1'].value()
            c2 = form['c2'].value()
            c3 = form['c3'].value()
            c4 = form['c4'].value()
            c5 = form['c5'].value()
            c6 = form['c6'].value()
            nsc1 = form['nsc1'].value()
            nsc2 = form['nsc2'].value()
            nsc3 = form['nsc3'].value()
            nsc4 = form['nsc4'].value()
            nsc5 = form['nsc5'].value()
            nsc6 = form['nsc6'].value()
            u1 = form['u1'].value()
            u2 = form['u2'].value()
            u3 = form['u3'].value()
            u4 = form['u4'].value()
            u5 = form['u5'].value()
            u6 = form['u6'].value()
            pos1 = form['pos1'].value()
            pos2 = form['pos2'].value()
            pos3 = form['pos3'].value()
            pos4 = form['pos4'].value()
            pos5 = form['pos5'].value()
            pos6 = form['pos6'].value()
            yp1 = form['yp1'].value()
            yp2 = form['yp2'].value()
            yp3 = form['yp3'].value()
            yp4 = form['yp4'].value()
            yp5 = form['yp5'].value()
            yp6 = form['yp6'].value()
            m1 = form['m1'].value()
            m2 = form['m2'].value()
            m3 = form['m3'].value()
            m4 = form['m4'].value()
            m5 = form['m5'].value()
            m6 = form['m6'].value()
            rc1 = form['rc1'].value()
            rc2 = form['rc2'].value()
            rc3 = form['rc3'].value()
            rc4 = form['rc4'].value()
            rc5 = form['rc5'].value()
            rc6 = form['rc6'].value()
            sec1 = form['sec1'].value()
            sec2 = form['sec2'].value()
            sec3 = form['sec3'].value()
            sec4 = form['sec4'].value()
            sec5 = form['sec5'].value()
            sec6 = form['sec6'].value()
            no1 = form['no1'].value()
            no2 = form['no2'].value()
            no3 = form['no3'].value()
            no4 = form['no4'].value()
            no5 = form['no5'].value()
            no6 = form['no6'].value()
            deg1 = form['deg1'].value()
            deg2 = form['deg2'].value()
            deg3 = form['deg3'].value()
            deg4 = form['deg4'].value()
            deg5 = form['deg5'].value()
            deg6 = form['deg6'].value()
            yow1 = form['yow1'].value()
            yow2 = form['yow2'].value()
            yow3 = form['yow3'].value()
            yow4 = form['yow4'].value()
            yow5 = form['yow5'].value()
            yow6 = form['yow6'].value()
            sal1 = form['sal1'].value()
            sal2 = form['sal2'].value()
            sal3 = form['sal3'].value()
            sal4 = form['sal4'].value()
            sal5 = form['sal5'].value()
            sal6 = form['sal6'].value()
            skill1 = form['skill1'].value()
            skill2 = form['skill2'].value()
            Sp_Name = form['Sp_Name'].value()
            Sp_DOB = form['Sp_DOB'].value()
            Sp_Qul = form['Sp_Qul'].value()
            Sp_Occ = form['Sp_Occ'].value()
            Sp_Deg = form['Sp_Deg'].value()
            Sp_Inc = form['Sp_Inc'].value()
            F_Name = form['F_Name'].value()
            F_DOB = form['F_DOB'].value()
            F_Qul = form['F_Qul'].value()
            F_Occ = form['F_Occ'].value()
            F_Deg = form['F_Deg'].value()
            F_Inc = form['F_Inc'].value()
            M_Name = form['M_Name'].value()
            M_DOB = form['M_DOB'].value()
            M_Qul = form['M_Qul'].value()
            M_Occ = form['M_Occ'].value()
            M_Deg = form['M_Deg'].value()
            M_Inc = form['M_Inc'].value()
            C1_Name = form['C1_Name'].value()
            C1_DOB = form['C1_DOB'].value()
            C1_St = form['C1_St'].value()
            C1_PSN = form['C1_PSN'].value()
            C2_Name = form['C2_Name'].value()
            C2_DOB = form['C2_DOB'].value()
            C2_St = form['C2_St'].value()
            C2_PSN = form['C2_PSN'].value()
            Ref1 = form['Ref1'].value()
            Ref2 = form['Ref2'].value()
            send_mail(
                f'Application for Job from: {Name_of_the_Candidate}, Phone: {Telephone_No}',
                f'''
                
                Post_Applying_For : {Post_Applying_For},
                Name_of_the_Candidate : {Name_of_the_Candidate},
                Residential_Address : {Residential_Address},
                Own_house_rented : {Own_house_rented},
                Mother_Tongue : {Mother_Tongue},
                date_of_birth : {date_of_birth},
                Caste_Category_Religion : {Caste_Category_Religion},
                Telephone_No : {Telephone_No},
                Email_ID : {Email_ID},
                Qualifications : {Qualifications},
                Last_Worked  : {Last_Worked},
                Reasons : {Reasons},
                Any_friends : {Any_friends},
                Have_you_worked  : {Have_you_worked},
                Present_Salary : {Present_Salary},
                Expected_Salary : {Expected_Salary}
                ''',
                settings.EMAIL_HOST_USER,
                [toEmailId1,],
            )
            form.save()
            return HttpResponseRedirect('?submitted=True')
    else:
        form = ApplyJobForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'applyjob.html', {'form':form, 'submitted':submitted })
# end Forms