a = int(input("Digite o primeiro lado do triângulo: "))
b = int(input("Digite o segundo lado do triângulo: "))
c = int(input("Digite o terceiro lado do triângulo: "))



if(a > 0 and b > 0 and c > 0):
    if(a < b + c and b < a + c and c < a + b):
        if(a == b and b == c):
            print("Triângulo Equilátero")
        elif(a == b or a == c or b == c):
            print("Triângulo Isósceles")
        else:
            print("Triângulo Escaleno")
    else:
        print("Não é um triângulo")
else:
        print("Não é um triângulo")



