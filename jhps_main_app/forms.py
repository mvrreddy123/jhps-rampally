from django import forms
from django.forms import ModelForm
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from .models import Admission_Enquiry, Refer_A_Student, Student_Enquiry, ApplyJob


class AdmissionEnquiryForm(ModelForm):
    mobile_No =  PhoneNumberField(

        widget = PhoneNumberPrefixWidget(initial="IN", attrs={'class': 'form-control mvrdd', 'placeholder': 'Phone Number*'}),
        
    )
    class Meta:
        model = Admission_Enquiry
        # fields = "__all__"
        fields = ('enq_name', 'mobile_No', 'email', 'message')
        labels = {
            'enq_name': '',
            'mobile_No': '',
            'email': '',
            'message': ''
        }
        widgets = {
            'enq_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Parent Name*'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email ID*'}),
            'message': forms.Textarea(attrs={'class': 'form-control txt-ara', 'placeholder': 'Enter Message*'})
        }
    #          labels = {
        #     'Participant_Name':'Participant Name',
        #     'Bank_Name':'Name of the Bank/ PACS',
        #     'Employee_ID':'Employee ID',
        #     'Mobile_No':'Mobile Number',
        #     'Email_ID':'Email ID',
        #     'Programme_No': 'Program Number'}


class ReferAStudentForm(ModelForm):
    class Meta:
        model = Refer_A_Student
        fields = ('child_name', 'parent_name', 'mobile_No', 'email', 'referee_parent_name',
                  'referee_child_name', 'referee_mobile_No', 'referee_email', 'Note')
        labels = {
            'child_name': '',
            'parent_name': '',
            'mobile_No': '',
            'email': '',
            'referee_parent_name': '',
            'referee_child_name': '',
            'referee_mobile_No': '',
            'referee_email': '',
            'Note': ''
        }
        widgets = {
            'child_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Child Name*'}),
            'parent_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Parent Name*'}),
            'mobile_No': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mobile Number*'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email*'}),
            'referee_parent_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Referee Child Name*'}),
            'referee_child_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Referee Parent Name*'}),
            'referee_mobile_No': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Referee Mobile Number*'}),
            'referee_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Referee Email*'}),
            'Note': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Note'})

        }


class StudentEnquiryForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(StudentEnquiryForm, self).__init__(*args, **kwargs)
        self.fields['academic_year'].choices =  [('', '---Please select Academic Year---')] + Student_Enquiry.YEAR_CHOICES
        self.fields['gender'].choices =  [('', '---Please select Gender---')] + Student_Enquiry.GENDER_CHOICES
        self.fields['relation'].choices =  [('', '---Please select Relation---')] + Student_Enquiry.REL_CHOICES
        self.fields['local_type'].choices =  [('', '---Please select Local Type---')] + Student_Enquiry.LOCAL_CHOICES

    mobile_No =  PhoneNumberField( widget = PhoneNumberPrefixWidget(initial="IN", attrs={'class': 'form-control mvrdd', 'placeholder': 'Mobile No*'}), )
    mother_mobile_No =  PhoneNumberField( widget = PhoneNumberPrefixWidget(initial="IN", attrs={'class': 'form-control mvrdd', 'placeholder': 'Mother Mobile No*'}), )
    father_mobile_No =  PhoneNumberField( widget = PhoneNumberPrefixWidget(initial="IN", attrs={'class': 'form-control mvrdd', 'placeholder': 'Father Mobile No*'}), )
    reference_mobile_No =  PhoneNumberField( widget = PhoneNumberPrefixWidget(initial="IN", attrs={'class': 'form-control mvrdd', 'placeholder': 'Reference Mobile No*'}), )
   

    class Meta:
        model = Student_Enquiry
        # academic_year = forms.ModelChoiceField(label="", queryset= Student_Enquiry.objects.values_list("academic_year"),  empty_label= "Placeholder")
        fields = ('academic_year', 'first_name', 'middle_name', 'last_name', 'date_of_birth', 'gender', 'relation', 'local_type', 'transfer_from', 'mobile_No', 'email', 'message', 'mother_name', 'mother_organization', 'mother_designation', 'mother_income', 'mother_mobile_No',
                  'mother_email', 'father_name', 'father_orgnization', 'father_designation', 'father_income', 'father_mobile_No', 'father_email', 'reference_name', 'reference_designation', 'reference_department', 'reference_company', 'reference_mobile_No', 'reference_email', 'remarks')
        labels = {'first_name': '', 'middle_name': '', 'last_name': '', 'date_of_birth': '', 'gender': 'Gender', 'relation': 'Relation', 'local_type': 'Local Type', 'transfer_from': '', 'mobile_No': '', 'email': '', 'message': '', 'mother_name': '', 'mother_organization': '', 'mother_designation': '', 'mother_income': '', 'mother_mobile_No': '',
                  'mother_email': '', 'father_name': '', 'father_orgnization': '', 'father_designation': '', 'father_income': '', 'father_mobile_No': '', 'father_email': '', 'reference_name': '', 'reference_designation': '', 'reference_department': '', 'reference_company': '', 'reference_mobile_No': '', 'reference_email': '', 'remarks': ''}
        widgets = {
            
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name*'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Middle Name*'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last name*'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Date of Birth*'}),
            #  'gender': forms.RadioSelect(attrs={'class':'form-control','placeholder': 'Gender*'}),
            #  'relation': forms.ChoiceField(choices = Student_Enquiry.REL_CHOICES),form-select
            # 'relation': forms.ChoiceField(attrs={'class':'form-select'}),
            #  'local_type': forms.ChoiceField(choices = Student_Enquiry.LOCAL_CHOICES),
            'transfer_from': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Transfer From*'}),
            'mobile_No': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mobile No*'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email*'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message*'}),
            'mother_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mother Name*'}),
            'mother_organization': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mother Organization*'}),
            'mother_designation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mother Designation*'}),
            'mother_income': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mother Income*'}),
            'mother_email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mother Email*'}),
            'father_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Father Name*'}),
            'father_orgnization': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Father Orgnization*'}),
            'father_designation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Father Designation*'}),
            'father_income': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Father Income*'}),
            'father_email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Father Email*'}),
            'reference_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Reference Name*'}),
            'reference_designation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Reference Designation*'}),
            'reference_department': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Reference Department*'}),
            'reference_company': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Reference Company*'}),
            'reference_email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Reference Email*'}),
            'remarks': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Remarks*'})

        }


class ApplyJobForm(ModelForm):
    Telephone_No =  PhoneNumberField(

        widget = PhoneNumberPrefixWidget(initial="IN", attrs={'class': 'form-control mvrdd', 'placeholder': 'Telephone No*'}),
        
    )
    class Meta:
        model = ApplyJob
        fields = ('Post_Applying_For', 'Name_of_the_Candidate', 'Residential_Address', 'Own_house_rented', 'Mother_Tongue', 'date_of_birth', 'Caste_Category_Religion', 'Email_ID', 'Telephone_No', 'Qualifications', 'Last_Worked', 'Reasons', 'Any_friends', 'Have_you_worked', 'Present_Salary', 'Expected_Salary', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'nsc1', 'nsc2', 'nsc3', 'nsc4', 'nsc5', 'nsc6', 'u1', 'u2', 'u3', 'u4', 'u5', 'u6', 'pos1', 'pos2', 'pos3', 'pos4', 'pos5', 'pos6', 'yp1', 'yp2', 'yp3', 'yp4', 'yp5', 'yp6', 'm1', 'm2', 'm3', 'm4', 'm5', 'm6', 'rc1', 'rc2',
                  'rc3', 'rc4', 'rc5', 'rc6', 'sec1', 'sec2', 'sec3', 'sec4', 'sec5', 'sec6', 'no1', 'no2', 'no3', 'no4', 'no5', 'no6', 'deg1', 'deg2', 'deg3', 'deg4', 'deg5', 'deg6', 'yow1', 'yow2', 'yow3', 'yow4', 'yow5', 'yow6', 'sal1', 'sal2', 'sal3', 'sal4', 'sal5', 'sal6', 'skill1', 'skill2', 'Sp_Name', 'Sp_DOB', 'Sp_Qul', 'Sp_Occ', 'Sp_Deg', 'Sp_Inc', 'F_Name', 'F_DOB', 'F_Qul', 'F_Occ', 'F_Deg', 'F_Inc', 'M_Name', 'M_DOB', 'M_Qul', 'M_Occ', 'M_Deg', 'M_Inc', 'C1_Name', 'C1_DOB', 'C1_St', 'C1_PSN', 'C2_Name', 'C2_DOB', 'C2_St', 'C2_PSN', 'Ref1', 'Ref2', 'upload_cv')
        labels = {'Post_Applying_For': '', 'Name_of_the_Candidate': '', 'Residential_Address': '', 'Own_house_rented': '', 'Mother_Tongue': '', 'date_of_birth': '', 'Caste_Category_Religion': 'Caste Category /Religion', 'Email_ID': '', 'Telephone_No': '', 'Qualifications': '', 'Last_Worked': '', 'Reasons': '', 'Any_friends': '', 'Have_you_worked': '', 'Present_Salary': '', 'Expected_Salary': '', 'c1': '', 'c2': '', 'c3': '', 'c4': '', 'c5': '', 'c6': '', 'nsc1': '', 'nsc2': '', 'nsc3': '', 'nsc4': '', 'nsc5': '', 'nsc6': '', 'u1': '', 'u2': '', 'u3': '', 'u4': '', 'u5': '', 'u6': '', 'pos1': '', 'pos2': '', 'pos3': '', 'pos4': '', 'pos5': '', 'pos6': '', 'yp1': '', 'yp2': '', 'yp3': '', 'yp4': '', 'yp5': '', 'yp6': '', 'm1': '', 'm2': '', 'm3': '', 'm4': '', 'm5': '', 'm6': '', 'rc1': '', 'rc2': '',
                  'rc3': '', 'rc4': '', 'rc5': '', 'rc6': '', 'sec1': '', 'sec2': '', 'sec3': '', 'sec4': '', 'sec5': '', 'sec6': '', 'no1': '', 'no2': '', 'no3': '', 'no4': '', 'no5': '', 'no6': '', 'deg1': '', 'deg2': '', 'deg3': '', 'deg4': '', 'deg5': '', 'deg6': '', 'yow1': '', 'yow2': '', 'yow3': '', 'yow4': '', 'yow5': '', 'yow6': '', 'sal1': '', 'sal2': '', 'sal3': '', 'sal4': '', 'sal5': '', 'sal6': '', 'skill1': '', 'skill2': '', 'Sp_Name': '', 'Sp_DOB': '', 'Sp_Qul': '', 'Sp_Occ': '', 'Sp_Deg': '', 'Sp_Inc': '', 'F_Name': '', 'F_DOB': '', 'F_Qul': '', 'F_Occ': '', 'F_Deg': '', 'F_Inc': '', 'M_Name': '', 'M_DOB': '', 'M_Qul': '', 'M_Occ': '', 'M_Deg': '', 'M_Inc': '', 'C1_Name': '', 'C1_DOB': '', 'C1_St': '', 'C1_PSN': '', 'C2_Name': '', 'C2_DOB': '', 'C2_St': '', 'C2_PSN': '', 'Ref1': '', 'Ref2': '', 'upload_cv': ''}
        widgets = {
        'Post_Applying_For': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Post Applying For*'}), 
        'Name_of_the_Candidate': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name of the Candidate*'}), 
        'Residential_Address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Residential Address*'}), 
        'Own_house_rented': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Own house / Rented*'}), 
        'Mother_Tongue': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mother Tongue*'}), 
        'date_of_birth': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Date of Birth*'}), 
        # 'Caste_Category_Religion': forms.ChoiceField(), 
        'Email_ID': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email ID*'}), 
        'Qualifications': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Qualifications*'}), 
        'Last_Worked': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Organization Last Worked / Working *'}), 
        'Reasons': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Reasons for or desire to leave present Job / Position*'}), 
        'Any_friends': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Any friends /relatives working in this school *'}), 
        'Have_you_worked': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Have you worked in this school earlier – Details of service & reason for leaving *'}), 
        'Present_Salary': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Present Salary(Salary certificate/ Pay slip to be submitted)*'}), 
        'Expected_Salary': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Expected Salary*'}), 
        'c1': forms.TextInput(attrs={'class': 'form-control'}), 
        'c2': forms.TextInput(attrs={'class': 'form-control'}), 
        'c3': forms.TextInput(attrs={'class': 'form-control'}), 
        'c4': forms.TextInput(attrs={'class': 'form-control'}), 
        'c5': forms.TextInput(attrs={'class': 'form-control'}), 
        'c6': forms.TextInput(attrs={'class': 'form-control'}), 
        'nsc1': forms.TextInput(attrs={'class': 'form-control'}), 
        'nsc2': forms.TextInput(attrs={'class': 'form-control'}), 
        'nsc3': forms.TextInput(attrs={'class': 'form-control'}), 
        'nsc4': forms.TextInput(attrs={'class': 'form-control'}), 
        'nsc5': forms.TextInput(attrs={'class': 'form-control'}), 
        'nsc6': forms.TextInput(attrs={'class': 'form-control'}), 
        'u1': forms.TextInput(attrs={'class': 'form-control'}), 
        'u2': forms.TextInput(attrs={'class': 'form-control'}), 
        'u3': forms.TextInput(attrs={'class': 'form-control'}), 
        'u4': forms.TextInput(attrs={'class': 'form-control'}), 
        'u5': forms.TextInput(attrs={'class': 'form-control'}), 
        'u6': forms.TextInput(attrs={'class': 'form-control'}), 
        'pos1': forms.TextInput(attrs={'class': 'form-control'}), 
        'pos2': forms.TextInput(attrs={'class': 'form-control'}), 
        'pos3': forms.TextInput(attrs={'class': 'form-control'}), 
        'pos4': forms.TextInput(attrs={'class': 'form-control'}), 
        'pos5': forms.TextInput(attrs={'class': 'form-control'}), 
        'pos6': forms.TextInput(attrs={'class': 'form-control'}), 
        'yp1': forms.TextInput(attrs={'class': 'form-control'}), 
        'yp2': forms.TextInput(attrs={'class': 'form-control'}), 
        'yp3': forms.TextInput(attrs={'class': 'form-control'}), 
        'yp4': forms.TextInput(attrs={'class': 'form-control'}), 
        'yp5': forms.TextInput(attrs={'class': 'form-control'}), 
        'yp6': forms.TextInput(attrs={'class': 'form-control'}), 
        'm1': forms.TextInput(attrs={'class': 'form-control'}), 
        'm2': forms.TextInput(attrs={'class': 'form-control'}), 
        'm3': forms.TextInput(attrs={'class': 'form-control'}), 
        'm4': forms.TextInput(attrs={'class': 'form-control'}), 
        'm5': forms.TextInput(attrs={'class': 'form-control'}), 
        'm6': forms.TextInput(attrs={'class': 'form-control'}), 
        'rc1': forms.TextInput(attrs={'class': 'form-control'}), 
        'rc2': forms.TextInput(attrs={'class': 'form-control'}),
        'rc3': forms.TextInput(attrs={'class': 'form-control'}), 
        'rc4': forms.TextInput(attrs={'class': 'form-control'}), 
        'rc5': forms.TextInput(attrs={'class': 'form-control'}), 
        'rc6': forms.TextInput(attrs={'class': 'form-control'}), 
        'sec1': forms.TextInput(attrs={'class': 'form-control'}), 
        'sec2': forms.TextInput(attrs={'class': 'form-control'}), 
        'sec3': forms.TextInput(attrs={'class': 'form-control'}), 
        'sec4': forms.TextInput(attrs={'class': 'form-control'}), 
        'sec5': forms.TextInput(attrs={'class': 'form-control'}), 
        'sec6': forms.TextInput(attrs={'class': 'form-control'}), 
        'no1': forms.TextInput(attrs={'class': 'form-control'}), 
        'no2': forms.TextInput(attrs={'class': 'form-control'}), 
        'no3': forms.TextInput(attrs={'class': 'form-control'}), 
        'no4': forms.TextInput(attrs={'class': 'form-control'}), 
        'no5': forms.TextInput(attrs={'class': 'form-control'}), 
        'no6': forms.TextInput(attrs={'class': 'form-control'}), 
        'deg1': forms.TextInput(attrs={'class': 'form-control'}), 
        'deg2': forms.TextInput(attrs={'class': 'form-control'}), 
        'deg3': forms.TextInput(attrs={'class': 'form-control'}), 
        'deg4': forms.TextInput(attrs={'class': 'form-control'}), 
        'deg5': forms.TextInput(attrs={'class': 'form-control'}), 
        'deg6': forms.TextInput(attrs={'class': 'form-control'}), 
        'yow1': forms.TextInput(attrs={'class': 'form-control'}), 
        'yow2': forms.TextInput(attrs={'class': 'form-control'}), 
        'yow3': forms.TextInput(attrs={'class': 'form-control'}), 
        'yow4': forms.TextInput(attrs={'class': 'form-control'}), 
        'yow5': forms.TextInput(attrs={'class': 'form-control'}), 
        'yow6': forms.TextInput(attrs={'class': 'form-control'}), 
        'sal1': forms.TextInput(attrs={'class': 'form-control'}), 
        'sal2': forms.TextInput(attrs={'class': 'form-control'}), 
        'sal3': forms.TextInput(attrs={'class': 'form-control'}), 
        'sal4': forms.TextInput(attrs={'class': 'form-control'}), 
        'sal5': forms.TextInput(attrs={'class': 'form-control'}), 
        'sal6': forms.TextInput(attrs={'class': 'form-control'}), 
        'skill1': forms.TextInput(attrs={'class': 'form-control'}), 
        'skill2': forms.TextInput(attrs={'class': 'form-control'}), 
        'Sp_Name': forms.TextInput(attrs={'class': 'form-control'}), 
        'Sp_DOB': forms.TextInput(attrs={'class': 'form-control'}), 
        'Sp_Qul': forms.TextInput(attrs={'class': 'form-control'}), 
        'Sp_Occ': forms.TextInput(attrs={'class': 'form-control'}), 
        'Sp_Deg': forms.TextInput(attrs={'class': 'form-control'}), 
        'Sp_Inc': forms.TextInput(attrs={'class': 'form-control'}), 
        'F_Name': forms.TextInput(attrs={'class': 'form-control'}), 
        'F_DOB': forms.TextInput(attrs={'class': 'form-control'}), 
        'F_Qul': forms.TextInput(attrs={'class': 'form-control'}), 
        'F_Occ': forms.TextInput(attrs={'class': 'form-control'}), 
        'F_Deg': forms.TextInput(attrs={'class': 'form-control'}), 
        'F_Inc': forms.TextInput(attrs={'class': 'form-control'}), 
        'M_Name': forms.TextInput(attrs={'class': 'form-control'}), 
        'M_DOB': forms.TextInput(attrs={'class': 'form-control'}), 
        'M_Qul': forms.TextInput(attrs={'class': 'form-control'}), 
        'M_Occ': forms.TextInput(attrs={'class': 'form-control'}), 
        'M_Deg': forms.TextInput(attrs={'class': 'form-control'}), 
        'M_Inc': forms.TextInput(attrs={'class': 'form-control'}), 
        'C1_Name': forms.TextInput(attrs={'class': 'form-control'}), 
        'C1_DOB': forms.TextInput(attrs={'class': 'form-control'}), 
        'C1_St': forms.TextInput(attrs={'class': 'form-control'}), 
        'C1_PSN': forms.TextInput(attrs={'class': 'form-control'}), 
        'C2_Name': forms.TextInput(attrs={'class': 'form-control'}), 
        'C2_DOB': forms.TextInput(attrs={'class': 'form-control'}), 
        'C2_St': forms.TextInput(attrs={'class': 'form-control'}), 
        'C2_PSN': forms.TextInput(attrs={'class': 'form-control'}), 
        'Ref1': forms.Textarea(attrs={'class': 'form-control'}), 
        'Ref2': forms.Textarea(attrs={'class': 'form-control'}), 
        'upload_cv': forms.FileInput()
        }

