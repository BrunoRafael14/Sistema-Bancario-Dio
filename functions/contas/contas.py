def criar_conta(*, cliente_dados, contas):
    if contas:
        conta = contas[-1]["Número da Conta"] + 1
    else:
        conta = 1

    cliente_dados.update({
        "Número da Conta": conta,
        "Agência": "0001"
    })

    return cliente_dados