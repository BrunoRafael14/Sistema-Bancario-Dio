def menu_login(clientes, status_login):
    resposta = input("Você já possui login ? (s/n): ".center(30, "-"))
    if resposta == "s" or resposta == "sim":
        return logar_usuario(clientes, status_login)
    elif resposta == "n" or resposta == "não":
        return registrar_usuario(clientes = clientes)


# Refazer Tudo isso, com POO acho que vai ser mais fácil

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
        "Data de Nascimento": data_nascimento,
        "Senha": senha,
        "Endereço": endereco
    }

    return cliente

def registrar_usuario(*, clientes):
    cliente = puxar_informacoes()
    clientes = cliente
    print(clientes)

    return clientes



# aqui ainda vou ver como vai funcionar a questão de login, nesse caso, só vai ter acesso as funcionalidades de status = on ?, irei ver melhor
def logar_usuario(clientes, status_login, /):
    cpf = input("Informe seu CPF (Sem pontos ou espaços): ")
    senha = input("Informe senha para login")

    if cpf in clientes and senha in clientes:
        status_login="on"
    else:
        print("Usuário Não encontrado")
