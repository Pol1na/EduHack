from django.shortcuts import render
from .forms import LoginForm, UserRegistrationForm
from django.contrib.auth import login, authenticate  # add this
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm  # add this
from django.contrib import messages


class CreateUser(CreateView):
    form_class = UserRegistrationForm
    template_name = 'register.html'
    raise_exception = True


# #
def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                print(username)
                print(password)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('test')
            else:
                return redirect('test')

        else:
            return redirect('test')

    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})

# class LoginUser(LoginView):
#     template_name = 'login.html'
#     form_class = AuthenticationForm
#

def test(request):
    return render(
        request,
        'test.html',
    )


#
# def login(request):
#     return render(request, 'news/login.html')
def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password1'])
            # Save the User object
            new_user.save()
            return redirect('login')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'register.html', {'user_form': user_form})
