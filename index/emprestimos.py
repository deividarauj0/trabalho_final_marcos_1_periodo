import json
from utils import ler_arquivo, escrever_arquivo, limpar_tela, data_atual
from clientes import carregar_clientes
from livros import carregar_livros
from datetime import datetime

emprestimos = {}

def carregar_emprestimos():
    global emprestimos
    try:
        with open('emprestimos.json', 'r') as arquivo:
            emprestimos = json.load(arquivo)
            if not isinstance(emprestimos, dict):
                emprestimos = {}
    except FileNotFoundError:
        emprestimos = {}

def salvar_emprestimos():
    escrever_arquivo('emprestimos.json', emprestimos)

def menu_emprestimos():
    while True:
        limpar_tela()
        print("Escolha uma opção: ")
        opcao = input("1-Registrar empréstimo\n2-Pesquisar empréstimo\n3-Listar empréstimos\n4-Voltar\n\n")
        match opcao:
            case "1":
                registrar_emprestimo()
            case "2":
                pesquisar_emprestimo()
            case "3":
                listar_emprestimos()
            case "4":
                salvar_emprestimos()
                break

def registrar_emprestimo():
    limpar_tela()
    clientes = carregar_clientes()
    livros = carregar_livros()

    if not clientes:
        limpar_tela()
        print("Nenhum cliente cadastrado.")
        input("\n\nAperte ENTER para voltar.")
        limpar_tela()
        return

    if not livros:
        limpar_tela()
        print("Nenhum livro cadastrado.")
        input("\n\nAperte ENTER para voltar.")
        limpar_tela()
        return

    cpf_cliente = input("CPF do cliente: ")
    if cpf_cliente not in clientes:
        limpar_tela()
        print("Cliente não encontrado.")
        input("\n\nAperte ENTER para voltar.")
        limpar_tela()
        return

    codigo_livro = input("Código do livro: ")
    if codigo_livro not in livros:
        limpar_tela()
        print("Livro não encontrado.")
        input("\n\nAperte ENTER para voltar.")
        limpar_tela()
        return

    data_emprestimo = data_atual()

    while True:
        data_devolucao = input("Data de devolução (DDMMAAAA): ")
        try:
            data_devolucao_obj = datetime.strptime(data_devolucao, "%d%m%Y")
            break
        except ValueError:
            limpar_tela()
            print("Data de devolução inválida. Use o formato DDMMAAAA.")
            input("\n\nAperte ENTER para voltar.")
            limpar_tela()
            continue

    if data_devolucao_obj < datetime.now():
        limpar_tela()
        print("Data de devolução inválida. Deve ser uma data futura.")
        input("\n\nAperte ENTER para voltar.")
        limpar_tela()
        return

    data_devolucao_formatada = data_devolucao_obj.strftime("%d/%m/%Y")

    codigo_emprestimo = str(len(emprestimos) + 1)
    emprestimos[codigo_emprestimo] = {
        "cpf_cliente": cpf_cliente,
        "codigo_livro": codigo_livro,
        "data_emprestimo": data_emprestimo,
        "data_devolucao": data_devolucao_formatada
    }

    salvar_emprestimos()
    limpar_tela()
    print("Empréstimo registrado com sucesso!\n\n")
    input("\n\nAperte ENTER para voltar.")
    limpar_tela()

def pesquisar_emprestimo():
    limpar_tela()
    codigo = input("Informe o código do empréstimo: ")
    emprestimo = emprestimos.get(codigo)
    if emprestimo:
        limpar_tela()
        print("Empréstimo encontrado:\n\n")
        print(f"CPF do Cliente: {emprestimo['cpf_cliente']}")
        print(f"Código do Livro: {emprestimo['codigo_livro']}")
        print(f"Data de Empréstimo: {emprestimo['data_emprestimo']}")
        print(f"Data de Devolução: {emprestimo['data_devolucao']}")
    else:
        limpar_tela()
        print("Empréstimo não encontrado.")
    
    input("\n\nAperte ENTER para voltar.")
    limpar_tela()

def listar_emprestimos():
    limpar_tela()
    if not emprestimos:
        print("Nenhum empréstimo registrado.")
    else:
        for codigo_emprestimo, dados in emprestimos.items():
            print(f"Código: {codigo_emprestimo}")
            print(f"CPF do Cliente: {dados['cpf_cliente']}")
            print(f"Código do Livro: {dados['codigo_livro']}")
            print(f"Data de Empréstimo: {dados['data_emprestimo']}")
            print(f"Data de Devolução: {dados['data_devolucao']}\n")

    input("\n\nAperte ENTER para voltar.")
    limpar_tela()
