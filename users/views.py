from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserForm, UserTypeForm, DepartmentForm, RankForm, TaskAssignmentForm, CustomLoginForm
from .models import User, UserType, Department, Rank
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth import login as auth_login

# Create your views here.
def index(request):
    user_count = User.objects.count()
    department_count = Department.objects.count()
    context = {
        'user_count': user_count,
        'department_count': department_count
    }
    return render(request, 'index.html', context)




""""class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    authentication_form = CustomLoginForm

    def form_valid(self, form):
        auth_login(self.request, form.get_user())
        return redirect('index') """""


def add_type(request):
    if request.method == "POST":
        form = UserTypeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/list_type')
            except:
                pass
    else:
        form = UserTypeForm()
    return render(request, 'add_type.html', {'form': form})


def list_type(request):
    usertypes = UserType.objects.all()
    return render(request, "list_type.html", {'usertypes': usertypes})


def delete_type(request, id=0):
    usertype = UserType.objects.get(id=id)
    usertype.delete()
    return redirect('/list_type')


def edit_type(request, id):
    usertype = UserType.objects.get(id=id)
    return render(request, 'edit_type.html', {'usertype': usertype})


def update_type(request, id):
    usertype = UserType.objects.get(id=id)
    form = UserTypeForm(request.POST, instance=usertype)
    if form.is_valid():
        form.save()
        return redirect("/list_type")
    return render(request, 'edit_type.html', {'usertype': usertype})


def add_rank(request, ):
    if request.method == "POST":
        form = RankForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/list_rank')
            except:
                pass
    else:
        form = RankForm()
    return render(request, 'add_rank.html', {'form': form})


def list_rank(request):
    ranks = Rank.objects.all()
    return render(request, "list_rank.html", {'ranks': ranks})


def edit_rank(request, id):
    rank = Rank.objects.get(id=id)
    return render(request, 'edit_rank.html', {'rank': rank})


def update_rank(request, id):
    rank = Rank.objects.get(id=id)
    form = RankForm(request.POST, instance=rank)
    if form.is_valid():
        form.save()
        return redirect("/list_rank")
    return render(request, 'edit_rank.html', {'rank': rank})


def delete_rank(request, id=0):
    rank = Rank.objects.get(id=id)
    if request.method == 'POST':
        rank.delete()
        return redirect('/list_rank')
    return render(request, 'confirm_delete_rank.html', {'rank': rank})



def add_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/list_user')
            except:
                pass
    else:
        form = UserForm()
    return render(request, 'add_user.html', {'form': form})


def list_user(request):
    users = User.objects.all()
    return render(request, "list_user.html", {'users': users})


def list_dep(request):
    departments = Department.objects.all()
    return render(request, "list_dep.html", {'departments': departments})


def add_dep(request):
    if request.method == "POST":
        form = DepartmentForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/list_dep')
            except:
                pass
    else:
        form = DepartmentForm()
    return render(request, 'add_dep.html', {'form': form})


def delete_dep(request, id=0):
    department = Department.objects.get(id=id)
    department.delete()
    return redirect('/list_dep')


def edit_dep(request, id):
    department = Department.objects.get(id=id)
    return render(request, 'edit_dep.html', {'department': department})


def update_dep(request, id):
    department = Department.objects.get(id=id)
    form = DepartmentForm(request.POST, instance=department)
    if form.is_valid():
        form.save()
        return redirect("/list_dep")
    return render(request, 'edit_dep.html', {'department': department})


def team_lead(request):
    return render(request, 'teamlead/team_lead.html')

def so2(request):
    return render(request, 'SO2/so2.html')

def director(request):
    return render(request, 'director/director.html')

def co(request):
    return render(request, 'co/co.html')