nota1 = float(input("digite a nota1"))
nota2 = float(input("digite a nota2"))
nota3 = float(input("digite a nota3"))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print("aprovado")
elif media >= 5:
    print("recuperação")
else:
    print("reprovado")

print("sua media é: {} ".format(media))
print('sua media é: {:.2f}'.format(media))
