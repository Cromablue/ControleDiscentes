from django.db import models
from django.contrib.auth.models import User

class Disciplina(models.Model):
    nome = models.CharField(max_length=200)
    carga_horaria = models.PositiveIntegerField()
    usuarios = models.ManyToManyField(User, through='Matricula')

    def __str__(self):
        return self.nome

class Matricula(models.Model):
    aluno = models.ForeignKey(User, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    total_faltas = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.aluno.username} - {self.disciplina.nome}"
