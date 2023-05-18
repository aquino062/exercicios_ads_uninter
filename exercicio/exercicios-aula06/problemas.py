notas = [9,7,7,10,3,9,6,6,2]


print(notas.count(7))

notas[-1] = 4
maiorNumero = max(notas)
notas.sort() #ordena em ordem crescente
media = sum(notas) / len(notas) # soma e divide pelo tamanho da lista

print(notas)
print(maiorNumero)
print(media)
print("a media é de {:.2f}".format(media))