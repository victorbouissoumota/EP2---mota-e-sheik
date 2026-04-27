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
       

