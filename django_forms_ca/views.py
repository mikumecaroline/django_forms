from django.shortcuts import render

from . form import UserReg

def Reg(request):
    submit_button = request.POST.GET("carol")
    name = ''
    email = ''
    password = ''

    rForm = UserReg(request.POST or None)
    if rForm.is_valid():
        name = rForm.cleaned_data.get("name")
        email = rForm.cleaned_data.get("email")
        password = rForm.cleaned_data.get("password")

        context = {
            'rForm': rForm,
            'name': name,
            'email': email,
            'submit_button': submit_button
        }