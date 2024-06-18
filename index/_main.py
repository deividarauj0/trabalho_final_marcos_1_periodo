from clientes import menu_clientes, carregar_clientes, salvar_clientes
from livros import menu_livros, carregar_livros, salvar_livros
from emprestimos import menu_emprestimos, carregar_emprestimos, salvar_emprestimos
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
                menu_emprestimos()
            case "4":
                limpar_tela()
                break

carregar_clientes()
carregar_livros()

menu()

salvar_clientes()
salvar_livros()