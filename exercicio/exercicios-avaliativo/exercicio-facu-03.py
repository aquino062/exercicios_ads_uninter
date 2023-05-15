print("Bem vindo a companhia de Logistica Willian aquino")


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


def pesoObjeto():
    while True:
        try:
            peso = float(input("Digite o peso do objeto (em kg)"))

        except ValueError:
            print("Entrada inválida. Por favor, digite um valor numérico")
            continue

            return

        if (peso <= 0.1):
            return 1
        elif (peso >= 0.1 and peso < 1):
            return 1.5
        elif (peso >= 1 and peso < 10):
            return 2
        elif (peso >= 10 and peso < 30):
            return 3
        else:
            print("não é aceito , peso acima do limite maximo")


def rotaObjeto():
    print("Qual a rota:")

    print("RS - De Rio de Janeiro até São Paulo")
    print("SR - De São Paulo até Rio de Janeiro")
    print("BS - De Brasília até São Paulo")
    print("SB - De São Paulo até Brasília")
    print("BR - De Brasília até Rio de Janeiro")
    print("RB - Rio de Janeiro até Brasília")

    while True:
        rota = input("Digite a rota: ").upper()

        if rota == "RS" or rota == "SR":
            return 1
        elif rota == "BS" or rota == "SB":
            return 1.2
        elif rota == "BR" or rota == "RB":
            return 1.5
        else:
            print("Você digitou uma rota inválida.")
            print("Por favor, digite a rota desejada novamente.")


dimensao = dimensoesObejeto()
peso = pesoObjeto()
rota = rotaObjeto()

total = dimensao * peso * rota

print("Total a pagar é R$ {:.2f} (dimensões:{} * peso:{} * rota:{})".format(total, dimensao, peso, rota))
