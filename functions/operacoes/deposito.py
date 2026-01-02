def fazer_deposito(valor, contas, status_login):
        if valor > 0:
            for c in contas:
                if c["Número da Conta"] == status_login["Conta Ativa"]:
                    c["saldo"] += valor
                    c["extrato"] += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido.")
            