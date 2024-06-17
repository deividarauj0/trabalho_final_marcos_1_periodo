import json
from utils import ler_arquivo, escrever_arquivo, limpar_tela

livros = []
codigo_livro = 0

def menu_livros():
    limpar_tela()
    while True:
        print("Escolha uma opção: ")
        opcao = input(f"1-Cadastrar livro\n2-Pesquisar livro\n3-Listar livros\n4-Voltar\n\n")
        match opcao:
            case "1":
                cadastrar_livros()
            case "2":
                pesquisar_livros()
            case "3":
                listar_livros()
            case "4":
                break

def cadastrar_livros():
    limpar_tela()
    codigo_livro = codigo_livro + 1
    if codigo_livro in livros:
        print(f"Código já cadastrado.")
    else:
        titulo_livro = input(f"Título: ")
        autor_livro = input(f"Autor(es): ")
        isbn = input(f"ISBN: ")
        data_publicacao = input(f"Data de publicação: ")
        editora_livro = input(f"Editora: ")
        numero_de_paginas_livro = input(f"Quantidade de páginas: ")
        genero_livro = input(f"Gênero: ")
        idioma_livro = input(f"Idioma: ")

        livros[codigo_livro] = {
            "titulo_livro" : titulo_livro,
            "autor_livro" : autor_livro,
            "isbn" : isbn,
            "data_publicacao" : data_publicacao,
            "editora_livro" : editora_livro,
            "numero_de_paginas_livro" : numero_de_paginas_livro,
            "genero_livro" : genero_livro,
            "idioma_livro" : idioma_livro
        }

def pesquisar_livro():
    limpar_tela()
    pesquisar_cpf = input(f"Informe o CPF do cliente: ")
    cliente = clientes.get(cpf)
    if cliente:
        print(f"Cliente encontrado: Nome: {cliente['nome_completo']}, Data de Nascimento: {cliente['data_de_nascimento']}, Endereço: {cliente['endereco']}, Telefone: {cliente['telefone']}, Email: {cliente['email']}, Data de Cadastro: {cliente['data_cadastro']}")
        return None
    else:
        print("Cliente não encontrado.")
        return None

def listar_livros():
    limpar_tela()
    for livro in livros:
        print(livro)