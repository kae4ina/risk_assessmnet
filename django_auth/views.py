from django.shortcuts import render, redirect

def main_menu(request):
    return render(request,'templates/main_menu.html')