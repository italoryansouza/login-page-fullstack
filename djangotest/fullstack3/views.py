from django.shortcuts import render
from .forms import RegisterForm, LoginForm


def register(request):  
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user= form.save(commit= False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect("Home")
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user= form.get_user()
            login(request, user)
            return redirect("Welcome")
    else:
        form= LoginForm()

    return render(request, 'login.html', {'form': form})
# Create your views here.
