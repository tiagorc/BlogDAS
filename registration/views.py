from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import UserForm


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
