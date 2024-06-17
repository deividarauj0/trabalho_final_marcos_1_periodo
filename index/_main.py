from clientes import menu_clientes, carregar_clientes, salvar_clientes
from livros import menu_livros, carregar_livros, salvar_livros
#from emprestimos import emprestimos_livros#
from utils import limpar_tela

def menu():
    while True:
        limpar_tela()
        print("Escolha uma opção: ")
        opcao = input("1-Clientes\n2-Livros\n3-Empréstimos\n4-Sair\n\n")
        match opcao:
            case "1":
                menu_clientes()
            case "2":
                menu_livros()
            case "3":
                emprestimos_livros()
            case "4":
                limpar_tela()
                break

livros = carregar_livros()
clientes = carregar_clientes()
menu()
salvar_clientes()