from functions.operacoes.deposito import fazer_deposito
from functions.operacoes.extrato import puxar_extrato
from functions.operacoes.saque import fazer_saque
from functions.login.login import menu_login

status_login = {"Status": "off"}
clientes = []
contas = []

mensagem_inicial = 'Bem vindo'
print(mensagem_inicial.center(21, "="))

login = menu_login(clientes, status_login, contas)

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[t] Trocar Conta
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)
    if opcao == "d":
        valor = float(input("Informe o valor do Deposito: "))

        saldo, extrato = fazer_deposito(valor, saldo, extrato, contas, status_login)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        fazer_saque(valor=valor, contas=contas, status_login=status_login)

    elif opcao == "e":
        puxar_extrato(contas, status_login=status_login)

    elif opcao == "t":
        pass
    
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")