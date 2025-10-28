from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.views.decorators.http import require_http_methods

from tasks.forms import TaskForm
from .models import Task


@login_required
def index(request):
    show_hidden_tasks = 'show_hidden' in request.GET
    
    tasks = (
        request.user.tasks.all()
        if show_hidden_tasks
        else request.user.tasks.filter(hidden=False)
    ).order_by('-created_at')
    
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
    form = TaskForm(request.POST, initial={'user': request.user})
    if form.is_valid():
        is_first_task = not Task.objects.filter(user=request.user, hidden=False).exists()
        task = form.save(commit=False)
        task.user = request.user
        task.save()
        context = {'task': task}
        response = render(request, 'partials/task-row.html', context)
        response['HX-Trigger'] = 'create-task-success'
        if is_first_task:
            response['HX-Retarget'] = '#no-task-row'
            response['HX-Reswap'] = 'outerHTML'
        return response
    else:
        response = render(request, 'partials/add-task-form.html', {'form': form})
        response['HX-Retarget'] = '#add-task-form'
        response['HX-Reswap'] = 'outerHTML'
        return response


@login_required
def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    form = TaskForm(instance=task)
    context = {'task': form.instance, 'form': form}
    response = render(request, 'partials/edit-task-form.html', context)
    response['HX-Trigger'] = 'edit-task-success'
    return response


@login_required
@require_http_methods(['POST'])
def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    form = TaskForm(request.POST, instance=task)
    if form.is_valid():
        task = form.save()
        context = {'task': task}
        response = render(request, 'partials/task-row.html', context)
        response['HX-Trigger'] = 'update-task-success'
        return response
    else:
        context = {'task': form.instance, 'form': form}
        response = render(request, 'partials/edit-task-form.html', context)
        response['HX-Retarget'] = '#edit-task-form'
        return response


@login_required
@require_http_methods(['DELETE'])
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.delete()
    was_last_task = not Task.objects.filter(user=request.user, hidden=False).exists()
    if was_last_task:
        return render(request, 'partials/no-task-row.html')
    return HttpResponse(status=200)


@login_required
@require_http_methods(['POST'])
def show_hide_task(request, pk):
    is_first_task = not Task.objects.filter(user=request.user, hidden=False).exists()

    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.hidden = not task.hidden
    task.save()

    was_last_task = not Task.objects.filter(user=request.user, hidden=False).exists()

    if task.hidden:
        if was_last_task:
            return render(request, 'partials/no-task-row.html')
        return HttpResponse(status=200)
    else:
        context = {'task': task}
        response = render(request, 'partials/task-row.html', context)
        if is_first_task:
            response['HX-Retarget'] = '#no-task-row'
        return response
