from django.shortcuts import render

def home(request):
# Suggested code may be subject to a license. Learn more: ~LicenseLog:1777738098.
    return render(request, 'home.html')
