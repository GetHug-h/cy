import datetime
import re
import unidecode

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
            'festa', 'shopping', 'praia', 'viagem', 'viajar', 'nadar', 'jogar', 'brincar', 'compras', 'beber',
            'comer', 'dancar', 'esquiar']
    financas = ['economizar', 'criar poupanca', 'poupar', 'reduzir custos', 'investir', 'planejar']
    estudos = ['aprender', 'obter conhecimento', 'saber sobre', 'saber como', 'curso', 'estudar', 'estudo',
                'prova', 'semestre', 'nota da prova', 'professor', 'graduar', 'graduacao','turma', 'classe,'
                'semestre', 'bimestre', 'modulo', 'pos graduacao', 'bacharelado', 'licenciatura', 'mestrado',
                'doutorado', 'formatura', 'lista de exercicios', 'faculdade', 'escola', 'universidade', 'cursar',
                'projeto da faculdade']
    meses = ['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro',
              'novembro', 'dezembro']
    periodos = ['meio', 'dia', 'meia', 'noite', 'tarde', 'noite']
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
        entradaAux = unidecode._unidecode(entrada)
        palavras = entradaAux.split(' ')  # criar array com as palavras separadas por espaço
        numeros = []
        indiceHora = 0
        indiceDia = 0
        countAux = 0
        count = 0

        i = 0
        for p in palavras:
            palavras[i] = p.lower()
            i = i + 1

        flag = 0

        if entrada.find(self.periodos[0]) != -1 and entrada.find(self.periodos[1]) != -1:
            hora = 12
            flag = 1
        if entrada.find(self.periodos[2]) != -1 and entrada.find(self.periodos[3]) != -1:
            hora = 0
            flag = 1
        if entrada.find(self.periodos[4]) != -1:
            for word in palavras:
                if re.findall(r'-?\d+\.?\d*', word): # reconhecer somente numeros no contains. && pegar o primeiro num da frase
                    if (palavras[count - 1] == 'as' and countAux == 0) or countAux > 0:
                        countAux = countAux + 1
                    if countAux == 1:
                        indiceHora = count
                count = count + 1
            if int(palavras[indiceHora]) > 0 and int(palavras[indiceHora]) < 7:
                hora = int(palavras[indiceHora])
                hora = hora + 12
            flag = 1
        if entrada.find(self.periodos[5]) != -1:
            for word in palavras:
                if re.findall(r'-?\d+\.?\d*', word): # reconhecer somente numeros no contains. && pegar o primeiro num da frase
                    if (palavras[count - 1] == 'as' and countAux == 0) or countAux > 0:
                        countAux = countAux + 1
                    if countAux == 1:
                        indiceHora = count
                count = count + 1
            if int(palavras[indiceHora]) > 6 and int(palavras[indiceHora]) < 12:
                hora = int(palavras[indiceHora])
                hora = hora + 12
            flag = 1

        if flag == 0:
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
        elif flag == 1:
            count = 0
            indiceHora = -1
            indiceMinuto = -1
            for word in palavras:
                if re.findall(r'-?\d+\.?\d*', word): # reconhecer somente numeros no contains. && pegar o primeiro num da frase
                        if (palavras[count -1] == 'dia' and (palavras[count-2] == 'do' or palavras[count-2] == 'no')):
                            indiceDia = count
                            countAux = countAux + 1
                            break
                count = count + 1
        if countAux == 0: # entrada invalida (nao possui numeros)
            print('Entrada inválida!')
            return None

        if countAux == 1 and flag == 0: # se count for == 1 significa que só tem um numero no o que indica provavelmente que
            datap = datetime.datetime.today()                    # o usuario só falou a hora logo atribuir data atual
            datap = datetime.datetime(datap.year, datap.month, datap.day, int(palavras[indiceHora]), 0, 0)
        if count >= 1: # Encontrando a descricao de uma entrada valida
            descricaop = self.pdescricao(indiceHora, palavras, entrada, flag)

        if countAux > 1 or flag == 1:
            hora = 0
            datap = self.pdata(indiceHora, indiceMinuto, indiceDia, countAux, palavras, flag, hora)


        categoria = self.idfcategoria(palavras)
        atributos = [descricaop, datap, categoria]
        return atributos

    def pdata(self, indiceHora, indiceMinuto, indiceDia, countAux, words, flag, hora):
        # Parte de processamento da data

        minuto = 0
        count = 0

        if flag == 0:
            # Se countAux == 2 há hora e dia ou hora e minuto
            if countAux == 2 and indiceMinuto == 0:
                for word in words:
                    if count == indiceHora:
                        hora = int(word)
                    if count == indiceDia:
                        dia = int(word)
                        mes = words[count + 2]
                    count = count + 1

            count = 0
            if countAux == 2 and indiceMinuto != 0:
                for word in words:
                    if count == indiceHora:
                        hora = int(word)
                    if count == indiceMinuto:
                        minuto = int(word)
                        mes = words[count + 3]
                    count = count + 1

            count = 0
            if countAux == 3:
                for word in words:
                    if count == indiceHora:
                        hora = int(word)
                    if count == indiceMinuto:
                        minuto = int(word)
                    if count == indiceDia:
                        dia = int(word)
                        mes = words[count + 2]
                    count = count + 1

        if flag == 1:
            minuto = 0
            dia = int(words[indiceDia])
            mes = words[len(words) - 1]
        # Parte de converter mes em numero ao inves de escrito por extenso

        count = 0
        for m in self.meses:
            if m == mes:
                mes = int('0' + str(count+1))
            count = count + 1



        today = datetime.datetime.today()
        data = datetime.datetime(today.year, mes, dia, hora, minuto, 0)

        return data

    def pdescricao(self, indiceHora, words, entrada, flag):
        # Parte de processamento da descrição

        descricao = ''
        count = 0
        if flag == 0:
            for word in words:
                if count < indiceHora - 1:
                    if count == 0:
                        descricao = descricao + word.capitalize() + ' '
                    if count != 0:
                        descricao = descricao + word + ' '
                count = count + 1
            return descricao

        if flag == 1:
            aux = 0
            if entrada.find(self.periodos[0]) != -1 and entrada.find(self.periodos[1]) != -1:
                indice = entrada.find(self.periodos[0])
                for word in words:
                    if count < indice - 1:
                        if count == 0:
                            descricao = descricao + word.capitalize() + ' '
                        if count != 0:
                            descricao = descricao + word + ' '
                    count = count + 1
                return descricao

            if entrada.find(self.periodos[2]) != -1 and entrada.find(self.periodos[3]) != -1:
                indice = entrada.find(self.periodos[2])
                for word in words:
                    if count < indice - 1:
                        if count == 0:
                            descricao = descricao + word.capitalize() + ' '
                        if count != 0:
                            descricao = descricao + word + ' '
                    count = count + 1
                return descricao

            if entrada.find(self.periodos[4]) != -1:
                indice = entrada.find(self.periodos[4])
                for word in words:
                    if count < indice - 1:
                        if count == 0:
                            descricao = descricao + word.capitalize() + ' '
                        if count != 0:
                            descricao = descricao + word + ' '
                    count = count + 1
                return descricao

            if entrada.find(self.periodos[5]) != -1:
                indice = entrada.find(self.periodos[5])
                for word in words:
                    if count < indice - 1:
                        if count == 0:
                            descricao = descricao + word.capitalize() + ' '
                        if count != 0:
                            descricao = descricao + word + ' '
                    count = count + 1
                return descricao


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
