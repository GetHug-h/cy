from rest_framework import serializers
from .models import Tarefa, Input

class TarefaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarefa
        fields = '__all__'

 
class InputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Input
        fields = '__all__'