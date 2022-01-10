from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from . models import Person, Students
from . forms import PersonForm, SignupForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
@login_required(login_url='login')
def home(request):
    dynamicdata = Person.objects.all()  # CRUD #ORM
    dynastu = Students.objects.all()

    # print(dynamicdata)
    context = {'dynamic': dynamicdata, 'dyna': dynastu}
    return render(request, 'home.html', context)


def update(request, id):  # GET#PUT#POST
    z = Person.objects.get(pk=id)
    form = PersonForm(instance=z)  # old data
    if request.method == 'POST':
        form = PersonForm(request.POST, instance=z)
        if form.is_valid():
            form.save()
            return redirect('/app/home/')
    context = {'form': form}
    return render(request, 'update.html', context)


def delete(request, id):
    Person.objects.get(pk=id).delete()
    messages.info(request, "no data to show")
    return render(request, 'delete.html')
    # return redirect('/app/home')


def read(request, id):
    print(id)
    dynamicdata = Person.objects.get(pk=id)
    context = {'dynamic': dynamicdata}
    return render(request, 'read.html', context)

    # return HttpResponse('This is a read fuction')


def create(request):  # POST
    form = PersonForm()
    if request.method == 'POST':  # TRUE
        # breakpoint()
        print(request.POST)
        form = PersonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print('data saved')
        return redirect("/app/home/")
    context = {'form': form}
    return render(request, 'create.html', context)


def signup(request):
    form = SignupForm()
    if request.method == 'POST':  # TRUE
        print(request.POST)
        form = SignupForm(request.POST)
        if form.is_valid():
            # breakpoint()
            form.save()
    context = {'form': form}
    return render(request, 'signup.html', context)


def loginn(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            if request.user.is_authenticated:
                username = request.user.username
                messages.warning(request, "welcome to homepage" + username)

            return redirect('/app/home')

    return render(request, 'login.html')


def logoutt(request):  # get
    logout(request)
    return redirect('/login')  

def jav(request): 
	return render(request, 'jav.html')
