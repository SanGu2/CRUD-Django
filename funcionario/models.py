from django.db import models

# Create your models here.
from mongoengine import Document, StringField, FloatField, DateField

class Funcionario(Document):
    nome = StringField(required=True, max_length=100)
    cargo = StringField(required=True, max_length=50)
    salario = FloatField(required=True, min_value=0.0)
    data_admissao = DateField(required=True)

    meta = {
        'collection': 'funcionario',
        'ordering': ['-data_admissao']
    }

    def __str__(self):
        return f"{self.nome} - {self.cargo}"