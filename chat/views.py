from django.http import Http404, HttpResponse, request
from django.contrib.auth.models import User

from django.template import loader
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.core.files import File
from django.core.files.storage import FileSystemStorage
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Room
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from chat.forms import UserForm


class UserFormView(View):
    template_name = 'chat/register.html'
    error = 0

    def get(self,request):
        if request.user.is_authenticated():
            return redirect('list')
        request.session['enter']=False
        error = 0
        return render(request,self.template_name,{'error':error})


    def post(self,request):
        if(request.POST.get('type',None)=='1'):
            username=request.POST.get('Username',None)
            password=request.POST.get('Password',None)
            email=request.POST.get('email',None)
            print(username)
            if(username=="" or password==""  or email==""):
                return render(request, self.template_name, {'error': 3})

            try:
                if User.objects.get(username=username):
                    return render(request,self.template_name,{'error':2})
            except:

                User.objects.create_user(username=username, password=password, email=email)
                user = authenticate(username=username, password=password)
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        rooms=Room.objects.all()
                        return(redirect('list'))
        else:
            username = request.POST.get('Username', None)
            password = request.POST.get('Password', None)
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    rooms = Room.objects.all()
                    return (redirect('list'))
            else:
                return render(request,self.template_name,{'error':1})

class rlist(View):

    rooms = Room.objects.all()
    error=0

    def get(self, request):
        if request.user.is_authenticated():
            print("Logged in")
            rooms = Room.objects.all()
            error = 0
            return render(request,"chat/index1.html",{'rooms':rooms,'error':error})
        else:
            return redirect('reg')
    def post(self,request):
        type=request.POST.get('type', None)
        if(type=='2'):
            name = request.POST.get('name', None)
            password = request.POST.get('pass', None)
            room=Room()
            room.name=name
            room.password=password
            room.save()
            rooms = Room.objects.all()

            return render(request, "chat/index1.html", {'rooms': rooms})
        else:
            password = request.POST.get('pass', None)
            id=request.POST.get('id', None)

            print(password)
            print(Room.objects.get(id=id));
            if(password==Room.objects.get(id=id).password):
                request.session['enter'] = True
                return (redirect('room',room=id))
            else:
                rooms = Room.objects.all()
                error = 1
                return render(request,"chat/index1.html",{'rooms':rooms,'error':error})




@login_required(login_url='/')
def chatting(request,room):

    if('enter' in request.session):
        if(request.session['enter']==True):
            room2=Room.objects.get(id=int(room))
            print(room2.pk)

            room={'room':room2}
            return render(request,'chat/chatting.html',room)
        else:
            return redirect('list')

    else:
        return redirect('list')


@login_required(login_url='/')
def videochat(request,room1):

    room2 = Room.objects.get(id=int(room1))

    room = {'room': room2}
    print(room2.name)

    return render(request,'chat/videochat.html',room)
@login_required(login_url='/')
def logout1(request):
    del request.session['enter']

    logout(request)
    return (redirect('reg'))



