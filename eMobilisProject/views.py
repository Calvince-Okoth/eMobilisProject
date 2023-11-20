from django.shortcuts import render


def home(request):
    return render(request, 'index.html')
def style(request):
    return render(request, 'company.html')