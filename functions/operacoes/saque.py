def fazer_saque(*, valor, contas, status_login):
    for c in contas:
        if int(c["Número da Conta"]) == status_login["Conta Ativa"]:
            if valor > c["saldo"]:
                print("Operação falhou! você não tem saldo suficiente. ")
            elif valor > c["limite"]:
                print("Operação falhou! O valor do saque excede o limite.")
            elif c["numero_saques"] > c["LIMITE_SAQUES"]:
                print("Operação falhou! Número máximo de saques excedido.")
            elif valor > 0:
                c["saldo"] -= valor
                c["extrato"] += f"Saque: R$ {valor:.2f}\n"
                c["numero_saques"] += 1
         
        else: 
            print("Operação falhou! O valor informado é inválido.")