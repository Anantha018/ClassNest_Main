# classnest_Base/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib.auth.models import Group
from django.contrib import messages

from django.contrib.auth import update_session_auth_hash, logout as auth_logout
from .forms import UserUpdateForm, ProfileUpdateForm, PasswordResetForm


# classNest/views.py
from django.shortcuts import redirect

def home(request):
    return redirect('dashboard')  # Redirect to dashboard page



# Create groups if they don’t already exist
def create_user_groups():
    Group.objects.get_or_create(name='Student')
    Group.objects.get_or_create(name='Instructor')


create_user_groups()

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        user_type = request.POST.get('user_type')
        if form.is_valid():
            user = form.save()
            # Assign the user to the correct group
            if user_type == 'student':
                group = Group.objects.get(name='Student')
            elif user_type == 'instructor':
                group = Group.objects.get(name='Instructor')
            user.groups.add(group)

            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'classnest_Base/register.html', {'form': form})


@login_required
def dashboard_view(request):
    # Debugging: Print user and their groups
    print(f"User: {request.user}")
    print(f"User groups: {request.user.groups.all()}")

    # Check if the user is in the 'Instructor' group
    is_instructor = request.user.groups.filter(name='Instructor').exists()
    
    # Debugging: Print the result of the check
    print(f"Is instructor: {is_instructor}")
    
    return render(request, 'classnest_Base/dashboard.html', {'is_instructor': is_instructor})


@login_required
def create_course_view(request):
    if request.method == "POST":
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            course = form.save(commit=False)
            course.instructor = request.user
            course.save()
            return redirect('dashboard')  # Redirect to the dashboard or another page after creating the course
        else:
            print("Form errors:", form.errors)
    else:
        form = CourseForm()  # Initialize an empty form for GET requests

    return render(request, 'classnest_Base/create_course.html', {'form': form})

@login_required
def courses_view(request):
    is_instructor = request.user.groups.filter(name='Instructor').exists()  # Use 'Instructor' instead of 'Instructors'
    courses = Course.objects.all()
    return render(request, 'classnest_Base/courses.html', {'courses': courses, 'is_instructor': is_instructor})



@login_required
def course_detail_view(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    is_instructor = request.user == course.instructor
    return render(request, 'classnest_Base/course_detail.html', {
        'course': course,
        'is_instructor': is_instructor
    })


    
@login_required
def delete_course_view(request, course_id):
    # Get the course object or return a 404 error if not found
    course = get_object_or_404(Course, id=course_id)
    
    # Check if the user is the instructor who created the course or an admin
    if request.user == course.instructor or request.user.is_superuser:
        course.delete()  # Delete the course
        # Redirect to the courses page with a success message (optional)
        return redirect('courses')
    else:
        # If the user is not authorized, return a forbidden response
        return HttpResponseForbidden("You are not allowed to delete this course.")  


#profile
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    
    return render(request, 'classnest_Base/profile.html', context)

@login_required
def reset_password(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            new_password1 = form.cleaned_data.get('new_password1')
            request.user.set_password(new_password1)
            request.user.save()
            update_session_auth_hash(request, request.user)  # Keeps user logged in after password change
            return redirect('profile')
    else:
        form = PasswordResetForm()

    return render(request, 'classnest_Base/password_change.html', {'form': form})

@login_required
def logout_view(request):
    auth_logout(request)
    return redirect('login')