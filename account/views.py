from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render

from .forms import LoginForm


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request, username=cd["username"], password=cd["password"]
            )
            if user is not None:
                if user.is_active:
                    # set the user in the session by calling login method
                    login(request, user)
                    return HttpResponse("Authenticated successfully")
                else:
                    # data is valid but account is not acitve
                    return HttpResponse("Disabled account")
            else:
                # form error e.g. user didn't fill in correctly
                return HttpResponse("Invalid login")
    else:
        # Instantiate a new login form for GET request
        form = LoginForm()
    return render(
        request, "account/login.html", {"form": form}
    )  # Create your views here.
