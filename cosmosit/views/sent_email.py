from django.shortcuts import redirect, render
from django.http import request

def sent_email(request):
    return render(request, 'sections/sent-email.html',context={})