from django.shortcuts import render
from .models import About_us, Campus, Admission, Academics, Sports_CSA, Careers, Circulars, Downloads
from .forms import AdmissionEnquiryForm, ReferAStudentForm, StudentEnquiryForm, ApplyJobForm
from django.http import HttpResponseRedirect
# Create your views here.

def index(request):
    return render(request, 'index.html')

def aboutUs(request):
    aboutData = About_us.objects.all()
    args = {'aboutData': aboutData}
    return render(request, 'aboutus.html', args)

def campus(request):
    campusData = Campus.objects.all()
    args = {'campusData': campusData}
    return render(request, 'campus.html', args)

def admissions(request):
    admissionsData = Admission.objects.all()
    args = {'admissionsData': admissionsData}
    return render(request, 'admissions.html', args)

def academics(request):
    academicsData = Academics.objects.all()
    args = {'academicsData': academicsData}
    return render(request, 'academics.html', args)

def sportsCSA(request):
    sportsCSAData = Sports_CSA.objects.all()
    args = {'sportsCSAData': sportsCSAData}
    return render(request, 'sportsCSA.html', args)

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