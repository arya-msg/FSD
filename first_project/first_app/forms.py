from django import forms
from first_app.models import Degree

class DegreeForm(forms.Form) :
    title = forms.CharField(label='Title', max_length=20)
    branch = forms.CharField(label='Branch', max_length=50)
    file = forms.FileField(label='Select a JSON file', help_text='(max. 2 mb)')

class StudentForm(forms.Form):
    roll_number = forms.CharField(label='Roll Number', max_length=20)
    name = forms.CharField(label='Name', max_length=50)
    year = forms.IntegerField(label='Year' )
    dob = forms.DateField(label = "Date of Birth")
    degree_values = Degree.objects.all()

    degreeList = []

    for value in degree_values:
         degreeList.append((value.branch,value.branch))
    #
    degree = forms.ChoiceField(choices = degreeList)
    #degree = forms.CharField(label='Degree', max_length=50)
    file = forms.FileField(label='Select a JSON file', help_text='(max. 2 mb)')

class SearchForm(forms.Form):
    roll_number = forms.CharField(label='Roll Number', max_length=20)
    name = forms.CharField(label='Name', max_length=50)
    year = forms.IntegerField(label='Year' )
    fromDate = forms.DateField(label = "From Date")
    toDate = forms.DateField(label = "To Date")
    degree = forms.CharField(label='Degree', max_length=20)
