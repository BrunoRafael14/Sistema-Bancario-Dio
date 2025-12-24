def fazer_saque(*, valor, extrato, saldo, limite, numero_saques, LIMITE_SAQUES):
    if valor > saldo:
        print("Operação falhou! você não tem saldo suficiente. ")
    elif valor > limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif numero_saques > LIMITE_SAQUES:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else: 
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques