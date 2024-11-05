from django import forms
from .models import Disciplina, Matricula, Aluno

class DisciplinaForm(forms.ModelForm):
    class Meta:
        model = Disciplina
        fields = ['nome', 'carga_horaria']

class MatriculaForm(forms.ModelForm):
    class Meta:
        model = Matricula
        fields = ['aluno', 'disciplina', 'data_matricula', 'observacao']  # Adicione observação, se necessário

    observacao = forms.CharField(widget=forms.Textarea, required=False)  # Campo opcional

    def clean(self):
        cleaned_data = super().clean()
        aluno = cleaned_data.get('aluno')
        disciplina = cleaned_data.get('disciplina')

        if Matricula.objects.filter(aluno=aluno, disciplina=disciplina).exists():
            raise forms.ValidationError('Este aluno já está matriculado nesta disciplina.')

        return cleaned_data
