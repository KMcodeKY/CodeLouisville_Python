from django.db.models import F
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from .filters import ChecklistFilter
from .forms import ChecklistForm
from .models import Checklist

def checklist_detail(request, pk):
    checklist = get_object_or_404(Checklist, pk=pk)
    return render(request, 'checklist/checklist_detail.html', {'checklist': checklist})

class ChecklistDetailView(DetailView):
    model = Checklist

class ChecklistCreateView(CreateView):
    model = Checklist
    form_class = ChecklistForm

class ChecklistUpdateView(UpdateView):
    model = Checklist
    form_class = ChecklistForm

class ChecklistDeleteView(DeleteView):
    model = Checklist
    success_url = '/checklist/'

def checklist_filter_list(request):
    checklist_queryset = Checklist.objects.all().order_by('completed', F('end_date').asc(nulls_last=True))
    for each in checklist_queryset:
        each.detail_link = each.get_absolute_url()

    f = ChecklistFilter(request.GET, queryset=checklist_queryset)
    return render(request, 'checklist/checklist_filter.html', {'filter': f})