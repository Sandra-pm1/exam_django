from django.shortcuts import render,redirect
from django.views.generic import View
from roadapp.forms import ViolationForm,SignUpForm,SignInForm
from roadapp.models import Violation
from django.contrib.auth import authenticate,login,logout

# Create your views here.

class SignUpView(View):
    template_name="signup.html"
    form_class=SignUpForm
    def get(self,request,*args,**kwargs):
        form_instance=self.form_class()
        return render(request,self.template_name,{"form":form_instance})
    def post(self,request,*args,**kwargs):
        form_data=request.POST 
        form_instance=self.form_class(form_data)
        if form_instance.is_valid():
            form_instance.save()
            print("account created")
            return redirect("login")
        print("creation failed")
        return render(request,self.template_name,{"form":form_instance})

class SignInView(View):
    def post(self,request,*args,**kwargs):
        uname=data.get("username")
        pwd=data.get("password")
        user_obj=authenticate(request,username=uname,password=pwd)
        if user_obj:
            login("session created")
            return redirect("create")
        print("Invalid session")
        return render(request,self.template_name,{"form":form_instance})

class ViolationCreateView(View):
    template_name="create.html"
    form_class=ViolationForm
    def get(self,request,*args,**kwargs):
        form_instance=self.form_class()
        return render(request,self.template_name,{"form":form_instance})
    def post(self,request,*args,**kwargs):
        form_data=request.POST 
        form_instanceself.form_class(form_data)
        if form_instance.is_valid():
            form_instance.save()
            return redirect("create")
        return render(request,self.template_name,{"form":form_instance})
