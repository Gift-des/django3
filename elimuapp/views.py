from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def gallery(request):
    return render(request, 'gallery.html')

def information(request):
    return render(request, 'info.html')

def information2(request):
    return render(request, 'info2.html')

def Form(request):
    return render(request, 'Form.html')

def Login(request):
    return render(request, 'Login.html')

def Registration(request):
    return render(request, 'Registration.html')