from django.shortcuts import render

# For home page
def index(request):
    return render(request, 'index.html')

# For home page
def home(request):
    return render(request, 'index.html')

# For contact page
def contact(request):
    return render(request, 'contact.html')