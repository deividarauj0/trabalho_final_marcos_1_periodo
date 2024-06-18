import json
from utils import ler_arquivo, escrever_arquivo, limpar_tela

livros = {}
codigo_livro = 0

def carregar_livros():
    global livros, codigo_livro
    try:
        livros = ler_arquivo('livros.json')
        if livros and isinstance(livros, dict):
            codigo_livro = max(map(int, livros.keys()))
        else:
            livros = {}
            codigo_livro = 0
    except FileNotFoundError:
        livros = {}
    except json.JSONDecodeError:
        print("Erro ao decodificar o arquivo JSON.")
        livros = {}

def salvar_livros():
    escrever_arquivo('livros.json', livros)

def menu_livros():
    while True:
        limpar_tela()
        print("Escolha uma opção: ")
        opcao = input("1-Cadastrar livro\n2-Pesquisar livro\n3-Listar livros\n4-Voltar\n\n")
        match opcao:
            case "1":
                cadastrar_livros()
            case "2":
                pesquisar_livros()
            case "3":
                listar_livros()
            case "4":
                break
            case _:
                print("Opção inválida. Tente novamente.")

def cadastrar_livros():
    global codigo_livro
    limpar_tela()
    codigo_livro += 1
    str_codigo_livro = str(codigo_livro)
    if str_codigo_livro in livros:
        print(f"Código já cadastrado.")
    else:
        titulo_livro = input("Título: ")
        autor_livro = input("Autor(es): ")
        isbn = input("ISBN: ")
        data_publicacao = input("Data de publicação (DDMMAAAA): ")

        if len(data_publicacao) == 8 and data_publicacao.isdigit():
            data_publicacao_formatada = f"{data_publicacao[:2]}/{data_publicacao[2:4]}/{data_publicacao[4:]}"
        else:
            limpar_tela()
            print("Data de publicação inválida. Use o formato DDMMAAAA.")
            input("\n\nAperte ENTER para voltar.")
            return

        editora_livro = input("Editora: ")
        numero_de_paginas_livro = input("Quantidade de páginas: ")
        genero_livro = input("Gênero: ")
        idioma_livro = input("Idioma: ")

        livros[str_codigo_livro] = {
            "titulo_livro": titulo_livro,
            "autor_livro": autor_livro,
            "isbn": isbn,
            "data_publicacao_formatada": data_publicacao_formatada,
            "editora_livro": editora_livro,
            "numero_de_paginas_livro": numero_de_paginas_livro,
            "genero_livro": genero_livro,
            "idioma_livro": idioma_livro
        }

        salvar_livros()
        print("Livro cadastrado com sucesso!\n\n")

def pesquisar_livros():
    limpar_tela()
    codigo = input("Informe o código do livro: ")
    if codigo in livros:
        livro = livros[codigo]
        print(f"\n\nTítulo: {livro['titulo_livro']}")
        print(f"Autor(es): {livro['autor_livro']}")
        print(f"ISBN: {livro['isbn']}")
        print(f"Data de publicação: {livro['data_publicacao_formatada']}")
        print(f"Editora: {livro['editora_livro']}")
        print(f"Quantidade de páginas: {livro['numero_de_paginas_livro']}")
        print(f"Gênero: {livro['genero_livro']}")
        print(f"Idioma: {livro['idioma_livro']}")
    else:
        print("Livro não encontrado.\n\n")

    input("\n\nAperte ENTER para voltar.")
    limpar_tela()

def listar_livros():
    limpar_tela()
    if not livros:
        print("Nenhum livro cadastrado.\n\n")
    else:
        for codigo_livro, dados in livros.items():
            print(f"Código: {codigo_livro}")
            print(f"Título: {dados['titulo_livro']}")
            print(f"Autor(es): {dados['autor_livro']}")
            print(f"ISBN: {dados['isbn']}")
            print(f"Data de publicação: {dados['data_publicacao_formatada']}")
            print(f"Editora: {dados['editora_livro']}")
            print(f"Quantidade de páginas: {dados['numero_de_paginas_livro']}")
            print(f"Gênero: {dados['genero_livro']}")
            print(f"Idioma: {dados['idioma_livro']}")
            print("\n")

    input("\n\nAperte ENTER para voltar.")
    limpar_tela()