from django.shortcuts import render
from .models import About_us, Campus, Admission, Academics, Sports_CSA, Careers, Circulars, Downloads, Management
from .forms import AdmissionEnquiryForm, ReferAStudentForm, StudentEnquiryForm, ApplyJobForm
from django.http import HttpResponseRedirect
# Create your views here.

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
def ELearning(request):
    ELearningData = Academics.objects.filter(select_page = 1 )
    args = {'ELearningData': ELearningData}
    return render(request, 'ELearning.html', args)
def CurriculumSyllabus(request):
    CurriculumSyllabusData = Academics.objects.filter(select_page = 2 )
    args = {'CurriculumSyllabusData': CurriculumSyllabusData}
    return render(request, 'CurriculumSyllabus.html', args)
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

# start Forms
def contactUs(request):
    # return HttpResponse('Hi JHPS')
    submitted = False
    if request.method == 'POST':
        form = AdmissionEnquiryForm(request.POST)
        if form.is_valid():
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
    # return HttpResponse('Hi JHPS')
    submitted = False
    if request.method == 'POST':
        form = StudentEnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('?submitted=True')
    else:
        form = StudentEnquiryForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'StudentEnquiryForm.html', {'form':form, 'submitted':submitted })


def Applyjob(request):
    # return HttpResponse('Hi JHPS')
    submitted = False
    if request.method == 'POST':
        form = ApplyJobForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('?submitted=True')
    else:
        form = ApplyJobForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'applyjob.html', {'form':form, 'submitted':submitted })
# end Forms