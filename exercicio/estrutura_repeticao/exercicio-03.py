print("Digite s para sair")
total = 0
dinheiro = 0

while True:
    idade = input("Qual sua idade?")
    if idade == 's':

        break

    idade = int(idade)
    total +=1
    if idade < 3:
        ingreso = 0
    else:
        if idade > 12:
            ingreso = 30
        else:
            ingreso = 15

    dinheiro += ingreso

media = dinheiro / total
print('Total de pessoas {}' .format(total))
print('Total arrecadado {}' .format(dinheiro))
print('Média arrecadada {}' .format(media))