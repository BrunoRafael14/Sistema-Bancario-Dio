def fazer_deposito(valor, saldo, extrato):
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(saldo, extrato)
        else:
            print("Operação falhou! O valor informado é inválido.")
    
        return saldo, extrato