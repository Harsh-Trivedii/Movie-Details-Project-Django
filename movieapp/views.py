from django.shortcuts import render,redirect
from movieapp.forms import MovieForm,SignUpForm
from movieapp.models import Movie
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# Create your views here.
def home_view(request):
    return render(request,'movieapp/home.html')

@login_required
def add_movies(request):
    form=MovieForm()
    if request.method=='POST':
        form=MovieForm(request.POST)
        if form.is_valid():
            form.save()
            print('Succesfully saved in the database')
        return redirect(home_view)
    context={
        'form':form,
    }
    return render(request,'movieapp/addmovies.html',context)

@login_required
def listmovie_view(request):
    movielist=Movie.objects.all()
    context={
        'movielist':movielist,
    }
    return render(request,'movieapp/movielist.html',context)

def logout(request):
    return render(request,'movieapp/logout.html')

def signup_view(request):
    form=SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login/')
    context={
        'form':form,
    }
    return render(request,'movieapp/signup.html',context)
    