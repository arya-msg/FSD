from django import forms
from first_app.models import Degree

class DegreeForm(forms.Form) :
    title = forms.CharField(label='Title', max_length=20, required=False)
    branch = forms.CharField(label='Branch', max_length=50, required=False)
    # file = forms.FileField(label='Select a JSON file', help_text='(max. 2 mb)', required=False)
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), label='Select JSON files', help_text='(max. 2 mb)', required=False)

class StudentForm(forms.Form):
    roll_number = forms.CharField(label='Roll Number', max_length=20, required=False)
    name = forms.CharField(label='Name', max_length=50, required=False)
    year = forms.IntegerField(label='Year', required=False)
    dob = forms.DateField(label = "Date of Birth(mm/dd/yyyy)", required=False)
    degree_values = Degree.objects.all()
    #file = forms.FileField(label='Select a JSON file', help_text='(max. 2 mb)', required=False)
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), label='Select JSON files', help_text='(max. 2 mb)', required=False)

    degreeList = []
    for value in degree_values:
         degreeList.append((value.branch,value.branch))
    degree = forms.ChoiceField(choices = degreeList)

class SearchForm(forms.Form):
    roll_number = forms.CharField(label='Roll Number', max_length=20, required=False)
    name = forms.CharField(label='Name', max_length=50, required=False)
    year = forms.IntegerField(label='Year', required=False)
    fromDate = forms.DateField(label = "From Date(mm/dd/yyyy)", required=False)
    toDate = forms.DateField(label = "To Date(mm/dd/yyyy)", required=False)
    degree = forms.CharField(label='Degree', max_length=20, required=False)
    sort = forms.BooleanField(label = "Sort Asc", required=False)
