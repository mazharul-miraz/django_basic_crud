from django.shortcuts import render
from .forms import StudentForm
from .models import studentInfo


# Create your views here.


def home(request):
    if request.method == 'POST':
        fm = StudentForm(request.POST)
        if fm.is_valid():
            name = fm.changed_data['name']
            email = fm.changed_data['email']
            address = fm.changed_data['address']
            reg = studentInfo(name = name, email = email, address = address)
            reg.save()
            print(name)
    # if a GET (or any other method) we'll create a blank form
    else:
        fm = StudentForm()
    return render(request,'index.html',{'form':fm})


def view(request):
    context= {}
    context ['studentInfo'] = studentInfo.objects.all()
    return render(request,'view.html')