from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def staff_login(request):
    # If already logged in, redirect straight to general page
    if request.user.is_authenticated:
        return redirect("general_exam_page")

    if request.method == "POST":
        username = request.POST.get("username")  # 👈 changed from staff_id
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("general_exam_page")  # ✅ redirect after success
        else:
            messages.error(request, "Invalid Username or Password.")
    
    return render(request, "reports/staff_portal.html")


@login_required(login_url="/")  # 👈 redirect to login if not logged in
def general_exam_page(request):
    return render(request, "reports/general_page.html")


def staff_logout(request):
    logout(request)
    return redirect("staff_login")


def exam_result_view(request):
    return render(request, 'reports/exam_result.html')  # You'll need to create this template


@login_required(login_url="/")
def staff_broadsheet(request):
    return render(request, "reports/staff_broadsheet.html")
