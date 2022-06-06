from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Person

from django.views.generic import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView

# Create your views here.
class UserSignup(FormView):
	print("UserSignup")
	template_name = 'emplye_mang_sys_app/signup.html'
	form_class = UserCreationForm
	redirect_authenticated_user = True
	success_url = reverse_lazy('login')

	def form_valid(self, form):
		print("UserSignup.form_valid")
		user = form.save()
		if user is not None:
			print("UserSignup.form_valid.user not none")
			login(self.request, user)
		return super(UserSignup, self).form_valid(form)

	def get(self, *args, **kwargs):
		print("UserSignup.get")
		if self.request.user.is_authenticated:
			print("UserSignup.get.is_authenticated")
			return redirect('personlist')
		return super(UserSignup, self).get(*args, **kwargs)


class UserLogin(LoginView):
	print("UserLogin")
	template_name = 'emplye_mang_sys_app/signin.html'
	fields = '__all__'
	redirect_authenticated_user = True

	def get_success_url(self):
		print("UserLogin.get_success_url")
		return reverse_lazy('personlist')


class PersonCreate(LoginRequiredMixin,View):

	def get(self,request):
		print("PersonCreate.get")
		return render(request,'emplye_mang_sys_app/person_create_form.html')

	def post(self,request):
		print("PersonCreate.post")
		user = User.objects.get(username=request.user)
		my_name = request.POST.get('name')
		user.person_set.create(name=my_name)
		my_object = user.person_set.get(name=my_name).id
		return redirect('persondetail',my_object)


class PersonList(LoginRequiredMixin,View):
	def get(self,request):
		print("PersonList.get")
		account = User.objects.get(username=request.user)
		context = {'person_list':account}
		return render(request,'emplye_mang_sys_app/home.html',context)


class PersonDetail(LoginRequiredMixin,DetailView):
	model = Person
	context_object_name = 'person'

	def get(self,*args,**kwargs):
		print("PersonDetail.get")
		return super(PersonDetail, self).get(*args,**kwargs)

	def post(self,*args,**kwargs):
		print("PersonDetail.post")
		return super(PersonDetail, self).get(*args,**kwargs)

	def dispatch(self,request,pk,*args,**kwargs):
		print("PersonDetail.dispatch")
		peep = self.model.objects.get(id=pk)
		if self.request.POST.get('save'):
			print("PersonDetail.dispatch.save")
			for task in peep.task_set.all():
				if request.POST.get(f't{task.id}') == 'clicked':
					task.is_complete = True
				else:
					task.is_complete = False
				task.save()

		elif self.request.POST.get('add_item'):
			print("PersonDetail.dispatch.post.add")
			new = request.POST.get('new_item')
			peep.task_set.create(task=new, is_complete=False)

		elif request.POST.get('delete_this'):
			print("PersonDetail.dispatch.post.delete")
			task_index = request.POST.get('delete_this')
			peep.task_set.get(id=task_index).delete()

		return super(PersonDetail, self).dispatch(request,*args,**kwargs)


class PersonUpdate(LoginRequiredMixin,UpdateView):
	print("PersonUpdate")
	model = Person
	fields = ['name']
	template_name_suffix = '_update_form'
	success_url = reverse_lazy('personlist')


class PersonDelete(LoginRequiredMixin,DeleteView):
	print("PersonDelete")
	model = Person
	success_url = reverse_lazy('personlist')
