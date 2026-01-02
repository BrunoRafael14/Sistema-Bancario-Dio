def menu_contas(status_login, contas):
    while True:
        menu = """

    [t] trocar conta
    [c] criar Conta
    [q] Sair

    => """
        opcao = input(menu)
        if opcao == "t":
            trocar_conta(contas, status_login)
        elif opcao == "c":
            criar_conta(cliente=status_login, contas=contas)
        elif opcao == "q":
            break
        else:
            print("opção invalida")


def criar_conta(*, cliente, contas):
    if contas:
        conta = contas[-1]["Número da Conta"] + 1
    else:
        conta = 1

    contas.append({
        "CPF": cliente["CPF"],
        "Número da Conta": conta,
        "Agência": "0001",
        "saldo" : 0,
        "limite" : 500,
        "extrato" : "",
        "numero_saques": 0,
        "LIMITE_SAQUES": 3
    })

    return contas

def trocar_conta(contas, status_login):
    puxar_conta(contas, status_login)


# Função para puxar quais contas contas tem no CPF da pessoa logada
def puxar_conta(contas, status_login):
    for conta in contas:
        if conta["CPF"] == status_login["CPF"]:
            exibicao = f"""

Número da Conta: {conta["Número da Conta"]}
Agência: {conta["Agência"]}

======================
"""
            print(exibicao)


