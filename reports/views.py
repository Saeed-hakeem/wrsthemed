from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import TaskForm, ProjectForm, FeedbackForm, ReportForm
from .models import Project, Task, Report, Feedback

# Create your views here.
def task_assignment(request, task_id=None):
    # If task_id is provided, retrieve the existing task for editing
    if task_id:
        task = get_object_or_404(Task, id=task_id)
    else:
        task = None

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('success_page')  # Replace with your success page or URL
    else:
        form = TaskForm(instance=task)

    return render(request, 'task_assignment.html', {'form': form})

def view_task(request):
    tasks = Task.objects.all()
    return render(request, 'view_task.html', {'tasks': tasks})



def reports(request):
    return render(request, 'reports.html')

def so2_report(request):
    return render(request, 'so2_report.html')







def add_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/view_project')
            except:
                pass
    else:
        form = ProjectForm()
    return render(request, 'projects.html', {'form': form})


def view_project(request):
    projects = Project.objects.all()
    return render(request, 'view_project.html', {'projects': projects})


def feedback(request):
    return render(request, 'feedback.html')



def view_project(request):
    projects = Project.objects.all()
    return render(request, 'view_project.html', {'projects': projects})

# View details of a single project
"""""@login_required
def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    tasks = Task.objects.filter(project=project)
    return render(request, 'projects/project_detail.html', {'project': project, 'tasks': tasks})

# Create a new project
@login_required
def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/view_project')
    else:
        form = ProjectForm()
    return render(request, 'projects.html', {'form': form})

# Update an existing project
@login_required
def project_update(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'projects/project_form.html', {'form': form})

# Delete a project
@login_required
def project_delete(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == 'POST':
        project.delete()
        return redirect('project_list')
    return render(request, 'projects/project_confirm_delete.html', {'project': project})

# Assign tasks to a project
@login_required
def assign_task(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.project = project
            task.save()
            return redirect('project_detail', project_id=project.id)
    else:
        form = TaskForm()
    return render(request, 'projects/task_form.html', {'form': form, 'project': project})

# View tasks for a specific project
@login_required
def view_tasks(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    tasks = Task.objects.filter(project=project)
    return render(request, 'projects/task_list.html', {'tasks': tasks, 'project': project})"""""