from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Checklist

def checklist_list(request):
    checklist = Checklist.objects.all()
    return render(request, 'checklist/checklist_list.html', {'checklist': checklist})

def checklist_detail(request, pk):
    checklist = get_object_or_404(Checklist, pk=pk)
    return render(request, 'checklist/checklist_detail.html', {'checklist': checklist})

class ChecklistListView(ListView):
    context_object_name = 'checklist'
    model = Checklist

    def get_context_data(self, **kwargs):
        context = super(ChecklistListView, self).get_context_data(**kwargs)
        context['checklistlist'] = []
        for each in context['checklist']:
            context['checklistlist'].append({'url': each.get_absolute_url(), 'text': each})
        return context

class ChecklistDetailView(DetailView):
    model = Checklist

class ChecklistCreateView(CreateView):
    fields = ('title', 'start_date', 'end_date', 'description', 'category', 'completed')
    model = Checklist

class ChecklistUpdateView(UpdateView):
    fields = ('title', 'start_date', 'end_date', 'description', 'category', 'completed')
    model = Checklist

class ChecklistDeleteView(DeleteView):
    model = Checklist
    success_url = '/checklist/'