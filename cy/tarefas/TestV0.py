from . import TarefaV2

def processTask(data):
    print(data)
    tfa = TarefaV2.Tarefa(data)
    print(tfa.data_hora.hour)
    data = {
        "descricao": tfa.descricao,
        "data_hora": tfa.data_hora,
        "categoria": tfa.categoria
    }

    # {
    #     "entrada": "Fazer compras as 17 horas da tarde do dia 24 de dezembro"
    # }
    #
    # {
    #     "entrada": "Tomar remedio as 13 horas do dia 11 de janeiro"
    # }

    return data

