from django.shortcuts import render


def welcome_view(request):
    return render(request, 'reports/welcome.html')  # You'll need to create this template