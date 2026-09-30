import pickle

print('MINECRAFT CRUD')
print('bem-vindo ao sistema!')

print('CADASTRO DE MINECRAFT')


try:
    with open('jogos.dat', 'rb') as arquivo:
        jogos = pickle.load(arquivo)
except FileNotFoundError:
    jogos = []


while True:

    print('\nMENU')
    print('1 - cadastrar jogo')
    print('2 - listar jogos')
    print('3 - atualizar jogo')
    print('4 - excluir jogo')
    print('5 - sair')

    opcao = input('escolha uma opção: ')

    # CADASTRAR
    if opcao == '1':
        nome = input('nome: ')
        plataforma = input('plataforma: ')
        ano = input('ano de lançamento: ')

        if nome.strip() == '' or plataforma.strip() == '' or ano.strip() == '':
            print('PREENCHA TODOS OS CAMPOS!')
            continue

        try:
            ano = int(ano)

            if ano < 1970 or ano > 2100:
                print('DIGITE UM ANO VÁLIDO!')
                continue

        except ValueError:
            print('O ANO DEVE SER UM NÚMERO!')
            continue

        jogo = {
            'nome': nome,
            'plataforma': plataforma,
            'ano': ano
        }

        jogos.append(jogo)

        with open('jogos.dat', 'wb') as arquivo:
            pickle.dump(jogos, arquivo)

        print('JOGO CADASTRADO COM SUCESSO!')

    # LISTAR
    elif opcao == '2':
        print('\nJOGOS CADASTRADOS:')

        for i, jogo in enumerate(jogos, start=1):
            print(f'{i} - {jogo["nome"]} - {jogo["plataforma"]} - {jogo["ano"]}')

    # ATUALIZAR
    elif opcao == '3':
        if len(jogos) == 0:
            print('NENHUM JOGO CADASTRADO.')
        else:
            print('\nJOGOS CADASTRADOS:')

            for i, jogo in enumerate(jogos, start=1):
                print(f'{i} - {jogo["nome"]} - {jogo["plataforma"]} - {jogo["ano"]}')

            try:
                numero = int(input('digite o número do jogo que deseja atualizar: '))

                if 1 <= numero <= len(jogos):
                    indice = numero - 1

                    novo_nome = input('novo nome: ')
                    nova_plataforma = input('nova plataforma: ')
                    novo_ano = input('novo ano: ')

                    if novo_nome.strip() == '' or nova_plataforma.strip() == '' or novo_ano.strip() == '':
                        print('PREENCHA TODOS OS CAMPOS!')
                        continue

                    try:
                        novo_ano = int(novo_ano)

                        if novo_ano < 1970 or novo_ano > 2100:
                            print('DIGITE UM ANO VÁLIDO!')
                            continue

                    except ValueError:
                        print('O ANO DEVE SER UM NÚMERO!')
                        continue

                    jogos[indice]['nome'] = novo_nome
                    jogos[indice]['plataforma'] = nova_plataforma
                    jogos[indice]['ano'] = novo_ano

                    with open('jogos.dat', 'wb') as arquivo:
                        pickle.dump(jogos, arquivo)

                    print('JOGO ATUALIZADO COM SUCESSO!')

                else:
                    print('NÚMERO INVÁLIDO!')

            except ValueError:
                print('DIGITE APENAS UM NÚMERO!')

    # EXCLUIR
    elif opcao == '4':
        if len(jogos) == 0:
            print('NENHUM JOGO CADASTRADO.')
        else:
            print('\nJOGOS CADASTRADOS:')

            for i, jogo in enumerate(jogos, start=1):
                print(f'{i} - {jogo["nome"]} - {jogo["plataforma"]} - {jogo["ano"]}')

            try:
                numero = int(input('digite o número do jogo que deseja excluir: '))

                if 1 <= numero <= len(jogos):
                    jogo_removido = jogos.pop(numero - 1)

                    with open('jogos.dat', 'wb') as arquivo:
                        pickle.dump(jogos, arquivo)

                    print(f'JOGO "{jogo_removido["nome"]}" EXCLUÍDO COM SUCESSO!')

                else:
                    print('NÚMERO INVÁLIDO!')

            except ValueError:
                print('DIGITE APENAS UM NÚMERO!')

    # SAIR
    elif opcao == '5':
        print('SAINDO DO SISTEMA...')
        break

    # OPÇÃO INVÁLIDA
    else:
        print('OPÇÃO INVÁLIDA!')