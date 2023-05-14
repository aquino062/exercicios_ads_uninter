
valorProduto = int(input("digite o preço do produto"))
p= int(input('Digite o percentual de desconto % '))


valorDesconto = valorProduto * p / 100
valorFinal = valorProduto - valorDesconto


print('o valor do desconto foi de {}  desconto de {} %' .format(valorDesconto,p))
print('o valor final do produto foi de R$ {}'.format(valorFinal))





