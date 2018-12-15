import datetime
import re

class Tarefa:
    '''
    Classe que recebe como parâmetro uma string com as informações sobre a tarefa do usuário
    e realiza o seu processamento, guardando as informações identificadas em atributos da classe
    '''

    # Arrays para auxiliar a extração de informações

    saude = ['tomar', 'remedio', 'medicina', 'medico', 'atender', 'socorrer', 'medicar',
             'medicamento', 'dor', 'enxaqueca', 'medicar', 'curar', 'sarar', 'dor de cabeca', 
             'febre', 'nauseas', 'vomitos', 'dores', 'analgesico', 'injecao', 'hospital', 'medico',
             'doutor', 'farmacia', 'drogaria', 'injetar']
    trabalho = ['trabalhar', 'relatorio', 'criar', 'reuniao', 'chefe', 'empregado', 'empregada', 'emprego',
                'gerenciar', 'liderar']
    lazer = ['diversao', 'parque', 'corrida', 'jogo', 'videogame', 'tv', 'xbox', 'ps4', 'computador', 'notebook',
            'festa', 'shopping', 'praia', 'viagem', 'viajar', 'nadar', 'jogar', 'brincar', 'compras']
    financas = ['economizar', 'criar poupanca', 'poupar', 'reduzir custos', 'investir', 'planejar']
    estudos = ['aprender', 'obter conhecimento', 'saber sobre', 'saber como', 'curso', 'estudar', 'estudo',
                'prova', 'semestre', 'professor', 'graduar', 'graduacao','turma', 'classe,'
                'semestre', 'bimestre', 'modulo', 'graduacao', 'bacharelado', 'licenciatura', 'mestrado', 
                'doutorado', 'formatura', 'exercicios', 'faculdade', 'escola', 'universidade', 'cursar']
    meses = ['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro',
              'novembro', 'dezembro']
    periodos = ['meio dia', 'meia noite', 'tarde', 'noite']
    futuro = ['amanha', 'semana que vem', 'ano que vem', 'proximo ano', 'proxima semana', 'mes que vem', 'proximo mes', 
            'mes que vira', 'depois de amanha']
    horarios = [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 0]
    
    # Criar variaveis que vão no objeto tarefa (box com as informações da tarefa)
    def __init__(self, entrada):
        tarefa = self.processar(entrada)
        if tarefa != None:
            self.descricao = tarefa[0]
            self.data_hora = tarefa[1]
            self.dia = tarefa[1].day
            self.mes = tarefa[1].month
            self.hora = tarefa[1].hour
            self.categoria = tarefa[2]
            print('Tarefa criada com sucesso!')
        else:
            print('Dados invalidos. Nao foi possivel criar a tarefa.')

    # Processar string (frase de exemplo: tomar remedio as 6 horas da tarde do dia 10 de setembro)

    def processar(self, entrada):
        palavras = entrada.split(' ')  # criar array com as palavras separadas por espaço
        numeros = []
        indiceHora = 0
        indiceDia = 0
        countAux = 0
        count = 0

        i = 0
        for p in palavras:
            palavras[i] = p.lower()
            i = i + 1

        for word in palavras:
            if re.findall(r'-?\d+\.?\d*', word): # reconhecer somente numeros no contains. && pegar o primeiro num da frase
                if (palavras[count - 1] == 'as' and countAux == 0) or countAux > 0:
                    countAux = countAux + 1
                if countAux == 1:
                    indiceHora = count
                if countAux == 2:
                    if palavras[count -1] != 'dia':
                        indiceMinuto = count
                    else:
                        indiceMinuto = 0
                        indiceDia = count
                        break
                if countAux == 3 and palavras[count - 1] == 'dia':
                    indiceDia = count
            count = count + 1

        if countAux == 0: # entrada invalida (nao possui numeros)
            ind = self.procuraPeriodos(palavras)
            if ind is None:
                print('Entrada inválida!')
                return None
            else
                palavras = entrada.split(' ')
                self.processar(palavras, ind)

        if countAux == 1: # se count for == 1 significa que só tem um numero no o que indica provavelmente que
            datap = datetime.datetime.now()                    # o usuario só falou a hora logo atribuir data atual

        if count >= 1: # Encontrando a descricao de uma entrada valida
            descricaop = self.pdescricao(indiceHora, palavras, 0)
            
        if countAux > 1:
            datap = self.pdata(indiceHora, indiceMinuto, indiceDia, countAux, palavras)
            

        categoria = self.idfcategoria(palavras)
        atributos = [descricaop, datap, categoria]
        return atributos

    def processar(self, palavras, indFuturo)
        descricaop = self.pdescricao(indFuturo, palavras, 1)
        categoria = self.idfcategoria(palavras)
        datap = self.encontrarDataFutura(indFuturo)

    # Processamento de data de tarefa de entrada sem numero
    def encontraDataFutura(self, indFuturo)

        data = datetime.datetime.today()

        if indFuturo == 0:
            datap = datetime.datetime(today.year)
            datap.day = datap.day + 1
        if indFuturo == 1:
            datap.day = datap.day + 7
        if indFuturo == 2
            datap.year = datap.year + 1
            datap.day = None

        if indFuturo == 2
            datap.year = datap.year + 1
        if indFuturo == 2
            datap.year = datap.year + 1
        if indFuturo == 2
            datap.year = datap.year + 1
        if indFuturo == 2
            datap.year = datap.year + 1
        if indFuturo == 2
            datap.year = datap.year + 1
        if indFuturo == 2
            datap.year = datap.year + 1
    

    def pdata(self, indiceHora, indiceMinuto, indiceDia, countAux, words):
        # Parte de processamento da data

        minuto = 0

        count = 0
        # Se countAux == 2 há hora e dia ou hora e minuto
        if countAux == 2 and indiceMinuto == 0:
            print(0)
            for word in words:
                if count == indiceHora:
                    hora = int(word)
                if count == indiceDia:
                    dia = int(word)
                    mes = words[count + 2].lower()
                count = count + 1
        
        count = 0
        if countAux == 2 and indiceMinuto != 0:
            print(1)
            for word in words:
                if count == indiceHora:
                    hora = int(word)
                if count == indiceMinuto:
                    minuto = int(word)
                    mes = words[count + 3].lower()
                count = count + 1

        count = 0
        if countAux == 3:
            print(2)
            for word in words:
                if count == indiceHora:
                    hora = int(word)
                if count == indiceMinuto:
                    minuto = int(word)
                if count == indiceDia:
                    dia = int(word)
                    mes = words[count + 2].lower()
                count = count + 1

        # Parte de converter mes em numero ao inves de escrito por extenso

        count = 0
        for m in self.meses:
            if m == mes:
                mes = int('0' + str(count+1))
            count = count + 1
        today = datetime.datetime.today()
        data = datetime.datetime(today.year, mes, dia, hora, minuto, 0)

        return data

    # Entrada com números
    def pdescricao(self, indice, words, tipo):
        # Parte de processamento da descrição
        # 0 - Entrada com números
        # 1 - Entrada sem números (inclusive por extenso)
        # indice - Índice da palavra em que a concatenação
        # deve parar
         
        descricao = ''
        count = 0

        if tipo == 0:
            for word in words:
                if count < indice - 1:
                    descricao = descricao + word + ' '
                count = count + 1
        if tipo == 1:
            for word in words:
                if count < indice:
                    descricao = descricao + word + ' '
                count = count + 1
        return descricao

    def procuraFuturo(self, palavras):
        i = 0
        for f in futuro:
            for p in palavras
                if f = p:
                    return i
            i = i + 1
        return None

    def idfcategoria(self, palavras):
        for s in self.saude:
             for p in palavras:
                 if s == p:
                     return 'Saúde'

        for t in self.trabalho:
             for p in palavras:
                 if t == p:
                     return 'Trabalho'

        for l in self.lazer:
             for p in palavras:
                 if l == p:
                     return 'Lazer'

        for f in self.financas:
             for p in palavras:
                 if f == p:
                     return 'Finanças'

        for e in self.estudos:
             for p in palavras:
                 if e == p:
                     return 'Estudos'

        return 'Outros'
