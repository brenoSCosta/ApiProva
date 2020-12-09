from .models import Aluno
from rest_framework import serializers


class AlunoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Aluno
        fields = ('matricula', 'nome', 'nota','nota2', 'media')
