import TarefaV2

data = 'Fazer compras as 17 horas e 20 minutos da tarde do dia 24 de dezembro'
#data = 'Dançar as 20 horas do dia 10 de outubro'
#data = 'tomar remédio às 3 horas da tarde do dia 18 de agosto'
#data = 'tomar remédio às 10 horas da noite do dia 18 de agosto'
def processTask(data):
    print(data)
    tfa = TarefaV2.Tarefa(data)
    print(tfa.data_hora)
    print(tfa.descricao)
    print(tfa.categoria)
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

processTask(data)