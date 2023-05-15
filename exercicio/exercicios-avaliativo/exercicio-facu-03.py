print("Bem vindo a companhia de Logistica Willian aquino")


def dimensoesObejeto():
    while (True):
        try:
            comprimento = int(input('Digite o comprimento do obejto (em cm)'))
            largura = int(input('Digite a largura do obejto (em cm)'))
            altura = int(input('Digite a altura do obejto (em cm)'))
            volume = (altura * largura * comprimento)

        except:
            print("algo deu errado")

        else:
            if (volume < 1000):
                return 10
            elif (volume >= 1000 and volume < 10000):
                return 20
            elif (volume >= 10000 and volume < 30000):
                return 30
            elif (volume >= 30000 and volume < 10000):
                return 50
            elif (volume >= 100000):
               print("Não é aceito objetos tão grande")

        finally:
            print("o volume do objeto é {} ".format(volume))


print(dimensoesObejeto())
