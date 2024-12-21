from django.shortcuts import render,redirect
from django.views.generic import View
from roadapp.forms import ViolationForm
from roadapp.models import Violation
from roadapp.forms import SignInForm,SignUpForm
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
            print("Created Account")
            return redirect("login")
        print("Failed To Create Account")
        return render(request,self.template_name,{"form":form_instance})
    

class SignInView(View):
    template_name="signin.html"
    form_class=SignInForm
    def get(self,request,*args,**kwargs):
        form_instance=self.form_class()
        return render(request,self.template_name,{"form":form_instance})
    def post(self,request,*args,**kwargs):
        form_data=request.POST 
        form_instance=self.form_class(form_data)
        if form_instance.is_valid():
            data=form_instance.cleaned_data
            uname=data.get("username")
            pwd=data.get("password")
            user_object=authenticate(request,username=uname,password=pwd)
            if user_object:
                login(request,user_object)
                print("session started")
                return redirect("create")
        print("invalid Crediential")
        return render(request,self.template_name,{"form":form_instance})

class SignOutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("login")
    
class ViolationCreateView(View):
    template_name="create.html"
    form_class=ViolationForm
    def get(self,request,*args,**kwargs):
        form_instance=self.form_class()
        return render(request,self.template_name,{"form":form_instance})
    def post(self,request,*args,**kwargs):
        form_data=request.POST
        form_instance=self.form_class(form_data)
        if form_instance.is_valid():
            form_instance.save()
        return redirect("list")
        return render(request,self.template_name,{"form":form_instance})
    

class ViolationsListView(View):
    template_name="list.html"
    def get(self,request,*args,**kwargs):
        qs=Violation.objects.all()
        return render(request,self.template_name,{"data":qs}) 

        
class ViolationsUpdateView(View):
    template_name="update.html"
    form_class=ViolationForm
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        object=Violation.objects.get(id=id)
        form_instance=self.form_class(instance=object)
        return render(request,self.template_name,{"form":form_instance})
    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        object=Violation.objects.get(id=id)
        form_data=request.POST
        form_instance=self.form_class(form_data,instance=object)
        if form_instance.is_valid():
            form_instance.save()
            return redirect("list")
        return render(request,self.template_name,{"form":form_instance})

