def puxar_extrato(contas, /,*,status_login):
    for c in contas:
        if c["Número da Conta"] == status_login["Conta Ativa"]:
            print("\n================ EXTRATO ================")
            print("Não foram realizadas movimentações." if not c["extrato"] else c["extrato"])
            print(f"\nSaldo: R$ {c["saldo"]:.2f}")
            print("==========================================")