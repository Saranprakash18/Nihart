from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login_view(request):
    return render(request, 'auth.html')

def main_view(request):
    return render(request, 'main.html')

def seller_view(request):
    return render(request, 'seller.html')
