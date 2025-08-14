def main():  # Função principal
    while True:  # Escolhas do menu inicial
        escolha_inicial = menu_inicial()
        if escolha_inicial == 0:  # Sair do programa
            sair()
        elif escolha_inicial == 1:  # Fazer cadastro
            cadastrar()
        elif escolha_inicial == 2:  # Fazer login
            if login():
                while True:
                    escolha_principal = menu_principal()  # Escolhas do menu principal
                    if escolha_principal == 0:  # Sair do programa
                        sair()
                    elif escolha_principal == 1:  # Pesquisa de musicas
                        musica_pesquisa()
                    elif escolha_principal == 2:  # Escolhas do menu playlist
                        while True:
                            opcao_playlist = playlist()
                            if opcao_playlist == 1:  # Criação de playlist
                                criar_playlist()
                            elif opcao_playlist == 2:  # Remoção de músicas na playlist
                                remover_musica_playlist()
                            elif opcao_playlist == 3:  # Excluir uma playlist
                                excluir_playlist()
                            elif opcao_playlist == 4:  # Visualização de playlist
                                visualizar_playlist()
                            elif opcao_playlist == 0:  # Voltar para o menu principal
                                break
                            else:  # Validação de entrada do usúario
                                print(
                                    "--------------------------------------------------------------------------------"
                                )
                                print("🔴Digite uma opção válida🔴\n")
                    elif escolha_principal == 3:  # Escolhas do menu historico
                        while True:
                            opcao_hist = historico()
                            if (
                                opcao_hist == 1
                            ):  # Visualização do historico de músicas curtidas
                                curtidas_historico()
                            elif (
                                opcao_hist == 2
                            ):  # Visualização do historico de músicas descurtidas
                                descurtidas_historico()
                            elif opcao_hist == 0:  # Voltar para o menu principal
                                break
                            else:  # Validação de entrada do usúario
                                print(
                                    "--------------------------------------------------------------------------------"
                                )
                                print("🔴Digite uma opção válida🔴\n")
                    else:  # Validação de entrada do usúario
                        print(
                            "--------------------------------------------------------------------------------"
                        )
                        print("🔴Digite uma opção válida🔴\n")


def menu_inicial():  # Menu de cadastro e login
    menu_inicial = {
        1: "Cadastrar",
        2: "Login",
        0: "Sair",
    }
    print("\n")
    print("🟢 Bem vindo ao Spotifei 🟢")
    print("Feito por:Gabriel Pacioni Coelho\n")
    for opcao, descricao in menu_inicial.items():
        print(f"{opcao} - {descricao}")  # Impressão do menu inicial
    escolha_inicial = int(input("Escolha uma opção: "))
    return escolha_inicial


def cadastrar():  # Opção de cadastro
    nome = input("Qual seu nome completo: ")
    newusu = input("Qual o seu nome de usuário: ")
    while True:
        newsenha = input("Digite sua senha: ")
        newsenhaconfir = input("Digite sua senha novamente: ")
        if newsenha == newsenhaconfir:  # confirmação de senhas iguais
            break
        else:
            print(
                "--------------------------------------------------------------------------------"
            )
            print("🔴Senhas diferentes!🔴\n")

    with open("usuarios.txt", "a") as arquivo:
        arquivo.write(
            f"{nome},{newusu},{newsenha}\n"
        )  # Salva no arquivo txt o novo usuario

    print(f"Usuário {newusu} cadastrado no Spotifei!")


usuario_logado = False


def login():  # Opção de login
    global usuario_logado  # Variável global para diferenciar dados de cada usuario
    usuario = input("Qual o usuário: ")
    senha = input("Qual a senha: ")
    dados_usuario = []
    with open("usuarios.txt", "r") as arquivo:
        for linha in arquivo:
            dados_usuario.append(linha.strip().split(","))

    for dado in dados_usuario:
        if (
            dado[1].lower() == usuario.lower() and dado[2] == senha
        ):  # O elemento dado[1] sendo o usuario e o dado[2] a senha
            usuario_logado = usuario
            print(f"Usuário: {usuario}, Seja bem-vindo ao Spotifei!!")
            return usuario

    print(f"🔴 Usuário ou senha incorretos 🔴")
    return False


def menu_principal():  # Menu com as principais escolhas
    menu_principal = {
        1: "→Buscar(Procure as melhores músicas!)🎙️\n",  # Opção de pesquisar músicas
        2: "→Playlists(Veja e crie suas playlists!)🎶\n",  # Opções da playlist
        3: "→Histórico(Aqui você encontra seu historico de músicas curtidas)💭\n",  # Opções de veisualizar historico
        0: "→Sair\n",
    }
    print("\n")
    print("🟢Bem vindo ao Spotifei🟢")
    print("Feito por:Gabriel Pacioni Coelho\n")
    for opcao, descricao in menu_principal.items():
        print(f"{opcao} - {descricao}")  # Impressão do menu principal
    escolha_principal = int(input("Escolha uma opção: "))
    return escolha_principal


def musica_pesquisa():  # Pesquisa da música
    pesquisa_musica = input("Digite a música que deseja ouvir: ")
    with open("musicas.txt", "r") as arquivo_musicas:
        musicas_dados = arquivo_musicas.readlines()

    for musicas in musicas_dados:
        nome_musica, nome_artista, duracao, album = musicas.strip().split(",")
        if (
            pesquisa_musica.lower() == nome_musica.lower()
        ):  # Confirma se a música existe e é a procurada pelo usúario
            print(f"\n🎵{nome_musica} - {nome_artista} ({duracao}) | Álbum: {album}\n")
            return menu_musicas(nome_musica, nome_artista, duracao, album)
    else:
        print("🔴Música não encontrada.🔴")


def menu_musicas(
    nome_musica, nome_artista, duracao, album
):  # Menu de opções na música/Como curtir, descurtir ou adicionar á playlist
    menu_musicas = {
        1: "Ouvir",
        2: "Curtir",
        3: "Descurtir",
        4: "Adicionar á playlist",
        0: "Voltar ao menu",
    }
    for opcao, descricao in menu_musicas.items():
        print(f"{opcao} - {descricao}")  # impressão das opções disponiveis por música
    escolha_musical = int(input("Escolha uma opção: "))

    if escolha_musical == 1:  # Opção de tocar a musica
        print(f"\nTocando:▶️ {nome_musica} -- ({duracao})\n")
    elif escolha_musical == 2:  # Opção de curtir a musica
        with open("curtidas.txt", "a") as arquivo:
            arquivo.write(
                f"{nome_musica},{nome_artista},{duracao},{album},{usuario_logado}\n"
            )
            print("\nMúsica curtida com sucesso")
    elif escolha_musical == 3:  # Opção de descurtir a musica
        with open("descurtidas.txt", "a") as arquivo:
            arquivo.write(
                f"{nome_musica},{nome_artista},{duracao},{album},{usuario_logado}\n"
            )
            print("\nMúsica descurtida com sucesso")
    elif escolha_musical == 4:  # Opção de adicionar á playlist(já criada)
        adicionar_playlist = input(
            "Digite o nome da playlist que você quer adicionar música: "
        )
        with open("playlists.txt", "a") as arquivo:
            arquivo.write(
                f"{adicionar_playlist},{nome_musica},{nome_artista},{duracao},{album},{usuario_logado}\n"
            )
            print(f"Música adicionada à playlist: ({adicionar_playlist})")
    elif escolha_musical == 0:  # Voltar ao menu principal
        return menu_principal()


def playlist():  # Menu de playlist(criação/remoção de musica/excluir/visualizar)
    menu_playlist = {
        1: "•Criar",
        2: "•Remover músicas",
        3: "•Excluir",
        4: "•Visualizar",
        0: "•Voltar ao menu\n",
    }
    print("\nVocê pode criar/editar/excluir sua Playlist aqui!🎧\n")
    for opcao, descricao in menu_playlist.items():
        print(f"{opcao} - {descricao}")
    opcao_playlist = int(input("Escolha uma opção: "))
    return opcao_playlist


def criar_playlist():  # Criação de playlists
    nome_playlist = input("Digite o nome da playlist que você deseja criar: ")
    with open("playlists.txt", "a") as arquivo:
        arquivo.write(f"{nome_playlist},_,_,_,_,{usuario_logado}\n")
        print(f"🟢A sua playlist foi criada com sucesso🟢")


def remover_musica_playlist():  # Função de remoção de música em uma playlist
    encontrar_playlist = input(
        "Digite o nome da playlist da qual deseja remover uma música: "
    )

    with open("playlists.txt", "r") as arquivo:
        conteudo = arquivo.readlines()

    print(f"Musicas da playlist: {encontrar_playlist}")
    for (linha) in (conteudo):  # Loop para impressao das musicas presentes na playlist procurada pelo usuario
        nome_playlist, nome_musica, nome_artista, duracao, album, usuario = (
            linha.strip().split(",")
        )
        if (
            encontrar_playlist == nome_playlist
            and usuario == usuario_logado
            and nome_musica != "_"
        ):
            print(f"- {nome_musica} ({duracao}), {nome_artista} | Álbum: {album}")

    remover_musica = input("Digite o nome da música que deseja remover: ")
    outras_musicas = []
    musica_removida = False

    for (linha) in (conteudo):
        nome_playlist, nome_musica, nome_artista, duracao, album, usuario = linha.strip().split(",")
        if not (
            encontrar_playlist == nome_playlist
            and remover_musica.lower() == nome_musica.lower()
            and usuario == usuario_logado
        ):

            outras_musicas.append(linha)
        else:
            musica_removida = True
            print(f"Removendo música: {nome_musica} ({duracao}) de {nome_artista}")

    if (
        musica_removida
    ):  
        with open("playlists.txt", "w") as arquivo:
            for linha in outras_musicas:  
             arquivo.write(linha)
        print("🟢Música removida com sucesso.🟢")
    else:
        print("🔴 Música não encontrada na playlist desejada.🔴")


def excluir_playlist():
    apagar_playlist = input("Digite o nome da playlist que deseja excluir: ")
    with open("playlists.txt", "r") as arquivo:
        conteudo = arquivo.readlines()

    playlist_antigas = []
    playlist_encontrada = False

    for linha in conteudo:
        nome_playlist, _, _, _, _, usuario = linha.strip().split(",")
        if apagar_playlist == nome_playlist and usuario == usuario_logado:
            print(f"Removendo: {linha.strip()}")
            playlist_encontrada = True
        else:
            playlist_antigas.append(linha)

    if playlist_encontrada:
        with open("playlists.txt", "w") as arquivo:
            for linha in playlist_antigas:
                arquivo.write(linha)
        print("\n🟢Todas as músicas da playlist foram removidas com sucesso.🟢")
    else:
        print("🔴Playlist não encontrada.🔴")


def visualizar_playlist():
    visu_playlist = input("Digite o nome da playlist que você deseja visualizar: ")
    with open("playlists.txt", "r") as arquivo:
        conteudo = arquivo.readlines()

    playlist_encontrada = False
    print(f"\n🎧 Músicas da playlist '{visu_playlist}' de {usuario_logado}:")

    for linha in conteudo:
        nome_playlist, nome_musica, nome_artista, duracao, album, usuario = (
            linha.strip().split(",")
        )
        if (
            visu_playlist == nome_playlist
            and usuario == usuario_logado
            and nome_musica != "_"
        ):
            print(f"- {nome_musica} ({duracao}), {nome_artista} | Álbum: {album}")
            playlist_encontrada = True

    if playlist_encontrada == False:
        print("🔴Playlist não encontrada ou vazia.🔴")


def historico():  # Menu de historico
    menu_historico = {1: "•Curtidas", 2: "•Descurtidas", 0: "•Voltar ao menu\n"}
    print("\nHistórico de músicas:\n")
    for opcao, descricao in menu_historico.items():
        print(f"{opcao} - {descricao}")
    opcao_hist = int(input("Escolha uma opção: "))
    return opcao_hist


def curtidas_historico():  # Mostrar as musicas curtidas
    with open("curtidas.txt", "r") as arquivo_curtidas:
        curtidas_dados = arquivo_curtidas.readlines()
        print("\nMúsicas curtidas:")
        for linha in curtidas_dados:
            nome_musica, nome_artista, duracao, album, usuario = linha.strip().split(
                ","
            )
            if usuario == usuario_logado:
                print(
                    f"{nome_musica} ({duracao}), Artista: {nome_artista}, Álbum: {album}"
                )


def descurtidas_historico():  # Mostrar as musicas descurtidas
    with open("descurtidas.txt", "r") as arquivo_descurtidas:
        descurtidas_dados = arquivo_descurtidas.readlines()
        print("\nMúsicas descurtidas:")
        for linha in descurtidas_dados:
            nome_musica, nome_artista, duracao, album, usuario = linha.strip().split(
                ","
            )
            if usuario == usuario_logado:
                print(
                    f"{nome_musica} ({duracao}), Artista: {nome_artista}, Álbum: {album}"
                )


def sair():  # Função de saida do programa
    print("Saindo do Spotifei...")
    exit()


if __name__ == "__main__":  # Excecução da função principal
    main()
