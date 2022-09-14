import email
from unicodedata import name
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from .models import User
from .forms import StudentRegistration

def home(request):
    form = StudentRegistration()
    stud = User.objects.all()
    return render(request,'home.html',{'form':form,'stu':stud})
    
@csrf_exempt
def save_data(request):
    if request.method == 'POST':
        form = StudentRegistration(request.POST)
        if form.is_valid():
            name = request.POST['name']
            email = request.POST['email']
            password = request.POST['password']
            usr = User(name = name, email = email, password = password)
            usr.save()
            stud = User.objects.values()
            student_data = list(stud)
            return JsonResponse({'status':'Save', 'student_data':student_data})
        else:
            return JsonResponse({'status':'0'})