kmRodados = int(input('Digite a quantidade de km rodados'))
diasAluguelCarro = int(input("Digite a quantidade de dias que o carro foi alugado"))

valorPagar = diasAluguelCarro * 60 + kmRodados * 0.15

print("você ficou {} dias com o carro, rodou {} km.".format(diasAluguelCarro,kmRodados))
print("o valor a pagar é de R${}".format(valorPagar))
