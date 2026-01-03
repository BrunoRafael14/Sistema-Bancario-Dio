from functions.contas.contas import criar_conta

def menu_login(clientes, status_login, contas):
    while True:
        resposta = input("Você já possui login ? (s/n): ".center(30, "-"))
        if resposta == "s" or resposta == "sim":
            return logar_usuario(clientes, status_login)
        elif resposta == "n" or resposta == "não":
            registrar_usuario(clientes = clientes, contas = contas)


def puxar_informacoes():
    nome = input("Informe seu nome completo: ")
    cpf = input("Informe seu CPF (Sem pontos ou espaços): ")
    data_nascimento = input("Informe sua data de nascimento (XX/XX/XXXX): ")
    senha = input("Crie uma senha: ")
    endereco = input("informe seu endereço (Logradouro, n°, bairro, cidade/sigla do estado): ").split(", ")
    endereco = "-".join(endereco)    

    cliente = {
        "Nome": nome,
        "CPF": cpf,
        "Senha": senha,
        "Data de Nascimento": data_nascimento,
        "Endereço": endereco
    }

    return cliente


def registrar_usuario(*, clientes, contas):
    cliente = puxar_informacoes()
    for c in clientes:
        if c["CPF"] == cliente["CPF"]: 
            print("Usuário já existente, favor fazer login")
            return
        
    contas = criar_conta(cliente=cliente, contas=contas)
    for conta in contas:
        if conta["CPF"] == cliente["CPF"]:
            cliente.update({"Contas": [conta["Número da Conta"]]})
            print(cliente)

    clientes.append(cliente) 
    


def logar_usuario(clientes, status_login, /):
    cpf = input("Informe seu CPF (Sem pontos ou espaços): ")
    senha = input("Informe senha para login: ")

    for cliente in clientes:
        if cliente["CPF"] == cpf and cliente["Senha"] == senha:
            status_login["Status"] = "on"
            status_login["CPF"] = cpf
            status_login["Conta Ativa"] = int(cliente["Contas"][0])
            #Tirar esse print
            print(status_login)
        else:
            print("Usuário Não encontrado")
