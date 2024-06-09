from clientes import menu_clientes
from livros import menu_livros
from emprestimos import emprestimos_livros

def menu():
    while True:
        menu()
        print("Escolha uma opção: ")
        opcao = input("1-Clientes\n2-Livros\n3-Empréstimos\n4-Sair ")
        match opcao:
            case "1":
                menu_clientes()
            case "2":
                menu_livros()
            case "3":
                emprestimos_livros()
            case "4":
                break