from django.shortcuts import render, HttpResponse, redirect
from .forms import SignUpForm
import json
import requests


def home(request):
    user = request.user
    data = []
    if request.method == "POST" and request.is_ajax():
        coockie_consent = eval(request.POST.get('coockie_consent'))
        user.accept_cookie = coockie_consent
        user.save()
        data = {'coockie_consent': user.accept_cookie}
        return HttpResponse(json.dumps(data), content_type='application/json')
    if user.accept_cookie:
        url = 'https://api.imgflip.com/get_memes'
        r = requests.get(url = url)
        data = r.json().get('data',{}).get('memes')[:5]
    return render(request, 'account/home.html', {'data':data, 'coockie_consent':user.accept_cookie})   


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'account/sign_up.html', {'form': form})