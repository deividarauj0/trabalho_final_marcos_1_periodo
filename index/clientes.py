import json
from utils import ler_arquivo, escrever_arquivo, limpar_tela, data_atual, validar_cpf

clientes = {}

def carregar_clientes():
    global clientes
    try:
        with open('../dados_json/clientes.json', 'r') as arquivo:
            clientes = json.load(arquivo)
            if not isinstance(clientes, dict):
                clientes = {}
    except FileNotFoundError:
        clientes = {}
    return clientes

def salvar_clientes():
    escrever_arquivo('../dados_json/clientes.json', clientes)

def menu_clientes():
    while True:
        limpar_tela()
        print("Escolha uma opção: ")
        opcao = input("1-Cadastrar cliente\n2-Pesquisar cliente\n3-Listar clientes\n4-Voltar\n\n")
        match opcao:
            case "1":
                cadastrar_clientes()
            case "2":
                pesquisar_cliente()
            case "3":
                listar_clientes()
            case "4":
                salvar_clientes()
                break

def cadastrar_clientes():
    limpar_tela()
    cpf = input("CPF: ")

    if not validar_cpf(cpf):
        limpar_tela()
        print("CPF inválido. Tente novamente.\n\n")
        input("Aperte ENTER para voltar.")
        limpar_tela()
        return

    if cpf in clientes:
        limpar_tela()
        print("CPF já cadastrado.")
        input("\n\nAperte ENTER para voltar.")
        limpar_tela()
        return
    
    nome_completo = input("Nome completo: ")
    data_de_nascimento = input("Data de nascimento (DDMMAAAA): ")

    if len(data_de_nascimento) == 8 and data_de_nascimento.isdigit():
        data_nascimento_formatada = f"{data_de_nascimento[:2]}/{data_de_nascimento[2:4]}/{data_de_nascimento[4:]}"
    else:
        limpar_tela()
        print("Data de nascimento inválida. Use o formato DDMMAAAA.")
        input("\n\nAperte ENTER para voltar.")
        limpar_tela()
        return
    
    endereco = input("Endereço: ")
    telefone = input("Telefone (com DDD): ")

    if len(telefone) == 11 and telefone.isdigit():
        telefone_formatado = f"({telefone[:2]}) {telefone[2:7]}-{telefone[7:]}"
    else:
        limpar_tela()
        print("Telefone inválido. Use o formato correto com 11 dígitos.")
        input("\n\nAperte ENTER para voltar.")
        limpar_tela()
        return
    
    email = input("Email: ")
    data_cadastro = data_atual()

    clientes[cpf] = {
        "nome_completo": nome_completo,
        "data_nascimento_formatada": data_nascimento_formatada,
        "endereco": endereco,
        "telefone_formatado": telefone_formatado,
        "email": email,
        "data_cadastro": data_cadastro
    }

    salvar_clientes()
    limpar_tela()
    print("Cliente cadastrado com sucesso!\n\n")
    input("\n\nAperte ENTER para voltar.")
    limpar_tela()

def pesquisar_cliente():
    limpar_tela()
    pesquisar_cpf = input("Informe o CPF do cliente: ")
    cliente = clientes.get(pesquisar_cpf)
    if cliente:
        limpar_tela()
        print("Cliente encontrado:\n\n")
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
