from django.shortcuts import render,HttpResponse,get_object_or_404,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import ApplyScheme
from .models import AddCrops
from .models import Applicant
from .forms import ApplicationView
from .forms import AddCropsForm 
from .forms import ApplySchemeForm 


import json


# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render (request,'home.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        



    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('farmerhome')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')


def farmerhome(request):
    return render (request,'farmerhome.html')


def adminlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_staff:  # Check if the user is staff/admin
            login(request, user)
            # Redirect to a dashboard or any desired admin page upon successful login
            return redirect('adminhome')  # Update this with your admin page URL
        else:
            # Handle invalid login credentials
            error_message = "Invalid username or password."

    return render (request,'adminlogin.html')

def applyscheme(request):
    data = ApplyScheme.objects.all()
    return render(request, 'applyscheme.html', {'data': data})

    


def adminhome(request):
    return render(request,'adminhome.html')
def createscheme(request):
    if request.method == 'POST':
        sname = request.POST.get('schemeName')
        desc= request.POST.get('description')
        reqdocs = request.POST.get('requiredDocs')
        eligibility = request.POST.get('eligibility')
        lastdate = request.POST.get('lastDate')
        scheme=ApplyScheme(sname=sname,desc=desc,reqdocs=reqdocs,eligibility=eligibility,lastdate=lastdate)
        scheme.save()

        # You can modify the response as needed
        return JsonResponse({'message': 'Scheme added successfully'})

    return render(request, 'createscheme.html')
def viewscheme(request):
    data = ApplyScheme.objects.all()
    return render(request, 'viewscheme.html', {'data': data})

def addcrops(request):
    if request.method == 'POST':
        cname = request.POST.get('cname')
        desc= request.POST.get('desc')
        season = request.POST.get('season')
        soildetails = request.POST.get('soildetails')
        pesticides = request.POST.get('pesticides')
        crop=AddCrops(cname=cname,desc=desc,season=season,soildetails=soildetails,pesticides=pesticides)
        crop.save()

        # You can modify the response as needed
        return JsonResponse({'message': 'crop added successfully'})
    return render(request,'addcrops.html')

def viewcrops(request):
    data = AddCrops.objects.all()
    return render(request, 'viewcrops.html', {'data': data})

def cropdetails(request):
    data = AddCrops.objects.all()
    return render(request, 'cropdetails.html',{'data':data})



def apply(request):
    if request.method == 'POST':
        Applicant_Name = request.POST.get('Applicant_Name')
        monthly_income = request.POST.get('monthly_income')
        aadhar_card = request.FILES.get('aadhar_card')
        ration_card = request.FILES.get('ration_card')
        address = request.POST.get('address')
        apply_obj=Applicant(Applicant_Name=Applicant_Name,monthly_income=monthly_income,aadhar_card=aadhar_card,ration_card=ration_card,address=address)
        apply_obj.save()

        # Here you can perform further processing, validation, or save the data to a database

        # For example, printing the received data for demonstration purposes:
       

        return HttpResponse("Application submitted successfully!")

    return render(request, 'apply.html')

def userdetails(request):
    data = User.objects.all()
    return render(request, 'userdetails.html',{'data':data})



# def applicationlist(request):
#         applicants = Applicant.objects.all()
#         forms = ApplicationView(applicants)
#         return render(request, 'applicationlist.html', {'form': forms, 'applicants': applicants})

def applicationlist(request):
    if request.method == 'POST':
        for applicant in Applicant.objects.all():
            new_status = request.POST.get(f'status_{applicant.id}')
            if new_status in ['approved', 'rejected','pending']:
                applicant.status = new_status
                applicant.save()

        return redirect('applicationview')  # Redirect to the same page after updating

    applicants = Applicant.objects.exclude(status='approved')
    return render(request, 'applicationlist.html', {'applicants': applicants})

def update_status(request, item_id):
    item = get_object_or_404(Applicant, pk=item_id)
    if request.method == 'POST':
        status = request.POST.get('status')
        item.status = status
        item.save()
        return redirect('applicationlist')
    return render(request, 'update_status.html', {'item': item})

def viewApplication(request):
    data = request.object.filter()
    return render(request,'viewapplicationstatus.html',)


def myapplication(request):
    data = Applicant.objects.all()
    
    return render(request, 'myapplication.html',{'data':data})


def edit_crop(request, crop_id):
    crop = get_object_or_404(AddCrops, pk=crop_id)
    
    if request.method == 'POST':
        form = AddCropsForm(request.POST, instance=crop)
        if form.is_valid():
            form.save()
            return redirect('viewcrops')  # Redirect to a view after successful update
    else:
        form = AddCropsForm(instance=crop)
    
    return render(request, 'edit_crop.html', {'form': form, 'crop': crop})

def delete_crop(request, crop_id):
    crop = get_object_or_404(AddCrops, pk=item_id)
    crop.delete()
    return redirect('viewcrops')  

def edit_scheme(request, scheme_id):
    scheme = get_object_or_404(ApplyScheme, pk=scheme_id)
    
    if request.method == 'POST':
        form = ApplySchemeForm(request.POST, instance=scheme)
        if form.is_valid():
            form.save()
            return redirect('viewscheme')  # Redirect to a view after successful update
    else:
        form = ApplySchemeForm(instance=scheme)
    
    return render(request, 'edit_scheme.html', {'form': form, 'scheme': scheme})
def delete_scheme(request, scheme_id):
    scheme = get_object_or_404(ApplyScheme, pk=scheme_id)
    scheme.delete()
    return redirect('viewscheme')  
