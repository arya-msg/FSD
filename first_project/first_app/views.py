from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse

from .forms import DegreeForm
from .forms import StudentForm
from .forms import SearchForm                   # Relative import from our forms.py using .forms
from first_app.models import Degree, Student
from django.db.models import Q
import json
from django_globals import globals
from django.contrib import messages

global clicked
clicked = 0

#load index.html page
def index(request) :
    return render(request, 'index.html')

#load tictactoe.html page
def tictactoe(request):
    return render(request,'tictactoe.html')

#load Wordle.html page
def wordle(request):
    return render(request,'wordle.html')

#load project5_6.html page
def load_project5_6(request):

    global clicked
    clicked = clicked+1
    my_dict = { 'inject_var' : clicked}
    evenOrOdd = clicked%2
    my_dict['evenOrOdd'] =  evenOrOdd
    fruitList = ['Mango', 'Apple', 'Banana','Orange','Grapes']
    my_dict['fruits'] =  fruitList
    return render(request,'project5_6.html',context=my_dict)

#load help.html page associated with project5_6
def help(request) :
    return render(request,'help.html')

#Load project7_10.html page
def load_project7_8(request):
    return render(request,'project7_8.html')

def add_degree(request):
    if request.method == 'POST':
        print("inside addDegree post")
        form = DegreeForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            branch = form.cleaned_data['branch']
            file = form.cleaned_data['file']
            if (file == None and (len(title) == 0 or len(branch) == 0)):
                messages.error(request,'Either file has to be uploaded or fill both fields.')
                return HttpResponseRedirect('/project7_8/degree/')
            else :
                if (len(title) != 0 and len(branch) != 0):
                    dl = Degree(title=title, branch=branch)   # Create a Degree model instance
                    dl.save()
                elif ((len(title) != 0 and len(branch) == 0 ) or (len(title) == 0 and len(branch) != 0)):
                    messages.error(request,'Either fill both fields or leave both field blank')
                    return HttpResponseRedirect('/project7_8/degree/')

                if file != None  :
                     for count, x in enumerate(request.FILES.getlist("file")):
                        # f = request.FILES['file']      # open the json files - get file handle
                        # data = json.load(f)
                        data = json.load(x)
                        for deg in data['degree']:
                            t = deg['title']
                            b = deg['branch']
                            dl = Degree(title=t, branch=b)
                            dl.save()
                messages.success(request, "Degree Added")
                return HttpResponseRedirect('/project7_8/degree/')
    else:
        form = DegreeForm()
        degree_values = Degree.objects.all()
        my_dict = {'degree_rows' : degree_values}
        my_dict["form"] = form
        return render(request,'degree.html',context=my_dict)

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)

        if form.is_valid():
            roll_number = form.cleaned_data['roll_number']
            name = form.cleaned_data['name']
            year = form.cleaned_data['year']
            degree = form.cleaned_data['degree']
            dob = form.cleaned_data['dob']
            file = form.cleaned_data['file']
            if (file == None and (len(roll_number) == 0 or len(name) == 0 or dob == None or year == None)):
                messages.error(request,'Either file has to be uploaded or fill all the fields.')
                return HttpResponseRedirect('/project7_8/student/')
            else :
                if (len(roll_number) != 0 and len(name) != 0 and dob != None and year != None):
                    degree_value = Degree.objects.filter(branch = degree)
                    deg = ""
                    for value in degree_value:
                        deg = value
                    d1 = Student(roll_number=roll_number, name=name, year = year, dob = dob, degree = deg)
                    d1.save()
                if file != None:
                    # f = request.FILES['file']
                    # data = json.load(f)
                    for count, x in enumerate(request.FILES.getlist("file")):
                       data = json.load(x)
                       for deg in data['student']:
                           roll_number = deg['roll_number']
                           name = deg['name']
                           year = deg['year']
                           dob = deg['dob']
                           degree = deg['degree']
                           degree_value = Degree.objects.filter(branch = degree)
                           deg = ""
                           for value in degree_value:
                               deg = value
                           d1 = Student(roll_number=roll_number, name=name, year = year, dob = dob, degree = deg)
                           d1.save()
                messages.success(request, "Student Added")
                return HttpResponseRedirect('/project7_8/student/')
        else :
            print("invalid form")
    else:
        form = StudentForm()
        student_values = Student.objects.all()
        my_dict = { 'student_rows' : student_values}
        my_dict["form"] = form
        return render(request,'student.html',context=my_dict)

# def search_student(request):
#     return render(request,'search.html')

def search_student(request):
    form = SearchForm(request.GET)
    print("form:",form)
    if form.is_valid():
        roll_number = form.cleaned_data['roll_number']
        name = form.cleaned_data['name']
        year = form.cleaned_data['year']
        degree = form.cleaned_data['degree']
        toDate = form.cleaned_data['toDate']
        fromDate = form.cleaned_data['fromDate']
        sort = form.cleaned_data['sort']

        print ("roll_number: ", roll_number,"name: ", name,"year: ", year,"degree: ", degree,"toDate: ", toDate,"fromDate: ", fromDate, "sort: ", sort)
        if (len(roll_number) == 0 and len(name) == 0 and year == None and len(degree) == 0 and toDate == None and fromDate == None):
            form = SearchForm()
            student_values = Student.objects.all()
            my_dict = { 'student_rows' : student_values}
            my_dict["form"] = form
            return render(request,'search.html',context=my_dict)
        else:
            print ("roll_number: ", roll_number,"name: ", name,"year: ", year,"degree: ", degree,"toDate: ", toDate,"fromDate: ", fromDate, "sort: ", sort)
            student_values = None
            if(len(roll_number) != 0):

                print ("roll")
                if(sort):
                    student_values = Student.objects.filter(roll_number__icontains=roll_number).order_by('roll_number')
                else:
                    student_values = Student.objects.filter(roll_number__icontains=roll_number)
            elif(len(name) != 0):
                print ("name")
                if(sort):
                    student_values = Student.objects.filter(name__icontains=name).order_by('name')
                else:
                    student_values = Student.objects.filter(name__icontains=name)
            elif(len(degree) != 0):
                print ("degree")
                if(sort):
                    student_values = Student.objects.filter(Q(degree__title__icontains=degree) | Q(degree__branch__icontains=degree)).order_by('degree__title','degree__branch')
                else:
                    student_values = Student.objects.filter(Q(degree__title__icontains=degree) | Q(degree__branch__icontains=degree))
            elif(year != None):
                print ("year")
                if(sort):
                    student_values = Student.objects.filter(year__lte=year).order_by('year')
                else:
                    student_values = Student.objects.filter(year__lte=year)
            elif(toDate != None and fromDate != None):
                print ("toDate,fromDate")
                if(sort):
                    student_values = Student.objects.filter(dob__lte = toDate, dob__gte = fromDate).order_by('dob')
                else:
                    student_values = Student.objects.filter(dob__lte = toDate, dob__gte = fromDate)
            elif(toDate != None):
                print ("toDate")
                if(sort):
                    student_values = Student.objects.filter(dob__lte = toDate).order_by('dob')
                else:
                    student_values = Student.objects.filter(dob__lte = toDate)

            elif(fromDate != None):
                print ("fromDate")
                if(sort):
                    student_values = Student.objects.filter(dob__gte = fromDate).order_by('dob')
                else:
                    student_values = Student.objects.filter(dob__gte = fromDate)
            my_dict = { 'student_rows' : student_values}
            my_dict["form"] = form
            return render(request, 'search.html',  context=my_dict)
