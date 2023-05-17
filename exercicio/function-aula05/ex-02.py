def valid_int(pergunta, min, max):
    x = int(input(pergunta))
    while ((x < min) or (x > max)): x = int(input(pergunta))
    return x

def criaArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'wt+')
        a.close()

    except:
        print('Erro na criação do arquivo')

    else:
        print('Arquivo {} foi criado com sucesso! \n ' .format(nomeArquivo))

def existeArquivo(nomoArquivo):
    try:
        a = open(nomoArquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def cadastrarJogo(nomeArquivo,nomeJogo,nomeVideoGame):
    try:
        a = open(nomeArquivo, 'at')

    except:
        print('Erro ao abrir o arquivo')

    else:
        a.write('{};{} \n'.format(nomeJogo, nomeVideoGame))

    finally:
        a.close()

def listarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
    except:
        print('Erro ao ler o arquivo')

    else:
        print(a.read())

    finally:
        a.close()

# principal
arquivo = 'games.txt'
if existeArquivo(arquivo):
    print('arquivo localizado no pc')

else:
    print('Arquivo não existe')
    criaArquivo(arquivo)


while True:
    print('MENU')
    print('1 - Cadastrar novo item')
    print('2 - listar cadastros')
    print('3 - Sair')

    op = valid_int('Escolha a opção desejada:', 1, 3)
    if op == 1:
        print('opção de cadastrar item selecionado \n')
        nomeJogo = input('Nome do jogo:')
        nomeVideoGame = input('Nome do video game:')
        cadastrarJogo(arquivo,nomeJogo,nomeVideoGame)
    elif op == 2:
        print('opção de listar selecionado \n')
        listarArquivo(arquivo)
    elif op == 3:
        print("Encerrando o programa...")
        break
