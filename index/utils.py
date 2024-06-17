from datetime import datetime
import json
import os
import re

def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []
    
def escrever_arquivo(nome_arquivo, dados):
    with open(nome_arquivo, 'w') as arquivo:
        json.dump(dados, arquivo, indent=4)

def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def data_atual():
    return datetime.now().strftime(f"%d-%m-%Y")

def validar_cpf(cpf):
    cpf = re.sub(r'\D', '', cpf)

    if len(cpf) != 11:
        return False

    if cpf == cpf[0] * len(cpf):
        return False
    
    def calcular_digito(cpf, multiplicadores):
        soma = sum(int(digito) * peso for digito, peso in zip(cpf, multiplicadores))
        resto = soma % 11
        return '0' if resto < 2 else str(11 - resto)
    
    multiplicadores_1 = range(10, 1, -1)
    multiplicadores_2 = range(11, 1, -1)
    
    if calcular_digito(cpf[:9], multiplicadores_1) != cpf[9]:
        return False
    
    if calcular_digito(cpf[:10], multiplicadores_2) != cpf[10]:
        return False
    
    return True