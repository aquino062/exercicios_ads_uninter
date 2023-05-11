# Imprime uma mensagem de boas-vindas ao usuário
print('Bem vindo a Loja do willian aquino')
print('----------------------------------')

# Solicita que o usuário insira o valor do produto como um número
valorProduto = float(input('Digite o valor do produto: '))

# Solicita que o usuário insira a quantidade do produto como um número inteiro
qntdProduto = int(input('Digite a quantidade do produto: '))

# Usa uma estrutura condicional para determinar qual é o desconto apropriado com base na quantidade comprada
if (qntdProduto <= 9):
    desconto = 0.0
elif (qntdProduto >= 10 and qntdProduto <= 99):
    desconto = 0.05
elif (qntdProduto >= 100 and qntdProduto <= 999):
    desconto = 0.10
else:
    desconto = 0.15

# Calcula o valor total multiplicando o valor do produto pela quantidade comprada
valorTotal = valorProduto * qntdProduto

# Calcula o valor de desconto multiplicando o valor total pelo valor de desconto apropriado
valorDesconto = valorTotal * desconto

# Calcula o valor final subtraindo o valor de desconto do valor total
valorFinal = valorTotal - valorDesconto


# Imprime o valor total, o valor de desconto e o valor final
print('Valor total: R$ {:.2f}'.format(valorTotal))
print('Valor desconto: R$ {:.2f} desconto de {} %'.format(valorDesconto, desconto * 100))
print('Valor final: R$ {:.2f}'.format(valorFinal))

