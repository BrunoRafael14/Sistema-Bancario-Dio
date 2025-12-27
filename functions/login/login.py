from functions.contas.contas import criar_conta

def menu_login(clientes, status_login, contas):
    resposta = input("Você já possui login ? (s/n): ".center(30, "-"))
    if resposta == "s" or resposta == "sim":
        return logar_usuario(clientes, status_login)
    elif resposta == "n" or resposta == "não":
        return registrar_usuario(clientes = clientes, contas = contas)


def puxar_informacoes():
    nome = input("Informe seu nome completo: ")
    cpf = input("Informe seu CPF (Sem pontos ou espaços): ")
    data_nascimento = input("Informe sua data de nascimento (XX/XX/XXXX): ")
    senha = input("Crie uma senha: ")
    endereco = input("informe seu endereço (Logradouro, n°, bairro, cidade/sigla do estado): ").split(", ")
    endereco = "-".join(endereco)    

    cliente_dados = {
        "Nome": nome,
        "CPF": cpf,
        "Senha": senha,
        "Data de Nascimento": data_nascimento,
        "Endereço": endereco
    }

    return cliente_dados


def registrar_usuario(*, clientes, contas):
    cliente_dados = puxar_informacoes()
    cliente = criar_conta(cliente_dados=cliente_dados, contas=contas, clientes=clientes)
    clientes = cliente
    print(clientes)

    return clientes



# Para terminar esse, primeiro terei que criar a opção de criar conta, para posteriormente com o login, puxar essa conta principal
def logar_usuario(clientes, status_login, /):
    cpf = input("Informe seu CPF (Sem pontos ou espaços): ")
    senha = input("Informe senha para login")

    if cpf in clientes and senha in clientes:
        pass
    else:
        print("Usuário Não encontrado")
