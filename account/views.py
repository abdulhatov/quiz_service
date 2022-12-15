from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from .forms import (
    AccountRegisterForm,
    AccountLoginForm,
)


class AccountRegisterView(TemplateView):
    template_name = "account/registration.html"

    def get(self, request):
        form = AccountRegisterForm()
        context = {
            'form':form,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = AccountRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.clean_password2())
            user.save()
            return redirect("account:login")
        return render(request, "account/errors.html", {'form':form})


class AccountLoginView(TemplateView):
    template_name = "account/login.html"

    def get(self, request):
        form = AccountLoginForm()
        context = {
            'form':form,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = AccountLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('quiz:quiz')
            else:
                return render(request, 'account/errors.html', {'form':"Username or password is not correct"})
        return render(request, "account/errors.html", {'form':form})

