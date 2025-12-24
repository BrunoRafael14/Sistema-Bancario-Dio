from functions.deposito import fazer_deposito
from functions.extrato import puxar_extrato
from functions.saque import fazer_saque

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
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
        
        saldo, extrato = fazer_deposito(valor, saldo, extrato)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        saldo, extrato, numero_saques = fazer_saque(valor=valor, extrato=extrato, saldo=saldo, limite=limite, numero_saques=numero_saques, LIMITE_SAQUES=LIMITE_SAQUES)


    elif opcao == "e":
        puxar_extrato(extrato, saldo=saldo)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")