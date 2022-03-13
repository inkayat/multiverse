from django.shortcuts import redirect, render
from .models import Data
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import DataForm


class Index(View):
    template = 'index.html'
    login_url = '/login/'
    
    def get(self, request):
        data = Data.objects.all()
        return render(request, self.template, {'data': data})


class Login(View):
    template = 'login.html'
    
    def get(self, request):
        form = AuthenticationForm()
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, self.template, {'form': form})

 
class AddData(View):
    template = 'multiverse/add_data.html'
    
    def post(self, request):
        form = DataForm(request.POST,request.FILES)
        if form.is_valid():
            form.save() 
        return redirect('/')
  
    def get(self, request):
        form = DataForm()
        return render(request, self.template, {'form': form})