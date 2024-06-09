from datetime import datetime

import json
from utils import ler_arquivo, escrever_arquivo, limpar_tela

clientes = []

def menu_clientes():
    while True:
        menu_clientes()
        opcao = input(f"1-Cadastrar cliente\n2-Pesquisar cliente\n3-Listar clientes\n4-Voltar")
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
    cpf = input(f"CPF: ")
    if cpf in clientes:
        print(f"CPF já cadastrado.")
    else:
        nome_completo = input(f"Nome completo: ")
        data_de_nascimento = input(f"Data de nascimento: ")
        endereco = input(f"Endereço: ")
        telefone = input(f"Telefone: ")
        email = input(f"Email: ")
        data_cadastro = datetime.now().strftime(f"%Y-%m-%d")

        clientes[cpf] = {
            "nome_completo" : nome_completo,
            "data_de_nascimento" : data_de_nascimento,
            "endereco" : endereco,
            "telefone" : telefone,
            "email" : email,
            "data_cadastrp" : data_cadastro
        }
        print("Cliente cadastrado com sucesso!")
def pesquisar_cliente():

def listar_clientes():