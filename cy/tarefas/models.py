from django.db import models

class Tarefa(models.Model):
    descricao = models.CharField(max_length=200)
    data_hora = models.DateTimeField()
    categoria = models.CharField(max_length=10)

    class Meta:
        verbose_name = u'Tarefa'
        verbose_name_plural = u'Tarefas'
        
    def __str__(self):
        return self.descricao
    
class Input(models.Model):
    entrada = models.CharField(max_length=250)
    class Meta:
        verbose_name = u'Input'
        verbose_name_plural = u'Inputs'
        
    def __str__(self):
        return self.entrada
