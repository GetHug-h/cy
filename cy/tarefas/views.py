from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import parser_classes
from .models import Tarefa, Input
from .serializers import TarefaSerializer, InputSerializer
from . import Test
import json
from rest_framework.renderers import JSONRenderer


@api_view(['GET'])
def tarefa_list(request, format=None):
    """
    List all task and create a new task
    """
    if request.method == 'GET':
        tarefas = Tarefa.objects.all()
        serializer = TarefaSerializer(tarefas, many=True)
        return Response(serializer.data)

def tarefa_post(request):
    """
    Create a new task.
    """
    tarefa = Test.processTask(request.data["entrada"])
    serializer = TarefaSerializer(data=tarefa)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def tarefa_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        tarefa = Tarefa.objects.get(pk=pk)
    except Tarefa.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TarefaSerializer(tarefa)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TarefaSerializer(tarefa, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        tarefa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET', 'POST'])
def input_list(request):
    """
    List all code snippets, or create a new input.
    """
    if request.method == 'GET':
        inputs = Input.objects.all()
        serializer = InputSerializer(inputs, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = InputSerializer(data=request.data)
        if serializer.is_valid():
            tarefa_post(request)
            # process_tarefa(request.data)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def input_detail(request, pk, format=None):
    """
    Retrieve, update or delete an input.
    """
    try:
        _input = Input.objects.get(pk=pk)
    except Input.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = InputSerializer(_input)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = InputSerializer(_input, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        _input.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
