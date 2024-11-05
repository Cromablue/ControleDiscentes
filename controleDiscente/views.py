from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Disciplina, Matricula
from .forms import DisciplinaForm, MatriculaForm

# Views para Disciplina
class DisciplinaListView(ListView):
    model = Disciplina
    template_name = 'disciplina_list.html'
    context_object_name = 'disciplinas'

class DisciplinaCreateView(CreateView):
    model = Disciplina
    form_class = DisciplinaForm
    template_name = 'disciplina_form.html'
    success_url = reverse_lazy('disciplina_list')

class DisciplinaUpdateView(UpdateView):
    model = Disciplina
    form_class = DisciplinaForm
    template_name = 'disciplina_form.html'
    success_url = reverse_lazy('disciplina_list')

class DisciplinaDeleteView(DeleteView):
    model = Disciplina
    template_name = 'disciplina_confirm_delete.html'
    success_url = reverse_lazy('disciplina_list')

# Views para Matricula
class MatriculaListView(ListView):
    model = Matricula
    template_name = 'matricula_list.html'
    context_object_name = 'matriculas'

class MatriculaCreateView(CreateView):
    model = Matricula
    form_class = MatriculaForm
    template_name = 'matricula_form.html'
    success_url = reverse_lazy('matricula_list')

class MatriculaUpdateView(UpdateView):
    model = Matricula
    form_class = MatriculaForm
    template_name = 'matricula_form.html'
    success_url = reverse_lazy('matricula_list')

class MatriculaDeleteView(DeleteView):
    model = Matricula
    template_name = 'matricula_confirm_delete.html'
    success_url = reverse_lazy('matricula_list')
