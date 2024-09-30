from django.shortcuts import redirect, render

from login.forms import userform
from login.models import User
from django.contrib import messages, auth

# Create your views here.
def registeruser(request):
    if request.method == 'POST':
        user_form = userform(request.POST)
        if user_form.is_valid():
            first_name = user_form.cleaned_data['first_name']
            last_name = user_form.cleaned_data['last_name']
            username = user_form.cleaned_data['username']
            email = user_form.cleaned_data['email']
            password = user_form.cleaned_data['password']
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
            user.role = User.CUSTOMER
            user.save()
            return redirect('login')
        else:
            print("Invalid form")
            print(user_form.errors)
    else:
        user_form = userform()
            
    context = {
        'user_form':user_form,
    }
    return render(request,'registeruser.html',context)

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user =  auth.authenticate(email = email,password = password)

        if user is not None:
            auth.login(request,user)
            return redirect("dashboard")
        else:
            messages.error(request,"your credentials is not matched")
            return redirect('login')

    return render(request,'login.html')

def dashboard(request):
    return render(request,"dashboard.html")