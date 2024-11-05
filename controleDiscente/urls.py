from django.urls import path
from .views import (
    DisciplinaListView, DisciplinaCreateView, DisciplinaUpdateView, DisciplinaDeleteView,
    MatriculaListView, MatriculaCreateView, MatriculaUpdateView, MatriculaDeleteView
)

urlpatterns = [
    path('disciplinas/', DisciplinaListView.as_view(), name='disciplina_list'),
    path('disciplinas/add/', DisciplinaCreateView.as_view(), name='disciplina_create'),
    path('disciplinas/edit/<int:pk>/', DisciplinaUpdateView.as_view(), name='disciplina_update'),
    path('disciplinas/delete/<int:pk>/', DisciplinaDeleteView.as_view(), name='disciplina_delete'),
    
    path('matriculas/', MatriculaListView.as_view(), name='matricula_list'),
    path('matriculas/add/', MatriculaCreateView.as_view(), name='matricula_create'),
    path('matriculas/edit/<int:pk>/', MatriculaUpdateView.as_view(), name='matricula_update'),
    path('matriculas/delete/<int:pk>/', MatriculaDeleteView.as_view(), name='matricula_delete'),
]
