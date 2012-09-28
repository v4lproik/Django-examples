# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.core.context_processors import csrf
from django.template import RequestContext


def homepage(request):
    
    c = {}
    c.update(csrf(request))
    
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "You are successfully logged in!"
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."

        return render_to_response('login.html', {'state':state, 'username': username}, RequestContext(request))
    else:
        return render_to_response("login.html", c)
    