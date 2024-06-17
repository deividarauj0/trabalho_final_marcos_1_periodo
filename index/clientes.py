import json
from utils import ler_arquivo, escrever_arquivo, limpar_tela, data_atual, validar_cpf

clientes = {}

def carregar_clientes():
    try:
        with open('clientes.json', 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return {}

def salvar_clientes():
    with open('clientes.json', 'w') as arquivo:
        json.dump(clientes, arquivo)

def menu_clientes():
    limpar_tela()
    while True:
        print("Escolha uma opção: ")
        opcao = input(f"1-Cadastrar cliente\n2-Pesquisar cliente\n3-Listar clientes\n4-Voltar\n\n")
        match opcao:
            case "1":
                cadastrar_clientes()
            case "2":
                pesquisar_cliente()
            case "3":
                listar_clientes()
            case "4":
                break


def cadastrar_clientes():
    limpar_tela()
    cpf = input(f"CPF: ")

    if not validar_cpf(cpf):
        limpar_tela()
        print(f"CPF inválido. Tente novamente.\n\n")
        return

    if cpf in clientes:
        limpar_tela()
        print(f"CPF já cadastrado.")
        input("\n\nAperte ENTER para voltar.")
        limpar_tela()
        return

    
    nome_completo = input(f"Nome completo: ")
    data_de_nascimento = input(f"Data de nascimento: ")
    data_nascimento_formatada = f"{data_de_nascimento[:2]}/{data_de_nascimento[2:4]}/{data_de_nascimento[4:]}"
    endereco = input(f"Endereço: ")
    telefone = input(f"Telefone: ")
    telefone_formatado = f"({telefone[:2]}) {telefone[2:7]}-{telefone[7:]}"
    email = input(f"Email: ")
    data_cadastro = data_atual()

    clientes[cpf] = {
        "nome_completo" : nome_completo,
        "data_nascimento_formatada" : data_nascimento_formatada,
        "endereco" : endereco,
        "telefone_formatado" : telefone_formatado,
        "email" : email,
        "data_cadastro" : data_cadastro
    }

    limpar_tela()
    print("Cliente cadastrado com sucesso!\n\n")

def pesquisar_cliente():
    limpar_tela()
    pesquisar_cpf = input(f"Informe o CPF do cliente: ")
    cliente = clientes.get(pesquisar_cpf)
    if cliente:
        limpar_tela()
        print(f"Cliente encontrado:\n\n")
        print(f"Nome: {cliente['nome_completo']}")
        print(f"Data de Nascimento: {cliente['data_nascimento_formatada']}")
        print(f"Endereço: {cliente['endereco']}")
        print(f"Telefone: {cliente['telefone_formatado']}")
        print(f"Email: {cliente['email']}")
        print(f"Data de Cadastro: {cliente['data_cadastro']}")
    else:
        limpar_tela()
        print("Cliente não encontrado.")
    
    input("\n\nAperte ENTER para voltar.")
    limpar_tela()

def listar_clientes():
    limpar_tela()
    if not clientes:
        print("Nenhum cliente cadastrado.")
    else:
        for cpf, dados in clientes.items():
            cpf_formatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
            print(f"Nome: {dados['nome_completo']}")
            print(f"CPF: {cpf_formatado}")
            print(f"Endereço: {dados['endereco']}")
            print(f"Telefone: {dados['telefone_formatado']}")
            print(f"Email: {dados['email']}")
            print(f"Data de Cadastro: {dados['data_cadastro']}\n")

    input("\n\nAperte ENTER para voltar.")
    limpar_tela()
