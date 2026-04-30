def rolar_dados (n):
    import random
    i = 0
    lista = []
    while i < n:
        num = random.randint(1,6)
        lista.append(num)
        i += 1
    return lista

def guardar_dado (dados_rolados, dados_noestoque, dados_paraguardar):
    dado = dados_rolados[dados_paraguardar]
    dados_noestoque.append(dado)
    dados_rolados = dados_rolados[:dados_paraguardar] + dados_rolados [dados_paraguardar+1:]
    return [dados_rolados, dados_noestoque]

def remover_dado(dados_rolados, dados_no_estoque, dado_para_remover):
    dado = dados_no_estoque[dado_para_remover]
    dados_rolados.append(dado)
    dados_no_estoque = dados_no_estoque[:dado_para_remover] + dados_no_estoque[dado_para_remover + 1:]
    return [dados_rolados, dados_no_estoque]

def calcula_pontos_regra_simples (faces):
    pontos = {}
    for categoria in range(1,7):
        soma = 0
        for dado in faces:
            if dado == categoria:
                soma = soma + dado
        pontos [categoria] = soma
    return pontos

def calcula_pontos_soma (lista):
    sum = 0
    for dado in lista:
        sum += dado
    return sum

def calcula_pontos_sequencia_baixa(dados):
    if 1 in dados and 2 in dados and 3 in dados and 4 in dados:
        return 15
    if 2 in dados and 3 in dados and 4 in dados and 5 in dados:
        return 15
    if 3 in dados and 4 in dados and 5 in dados and 6 in dados:
        return 15
    return 0

def calcula_pontos_sequencia_alta (dados):
    if 1 in dados and 2 in dados and 3 in dados and 4 in dados and 5 in dados:
        return 30
    if 2 in dados and 3 in dados and 4 in dados and 5 in dados and 6 in dados:
        return 30
    return 0

       
def calcula_pontos_full_house(dados):
    contagem = {}
    for d in dados:
        if d in contagem:
            contagem[d] += 1
        else:
            contagem[d] = 1
    
    if len(contagem) == 2:
        tem_tres = False
        tem_dois = False
        for valor in contagem:
            if contagem[valor] == 3:
                tem_tres = True
            elif contagem[valor] == 2:
                tem_dois = True
        
        if tem_tres and tem_dois:
            total = 0
            for d in dados:
                total += d
            return total
    
    return 0

def calcula_pontos_quadra(dados):
    contagem = {}
    for d in dados:
        if d in contagem:
            contagem[d] += 1
        else:
            contagem[d] = 1
    
    tem_quadra = False
    for valor in contagem:
        if contagem[valor] >= 4:
            tem_quadra = True
    
    if tem_quadra:
        total = 0
        for d in dados:
            total += d
        return total
    
    return 0


def calcula_pontos_quina(dados):
    contagem = {}
    for d in dados:
        if d in contagem:
            contagem[d] += 1
        else:
            contagem[d] = 1
    
    for valor in contagem:
        if contagem[valor] >= 5:
            return 50
    
    return 0