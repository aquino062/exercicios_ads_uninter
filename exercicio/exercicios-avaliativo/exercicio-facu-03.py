print("Bem vindo a companhia de Logistica Willian aquino")


# solicita as dimensões (comprimento, largura e altura) do objeto em centímetros, calcula o volume do objeto e retorna um valor com base no volume.
def dimensoesObejeto():
    while True:
        try:
            comprimento = float(input('Digite o comprimento do obejto (em cm)'))
            largura = float(input('Digite a largura do obejto (em cm)'))
            altura = float(input('Digite a altura do obejto (em cm)'))
            volume = (altura * largura * comprimento)
            print("O volume do objeto é (em cm³) {} ".format(volume))

            if (volume < 1000):
                return 10
            elif (volume >= 1000 and volume < 10000):
                return 20
            elif (volume >= 10000 and volume < 30000):
                return 30
            elif (volume >= 30000 and volume < 100000):
                return 50
            else:
                print("Não é aceito objetos tão grande")
                print("Por favor, entre com as dimensões novamente")




        except ValueError:
            print("Você digitou alguma dimensão não numérica. Por favor, entre com as dimensões novamente.")
            continue


# solicita o peso do objeto em quilogramas e retorna um valor com base no peso.
def pesoObjeto():
    while True:  # cria um loop infinito até que uma condição de interrupção seja encontrada.
        try:  # solicita o peso e converte em um número de ponto flutuante
            peso = float(input("Digite o peso do objeto (em kg)"))

        except ValueError:  # se o usuário digitar um valor não numérico,ele cai nesse bloco
            print("Entrada inválida. Por favor, digite um valor numérico")
            continue  # volta para o inicio do loop

            return
        # verificam o valor do peso e retornam um valor correspondente.
        if (peso <= 0.1):
            return 1
        elif (peso >= 0.1 and peso < 1):
            return 1.5
        elif (peso >= 1 and peso < 10):
            return 2
        elif (peso >= 10 and peso < 30):
            return 3
        else:  # Se nenhuma das condições acima for atendida
            print("não é aceito , peso acima do limite maximo")


# solicita ao usuário que digite a rota desejada e retorna um valor com base na rota escolhida.
def rotaObjeto():
    print("Qual a rota:")

    print("RS - De Rio de Janeiro até São Paulo")
    print("SR - De São Paulo até Rio de Janeiro")
    print("BS - De Brasília até São Paulo")
    print("SB - De São Paulo até Brasília")
    print("BR - De Brasília até Rio de Janeiro")
    print("RB - Rio de Janeiro até Brasília")

    while True:
        # solicita a rota e converte a string para maiúsculo caso seja digitado minúsculo
        rota = input("Digite a rota: ").upper()

        # verifica qual rota foi digitada e retorna um valor correspondente
        if rota == "RS" or rota == "SR":
            return 1
        elif rota == "BS" or rota == "SB":
            return 1.2
        elif rota == "BR" or rota == "RB":
            return 1.5
        else:  # Se nenhuma das condições acima for atendida
            print("Você digitou uma rota inválida.")
            print("Por favor, digite a rota desejada novamente.")


dimensao = dimensoesObejeto()  # Chama a função para obter o valor da dimensão
peso = pesoObjeto()  # Chama a função para obter o valor do peso
rota = rotaObjeto()  # Chama a função para obter o valor da rota

total = dimensao * peso * rota  # Calcula o valor total a pagar multiplicando os valores obtidos

# Imprime o valor total a pagar
print("Total a pagar é R$ {:.2f} (dimensões:{} * peso:{} * rota:{})".format(total, dimensao, peso, rota))
