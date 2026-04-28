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



       

