from django.db import models

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    data_criacao = models.DateField()

    def __str__(self):
        return self.nome

class Municipio(models.Model):
    nome = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.nome}/{self.estado}"

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    data_nascimento = models.DateField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
