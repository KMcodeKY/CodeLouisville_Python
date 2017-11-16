from django.db.models import F
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from .filters import ChecklistFilter
from .forms import ChecklistForm
from .models import Checklist

#Detail view summary for individual checklist item
def checklist_detail(request, pk):
    checklist = get_object_or_404(Checklist, pk=pk)
    return render(request, 'checklist/checklist_detail.html', {'checklist': checklist})

#Generic - Detail view summary for individual checklist item
class ChecklistDetailView(DetailView):
    model = Checklist

#Generic - Create view for new checklist item
class ChecklistCreateView(CreateView):
    model = Checklist
    form_class = ChecklistForm

#Generic - Update view for existing checklist item
class ChecklistUpdateView(UpdateView):
    model = Checklist
    form_class = ChecklistForm

#Generic - Delete view for existing checklist item
class ChecklistDeleteView(DeleteView):
    model = Checklist
    success_url = '/checklist/'

#Filter view for all checklist items (Main Display Page)
def checklist_filter_list(request):
    #Order by completed date, then end date, then start date
    checklist_queryset = Checklist.objects.all().order_by('completed', F('end_date').asc(nulls_last=True), F('start_date').asc(nulls_last=True))

    f = ChecklistFilter(request.GET, queryset=checklist_queryset)
    return render(request, 'checklist/checklist_filter.html', {'filter': f})