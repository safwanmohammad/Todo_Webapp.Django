from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import TodoForm
from .models import Task_todo
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView


class TasklistView(ListView):
    model = Task_todo
    template_name = 'home.html'
    context_object_name = 'task'


class TaskDetailView(DetailView):
    model = Task_todo
    template_name = 'details.html'
    context_object_name = 'task'


class TaskUpdateView(UpdateView):
    model = Task_todo
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name', 'priority', 'date')

    def get_success_url(self):
        return reverse_lazy('cbvdetails', kwargs={'pk': self.object.id})


class TaskDeleteView(DeleteView):
    model = Task_todo
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')


# Create your views here.
def add_todo(req):
    task1 = Task_todo.objects.all()
    if req.method == "POST":
        name = req.POST.get('name', '')
        priority = req.POST.get('priority', '')
        date = req.POST.get('date', '')
        task = Task_todo(name=name, priority=priority, date=date)
        task.save()

    return render(req, 'home.html', {'task': task1})


# def details(req):
#     task = Task_todo.objects.all()
#     return render(req, 'details.html', )

def delete_todo(req, task_id):
    task = Task_todo.objects.get(id=task_id)
    if req.method == "POST":
        task.delete()
        return redirect('/')
    return render(req, 'delete.html', {'task1': task})


def update_todo(req, task_id):
    task = Task_todo.objects.get(id=task_id)
    f = TodoForm(req.POST or None, instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(req, 'edit.html', {'f': f, 'task': task})
