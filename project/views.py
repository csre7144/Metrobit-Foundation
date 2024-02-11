from django.shortcuts import render,redirect
from .forms import feedback
from contact.forms import contactuser
# from project.models import feedbackform
# Create your views here.
def home(request):
      if request.method == 'POST':
            name = request.POST['name']
            phone_number = request.POST['phone_number']
            email = request.POST['email']
            message = request.POST['message']
            data = feedback(name=name, phone_number=phone_number, email=email, message=message)
            data.save()
      return render(request, 'index.html')

def about(request):
      return render(request, 'about.html')

def contact(request):
      if request.method == 'POST':
            name1 = request.POST['name1']
            phone1 = request.POST['phone1']
            email1 = request.POST['email1']
            txt = request.POST['txt']
            message1 = request.POST['message1']
            data1 = contactuser(name1=name1, phone1=phone1, email1=email1, txt=txt, message1=message1)
            data1.save()
      return render(request, 'contact.html')

def event(request):
      return render(request, 'events.html')

def divyangevent(request):
      return render(request, 'divyangexpo.html')