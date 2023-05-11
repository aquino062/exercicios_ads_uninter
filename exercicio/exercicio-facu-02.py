print('Bem vindo a Lanchonete do willian aquino')
print('------------- cardápio -----------------')

# Exibindo o cardápio com os códigos, descrições dos produtos e seus valores
print('|Código | Descrição do Produto     | Valor(R$) |')
print('|100    | Cachorro-Quente          |   9,00    |')
print('|101    | Cachorro-Quente Duplo    |   11,00   |')
print('|102    | X-Egg                    |   12,00   |')
print('|103    | X-Salada                 |   13,00   |')
print('|104    | X-Bacon                  |   14,00   |')
print('|105    | X-Tudo                   |   17,00   |')
print('|200    | Refrigerante Lata        |   5,00    |')
print('|201    | Chá Gelado               |   4,50    |')

print('----------------------------------------')

totalConta = 0

# Loop para receber os pedidos dos clientes até que eles decidam encerrar
while True:
    # Solicita ao usuário que digite o código do produto que deseja comprar
    codigo = int(input('Digite o código do produto que deseja comprar:'))

    # Verifica o código do produto selecionado e atualiza o total da conta
    if codigo == 100:
        print('você pediu um Cachorro-Quente no valor de R$9,00')
        totalConta += 9

    elif codigo == 101:
        print('você pediu um Cachorro-Quente Duplo no valor de R$11,00')
        totalConta += 11

    elif codigo == 102:
        print('você pediu um X-Egg no valor de R$12,00')
        totalConta += 12

    elif codigo == 103:
        print('você pediu um X-Salada no valor de R$13,00')
        totalConta += 13

    elif codigo == 104:
        print('você pediu um X-Bacon no valor de R$14,00')
        totalConta += 14

    elif codigo == 105:
        print('você pediu um X-Tudo no valor de R$17,00')
        totalConta += 17

    elif codigo == 200:
        print('você pediu um Refrigerante Lata no valor de R$5,00')
        totalConta += 5

    elif codigo == 201:
        print('você pediu um Chá Gelado no valor de R$4,50')
        totalConta += 4.5

    else:
        print('Opção inválida')
        continue

    # Pergunta ao usuário se deseja pedir mais alguma coisa ou encerrar o pedido
    opcao = int(input('Deseja pedir mais alguma coisa? 1 - Sim 2 - Não'))

    if opcao == 2:
        # Exibe o valor total da conta formatado com duas casas decimais
        print('Valor total da conta: R${:.2f}'.format(totalConta))
        break

print('Obrigado pela preferência, volte sempre!')
