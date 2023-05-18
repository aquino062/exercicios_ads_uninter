# Dicionário que armazena as peças
pecas = {}

# Variável para controlar o contador de peças
contador = 1


# Função para cadastrar uma peça
def cadastrarPeca(contador):
    global pecas
    # Gera um código para a peça com base no contador
    codigo = str(contador)
    print('Código da peça:', codigo)

    # Solicita os dados da peça ao usuário
    nome = input('Qual o nome da peça:')
    fabricante = input('Qual o fabricante:')
    valor = input('Qual o valor (R$):')

    # Armazena a peça no dicionário de peças
    pecas[codigo] = {'nome': nome, 'fabricante': fabricante, 'valor': valor}
    print('Peça cadastrada com sucesso!')

    # Incrementa o contador de peças
    return contador + 1


# Função para consultar as peças
def consultarPeca():
    print('Consultar Peça')
    print('Escolha a opção desejada:')
    print('1 - Consultar todas as peças ')
    print('2 - Consultar por codigo')
    print('3 - Consultar por fabricante')
    print('4 - retornar ')

    opcao = (input())
    # Consulta todas as peças e exibe os dados
    if opcao == '1':
        for codigo, peca in pecas.items():
            print('Código: ', codigo)
            print('Nome:', peca['nome'])
            print('Fabricante:', peca['fabricante'])
            print('Valor:', peca['valor'])
            print('---------------------------------')



    elif opcao == '2':
        codigo = input('Digite o código da peça:')
        # Solicita o código da peça e verifica se existe no dicionário
        if codigo in pecas:
            # Exibe os dados da peça
            peca = pecas[codigo]
            print('Código: ', codigo)
            print('Nome', peca['nome'])
            print('Fabricante:', peca['fabricante'])
            print('Valor:', peca['valor'])
            print('---------------------------------')
        else:
            print('Peça não encontrada')



    elif opcao == '3':
        # Solicita o fabricante da peça e busca as peças correspondentes
        fabricante = input('Digite o fabricante da peça: ')
        for codigo, peca in pecas.items():
            if peca['fabricante'].lower() == fabricante.lower():
                # Exibe os dados das peças encontradas
                print('Código: ', codigo)
                print('Nome', peca['nome'])
                print('Fabricante:', peca['fabricante'])
                print('Valor:', peca['valor'])
                print('---------------------------------')

    elif opcao == 4:
        return
    else:
        print('opção inválida!')


# Função para remover uma peça
def removerPeca():
    codigo = input('Digite o código da peça que deseja remover: ')
    if codigo in pecas:
        # Remove a peça do dicionário de peças
        del pecas[codigo]
        print('Peça removida com sucesso!')
    else:
        print('Peça não encontrada')


# Programa principal
print('Bem vindo ao controle de Estoque da Biciletaria do Willian Aquino')
while True:
    print('Escolha a opção desejada:')
    print('1 - Cadastrar peça')
    print('2 - Consultar peça')
    print('3 - Remover Peças')
    print('4 - Sair')

    menu = (input())

    if menu == '1':
        print('Cadastrar Peça')
        contador = cadastrarPeca(contador)  # Chama a função para cadastrar uma peça e atualiza o contador

    elif menu == '2':
        consultarPeca()  # Chama a função para consultar as peças


    elif menu == '3':
        print('Remover Peça')
        removerPeca()  # Chama a função para remover uma peça

    elif menu == '4':
        print('finalizando o programa')
        break  # Encerra o loop e finaliza o programa

    else:
        print('opção inválida!')
