from random import randint

def validar_jogada(pergunta):
    while True:
        try:
            jogada = int(input(pergunta))
            if jogada in (1, 2, 3):
                return jogada
            elif jogada == 0:
                return 0
            else:
                print("Opção inválida. Escolha 1 para Pedra, 2 para Papel ou 3 para Tesoura.")
        except ValueError:
            print("Entrada inválida. Insira um número inteiro.")


def determinar_vencedor(jogador1, jogador2):
    if jogador1 == jogador2:
        return 0  # Empate
    elif (jogador1 == 1 and jogador2 == 3) or (jogador1 == 2 and jogador2 == 1) or (jogador1 == 3 and jogador2 == 2):
        return 1  # Jogador 1 venceu
    else:
        return 2  # Jogador 2 venceu

def exibir_resultados(resultados):
    print("\n----- RESULTADOS -----")
    print("Número de vitórias do Jogador 1: {}".format(resultados[1]))
    print("Número de vitórias do Jogador 2: {}".format(resultados[2]))
    print("Número de empates: {}".format(resultados[0]))

def jogar_jokenpo():
    print("JOKENPO")
    print("1 - Pedra")
    print("2 - Papel")
    print("3 - Tesoura")

    resultados = [0, 0, 0]  # [Empates, Vitórias do Jogador 1, Vitórias do Jogador 2]

    while True:
        j1 = validar_jogada('Escolha sua jogada (1-3) ou digite 0 para sair: ')
        if j1 == 0:
            break

        j2 = randint(1, 3)
        resultado = determinar_vencedor(j1, j2)

        if resultado == 0:
            print("Empate!")
        elif resultado == 1:
            print("Jogador 1 ganhou!")
            resultados[1] += 1
        else:
            print("Jogador 2 ganhou!")
            resultados[2] += 1

        print("Jogador 1: {}, Jogador 2: {}".format(j1, j2))

    exibir_resultados(resultados)

jogar_jokenpo()