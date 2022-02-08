from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, User, PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from .models import Profile
from django.http import Http404
# Create your views here.

def register(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            User.objects.create_user(username=username, password=password) # 数据入库

            new_user = authenticate(username=username, password=password)
            if new_user:
                login(request, new_user)
            return redirect('blogs:index')

    context = {'form': form}
    # 渲染注册页面，它要么显示一个空表单，要么显示提交的无效表单
    return render(request, 'registration/register.html', context)

@login_required
def change_pwd(request, user_id):
    if request.method != 'POST':
        form = PasswordChangeForm(user=request.user)
    else:
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('blogs:homepage', user_id=user.id)
    context = {'form': form}
    return render(request, 'registration/change_pwd.html', context)

@login_required
def profile_edit(request, user_id):
    user = User.objects.get(id=user_id)
    if Profile.objects.filter(user_id=user_id).exists():
        profile = Profile.objects.get(user_id=user_id)
    else:
        profile = Profile.objects.create(user=user)
    if user != request.user:
        raise Http404
    if request.method != 'POST':
        form = ProfileForm(instance=profile)
    else:
        form = ProfileForm(instance=profile,data=request.POST, files=request.FILES)
        if form.is_valid():
            profile_clean_data = form.cleaned_data
            profile.mail = profile_clean_data['mail']
            profile.bio = profile_clean_data['bio']
            if 'avatar' in request.FILES:
                profile.avatar = profile_clean_data['avatar']
            profile.save()
            return redirect('blogs:homepage', user_id=user.id)

    context = {'form': form, 'profile': profile}
    return render(request, 'registration/profile_edit.html', context)
