def rolar_dados (n):
    import random
    i = 0
    lista = []
    while i < n:
        num = random.randint(1,6)
        lista.append(num)
        i += 1
    return lista
