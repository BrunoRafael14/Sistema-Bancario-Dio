from functions.operacoes.deposito import fazer_deposito
from functions.operacoes.extrato import puxar_extrato
from functions.operacoes.saque import fazer_saque
from functions.login.login import menu_login
from functions.contas.contas import menu_contas

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
[c] Conta
[q] Sair

=> """


while True:

    opcao = input(menu)
    if opcao == "d":
        valor = float(input("Informe o valor do Deposito: "))

        fazer_deposito(valor, contas, status_login)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        fazer_saque(valor=valor, contas=contas, status_login=status_login)

    elif opcao == "e":
        puxar_extrato(contas, status_login=status_login)

    elif opcao == "c":
        menu_contas(status_login, contas)
    
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")