from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserForm
from django.contrib.auth.models import User


@login_required
def user_detail(request):
    return render(request, 'registration/user_detail.html')

@login_required
def user_edit(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return render(request, 'registration/user_detail.html')
    else:
        form = UserForm(instance=request.user)

    return render(request, 'registration/user_edit.html', {'form': form})
