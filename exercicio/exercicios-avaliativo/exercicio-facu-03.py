print("Bem vindo a companhia de Logistica Willian aquino")


def dimensoesObejeto():
    while True:
        try:
            comprimento = int(input('Digite o comprimento do obejto (em cm)'))
            largura = int(input('Digite a largura do obejto (em cm)'))
            altura = int(input('Digite a altura do obejto (em cm)'))
            volume = (altura * largura * comprimento)
            break
        except ValueError:
            print("Você digitou alguma dimensão não numérico")
        except:
            print("algo deu errado")
    if (volume < 1000):
        return 10
    elif (volume >= 1000 and volume < 10000):
        return 20
    elif (volume >= 10000 and volume < 30000):
        return 30
    elif (volume >= 30000 and volume < 100000):
        return 50
    elif (volume >= 100000):
        print("Não é aceito objetos tão grande")

    print("o volume do objeto é {}".format(volume))


def pesoObjeto():
    try:
        peso = float(input("Digite o peso do objeto (em kg)"))

    except ValueError:
        print("Entrada inválida. Por favor, digite um valor numérico")

        return

    if (peso <= 0.1):
        return 1
    elif (peso >= 0.1 and peso < 1):
        return 1.5
    elif (peso >= 1 and peso < 10):
        return 2
    elif (peso >= 10 and peso < 30):
        return 3
    elif (peso) >= 30:
        return print("não é aceito , peso acima do limite maximo")


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


print(dimensoesObejeto())
