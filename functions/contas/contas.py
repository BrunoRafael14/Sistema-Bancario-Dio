def criar_conta(*, clientes, contas):
    if contas:
        conta = contas[-1]["Número da Conta"] + 1
    else:
        conta = 1

    contas.append({
        "CPF": clientes["CPF"],
        "Número da Conta": conta,
        "Agência": "0001"
    })

    return contas