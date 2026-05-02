from funcoes import *

cartela = {
    'regra_simples': {1: -1, 2: -1, 3: -1, 4: -1, 5: -1, 6: -1},
    'regra_avancada': {
        'sem_combinacao': -1,
        'quadra': -1,
        'full_house': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'cinco_iguais': -1
    }
}

categorias_simples = ['1', '2', '3', '4', '5', '6']
categorias_avancadas = ['sem_combinacao', 'quadra', 'full_house', 'sequencia_baixa', 'sequencia_alta', 'cinco_iguais']
todas_categorias = categorias_simples + categorias_avancadas

imprime_cartela(cartela)

rodada = 0
while rodada < 12:
    dados_rolados = rolar_dados(5)
    dados_guardados = []
    rerrolagens = 0

    print(f"Dados rolados: {dados_rolados}")
    print(f"Dados guardados: {dados_guardados}")
    print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")

    jogada_feita = False
    while not jogada_feita:
        escolha = input()

        if escolha == '1':
            print("Digite o índice do dado a ser guardado (0 a 4):")
            indice = int(input())
            resultado = guardar_dado(dados_rolados, dados_guardados, indice)
            dados_rolados = resultado[0]
            dados_guardados = resultado[1]

        elif escolha == '2':
            print("Digite o índice do dado a ser removido (0 a 4):")
            indice = int(input())
            resultado = remover_dado(dados_rolados, dados_guardados, indice)
            dados_rolados = resultado[0]
            dados_guardados = resultado[1]

        elif escolha == '3':
            if rerrolagens >= 2:
                print("Você já usou todas as rerrolagens.")
            else:
                dados_rolados = rolar_dados(len(dados_rolados))
                rerrolagens += 1

        elif escolha == '4':
            imprime_cartela(cartela)

        elif escolha == '0':
            print("Digite a combinação desejada:")
            combinacao = input()

            valida = False
            while not valida:
                if combinacao not in todas_categorias:
                    print("Combinação inválida. Tente novamente.")
                    combinacao = input()
                elif combinacao in categorias_simples and cartela['regra_simples'][int(combinacao)] != -1:
                    print("Essa combinação já foi utilizada.")
                    combinacao = input()
                elif combinacao in categorias_avancadas and cartela['regra_avancada'][combinacao] != -1:
                    print("Essa combinação já foi utilizada.")
                    combinacao = input()
                else:
                    valida = True

            todos_dados = dados_rolados + dados_guardados
            cartela = faz_jogada(todos_dados, combinacao, cartela)
            jogada_feita = True
            rodada += 1
            continue

        else:
            print("Opção inválida. Tente novamente.")
            continue

        print(f"Dados rolados: {dados_rolados}")
        print(f"Dados guardados: {dados_guardados}")
        print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")

imprime_cartela(cartela)

pontuacao = 0
soma_simples = 0
for i in range(1, 7):
    if cartela['regra_simples'][i] != -1:
        pontuacao += cartela['regra_simples'][i]
        soma_simples += cartela['regra_simples'][i]

if soma_simples >= 63:
    pontuacao += 35

for chave in cartela['regra_avancada']:
    if cartela['regra_avancada'][chave] != -1:
        pontuacao += cartela['regra_avancada'][chave]

print(f"Pontuação total: {pontuacao}")