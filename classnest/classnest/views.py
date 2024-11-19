# classNest/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# classNest/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from classnest_Base.forms import UserUpdateForm, ProfileUpdateForm

@login_required
def profile_view(request):
    # Check if the logged-in user has a profile; if not, create one
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        # Create a profile for the user if it doesn't exist yet
        profile = Profile.objects.create(user=request.user)

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

    return render(request, 'classNest/profile.html', context)