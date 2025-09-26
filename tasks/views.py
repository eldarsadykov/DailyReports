from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.db.models import Q
from django.views.decorators.http import require_http_methods

from tasks.forms import TaskForm


@login_required
def index(request):
    tasks = request.user.tasks.all().order_by('-created_at')
    form = TaskForm()
    context = {'tasks': tasks, 'form': form}
    return render(request, 'tasks.html', context)


@login_required
def search_tasks(request):
    query = request.GET.get('search', '')
    tasks = request.user.tasks.filter(
        Q(key__icontains=query) | Q(name__icontains=query)
    ).order_by(
        '-created_at'
    )
    context = {'tasks': tasks}
    return render(request, 'partials/task-list.html', context)


@login_required
@require_http_methods(['POST'])
def create_task(request):
    form = TaskForm(request.POST)
    if form.is_valid():
        task = form.save(commit=False)
        task.user = request.user
        task.save()
        context = {'task': task}
        response = render(request, 'partials/task-row.html', context)
        response['HX-Trigger'] = 'create-task-success'
        return response