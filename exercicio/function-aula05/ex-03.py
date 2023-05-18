from datetime import date

# Criar um dicionário para armazenar os dados das pessoas
pessoas = []
total_cadastros = 0
soma_idades = 0
mulheres_menos_30 = []
homens_acima_media = []

while True:
    try:
        # Ler os dados da pessoa
        opcao = input("Deseja cadastrar uma pessoa? (s para sim, n para sair): ")
        if opcao.lower() == "n":
            break

        if opcao.lower() != 's':
            print("Opção inválida. Por favor, digite 's' para cadastrar uma pessoa ou 'n' para sair.")
            continue

        nome = input("Digite o nome da pessoa: ")
        ano_nascimento = int(input("Digite o ano de nascimento da pessoa: "))
        sexo = input("Digite o sexo da pessoa (M para masculino, F para feminino): ")

        # Calcular a idade da pessoa
        ano_atual = date.today().year
        idade = ano_atual - ano_nascimento

        # Armazenar os dados da pessoa no dicionário
        pessoa = {"nome": nome, "ano_nascimento": ano_nascimento, "sexo": sexo, "idade": idade}
        pessoas.append(pessoa)

        # Atualizar as estatísticas
        total_cadastros += 1
        soma_idades += idade

        # Verificar se a pessoa é mulher com menos de 30 anos
        if sexo.upper() == "F" and idade < 30:
            mulheres_menos_30.append(nome)


    except ValueError:
        print("Valor inválido para a idade.")
        continue

# Calcular a média das idades
media_idades = soma_idades / total_cadastros

# Identificar homens com idade acima da média
for pessoa in pessoas:
    if pessoa["sexo"].upper() == "M" and pessoa["idade"] > media_idades:
        homens_acima_media.append(pessoa["nome"])

# Apresentar os resultados
print("Total de cadastros efetuados:", total_cadastros)
print("Média de idades: {:.2f}".format(media_idades))
print("Mulheres com menos de 30 anos:", mulheres_menos_30)
print("Homens com idade acima da média:", homens_acima_media)
