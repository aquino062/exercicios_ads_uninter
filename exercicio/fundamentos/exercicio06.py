a = int(input("Digite o primeiro valor"))
b = int(input("Digite o segundo valor"))
c = input("Digite a operação: +, -, *, /")


if c == '+':
 resultado = a + b
elif c == '-':
 resultado = a - b
elif c == '*':
 resultado = a * b
elif c == '/':
  resultado = float(a) / b
else:
    print("Operação inválida")

print("O resultado é: {}" .format(resultado))
