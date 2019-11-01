from django.shortcuts import render,HttpResponse, get_object_or_404, redirect
from mechanic_assign.models import *
from mechanic_assign.forms import bookingform
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.http import HttpResponse 





def index(request):
   
    return render(request, 'index.html')
    
def user_profile(request):
    service_list = services.objects.all()
    my_bookings = booking.objects.filter(client = request.user).order_by('-id')
    my_comparision = comparison.objects.all()
   
    print(my_bookings)
    if request.method == "POST":
        if request.POST.get('form-type') == "vehicle_add":
           
            car_info = car()
            car_info.make = request.POST.get('make')
            car_info.model = request.POST.get('model')
            car_info.year = request.POST.get('year')
            car_info.username = request.user
            car_info.save()
        else:
           
            user_booking = booking()
            user_booking.services = get_object_or_404(services, id= request.POST.get('services'))
            user_booking.date = request.POST.get('date')
            user_booking.time = request.POST.get('time')
            user_booking.address = request.POST.get('address')
            user_booking.client = request.user
            user_booking.is_inspection = False
            user_booking.save()
    return render(request, 'user_profile.html', {'services':service_list, 'booking': my_bookings, 'comparision': my_comparision})
    
    
# booking page-contact.html

def contact(request):
    services_list = services.objects.all()
    if request.method == "POST":
        user = CustomUser()
        user.first_name = request.POST.get('customer_fname')
        user.last_name = request.POST.get('customer_lname')
        user.email = request.POST.get('email_address')
        user.phone_number = request.POST.get('phone_number')
        user.username = request.POST.get('customer_fname') + "_" + request.POST.get('customer_lname')
        user.save()
        car_info = car()
        car_info.make = request.POST.get('make')
        car_info.model = request.POST.get('model')
        car_info.year = request.POST.get('year')
        car_info.username = user
        car_info.save()
        user_booking = booking()
        user_booking.services = get_object_or_404(services, id= request.POST.get('services'))
        user_booking.date = request.POST.get('date')
        user_booking.time = request.POST.get('time')
        user_booking.address = request.POST.get('location')
        user_booking.client = user
        if request.POST.get('is_inspection'):
            user_booking.is_inspection = True
        else:
            user_booking.is_inspection = False
        user_booking.save()
    return render(request, 'contact.html', {'services':services_list })
   

    

def user_employee(request):

    return render(request, 'user_employee.html')
    
    
def service(request):
    return render(request, 'services.html')
    
def signup_login(request):
    if request.method == "POST":
        if request.POST.get('f_type') == "registration":
            user = CustomUser()
            user.first_name = request.POST.get('customer_fname')
            user.last_name = request.POST.get('customer_lname')
            user.email = request.POST.get('email_address')
            user.phone_number = request.POST.get('phone')
            user.password = make_password(request.POST.get('password'))
            user.username = request.POST.get('username')
            user.is_customer = True
            user.is_employee = False
            user.save()
        else:
            print(request.POST.get('username'))
            user = authenticate(username = request.POST.get('username'), password = request.POST.get('password'))
            if user:
                login(request, user)
                if user.is_employee:
                    return redirect(dashboard)
                else:
                    return redirect(user_profile)

    return render(request, 'signup_login.html')
    
    
def dashboard(request):
    my_bookings = booking.objects.all().order_by('-id')

    if request.method == 'POST': 
       
        if request.POST.get("f_type") == "complete":
            print(request.POST.get("booking_id"))
            c_booking = get_object_or_404(booking, pk= request.POST.get("booking_id"))
            c_booking.is_completed = True
            c_booking.save()
    return render(request, 'dashboard.html', { 'booking': my_bookings,}) 


def user_edit(request):
    update_list = customers.objects.all()
    if request.method == "POST":
        user = CustomUser()
        user.first_name = request.POST.get('customer_fname')
        user.last_name = request.POST.get('customer_lname')
        user.email = request.POST.get('email')
        user.phone_number = request.POST.get('phone')
        user.address = request.POST.get('address')
        user.save()
    return render(request, 'user_edit.html', {'customers':update_list,})
    
# uploading images
def upload_image(request, id):
    my_booking = get_object_or_404(booking, pk = id)
    if request.method == "POST":
        user_upload = comparison()
        user_upload.before_image = request.FILES['before_img'] 
        user_upload.booking = my_booking
        user_upload.after_image = request.FILES['after_img']
        user_upload.save()
    return render(request, 'upload_image.html')
    
 # viewing images   
def booking_view(request, id):
    
    my_booking = get_object_or_404(booking, pk = id)
    print(my_booking.id)
    comparision_photos = comparison.objects.all()
    
    comp_phot = []
    print(comp_phot)
    if comparision_photos:
        for pic in comparision_photos:
            print(pic.booking.id)
            if pic.booking.id == my_booking.id:
                comp_phot.append(pic)
                
    
    return render(request, 'booking_view.html', {'image_list' : comp_phot, 'booking' : my_booking})
    
def logout_view(request):
    logout(request)
    return redirect(index)