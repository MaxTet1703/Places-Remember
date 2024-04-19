from django.shortcuts import render, redirect
from django.contrib.auth import logout
# Create your views here.


def start_page(request):
    return render(request, 'startpage.html')

def main_page(request):
    print(request.user.is_authenticated)
    return render(request, 'main.html')

def logout_user(request):
    logout(request)
    return redirect('login')
