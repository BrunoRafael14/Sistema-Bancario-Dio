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