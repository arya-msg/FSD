from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse

from .forms import DegreeForm
from .forms import StudentForm                   # Relative import from our forms.py using .forms
from first_app.models import Degree, Student
import json

def index(request) :    # 'request' name is convention. It can be some other name too.
    return HttpResponse("Hello World")

def get_degree(request):
  if request.method == 'POST':                  # if this is a POST request we need to process the form data
    form = DegreeForm(request.POST, request.FILES)             # create a form instance and populate it with data from the request:
    if form.is_valid():                         # check whether it's valid:
      title = form.cleaned_data['title']        # retrieve the data in form.cleaned_data as required
      branch = form.cleaned_data['branch']

      d = Degree(title=title, branch=branch)    # write to the database
      d.save()
       # Retrieve the json file and process here
      f = request.FILES['file']          # open the json files - get file handle
      data = json.load(f)
      for deg in data['degree']:         # iterate through the degree list
        t = deg['title']                 # get the title of each item in the list
        b = deg['branch']                # get the branch of each item in the list
        dl = Degree(title=t, branch=b)   # Create a Degree model instance
        dl.save()                        # save

# loading form again after saving with the retrieved values

      form = DegreeForm()
      degree_values = Degree.objects.all()
      my_dict = { 'degree_rows' : degree_values}
      my_dict["form"] = form
      return render(request,'degree.html',context=my_dict)
      #return HttpResponseRedirect('/degree/')   # redirect to a degree page or to new URL: return HttpResponseRedirect('/thanks/')
  else:                                         # if a GET (or any other method) we'll create a blank form
    form = DegreeForm()
    degree_values = Degree.objects.all()
    my_dict = { 'degree_rows' : degree_values}
    my_dict["form"] = form
    return render(request, 'degree.html',  context=my_dict)

def get_student(request):
      if request.method == 'POST':                  # if this is a POST request we need to process the form data
        form = StudentForm(request.POST, request.FILES)             # create a form instance and populate it with data from the request:
        if form.is_valid():                         # check whether it's valid:
          roll_number = form.cleaned_data['roll_number']        # retrieve the data in form.cleaned_data as required
          name = form.cleaned_data['name']
          year = form.cleaned_data['year']
          degree = form.cleaned_data['degree']
          dob = form.cleaned_data['dob']

          degree_value = Degree.objects.filter(branch = degree)
          deg = ""

          for value in degree_value:
               deg = value
          d = Student(roll_number=roll_number, name=name, year = year, dob = dob, degree = degree_value[0])    # write to the database
          d.save()

           # Retrieve the json file and process here
          f = request.FILES['file']          # open the json files - get file handle
          data = json.load(f)
          for deg in data['student']:         # iterate through the degree list
            roll_number = form.cleaned_data['roll_number']        # retrieve the data in form.cleaned_data as required
            name = deg['name']
            year = deg['year']
            dob = deg['dob']
            degree = deg['degree']
            print("degree*****************", degree)
            degree_value = Degree.objects.filter(branch = degree)
            print("degree retrieved**************", degree_value)
            deg = ""
            for value in degree_value:
                 deg = value
            d1 = Student(roll_number=roll_number, name=name, year = year, dob = dob, degree = degree_value[0])                # get the title of each item in the list
            d1.save()                        # save

        # loading form again after saving with the retrieved values
          form = StudentForm()
          student_values = Student.objects.all()
          my_dict = { 'student_rows' : student_values}
          my_dict["form"] = form
          return render(request,'student.html',context=my_dict)

      else:                                         # if a GET (or any other method) we'll create a blank form
        form = StudentForm()
        student_values = Student.objects.all()
        my_dict = { 'student_rows' : student_values}
        my_dict["form"] = form
        return render(request, 'student.html',  context=my_dict)
