while True:

    c = input("Digite a operação: +, -, *, / ou digite s para sair")

    if c == '+' or c == '-' or c == '*' or c == '/':
        a = int(input("Digite o primeiro valor"))
        b = int(input("Digite o segundo valor"))

    if c == '+':
        resultado = a + b
        print("O resultado é: {}".format(resultado))
        continue
    elif c == '-':
        resultado = a - b
        print("O resultado é: {}".format(resultado))
        continue
    elif c == '*':
        resultado = a * b
        print("O resultado é: {}".format(resultado))
        continue
    elif c == '/':
        resultado = float(a) / b
        print("O resultado é: {}".format(resultado))
        continue
    elif c == 's' or c == 'S':
        break
    else:
        print("Operação inválida")

print("encerrando o programa")
