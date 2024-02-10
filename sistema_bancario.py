import textwrap


# Separar as funções existentes em
# - Saque
#     Keyword only (saldo, valor, extrato, limite, limite_saques, numero_saques) retornando saldo e extrato
# - Depósito
#     Positional only (saldo, valor, extrato) retornando saldo e extrato
# - Extrato
#     Positional (saldo) and keyword (extrato)


# Criar duas novas funções
# - Cadastrar cliente
#     Nome, data nascimento, cpf e endereco (string formada por logradouro, nro - bairro - cidade/Sigla Estado)
#     CPF deve ser unico
# - Conta Bancária
#     Agencia, numero da conta e sequencial
#     Numero da agencia deve ser fixo "0001"
#     Cada conta pertence a apenas um usuário



def menu():
    menu = """\n
    ============ Menu ============
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tListar Contas
    [nu]\tNovo Usuário
    [q]\tSair
    =>"""
    return input(textwrap.dedent(menu))

def saque(*, saldo, valor, extrato, limite_valor_saque, numero_quantidade_saques, numero_saques):
 
    if numero_saques >= numero_quantidade_saques:
        print("Erro: Limite de saques atingido")
    elif valor <= 0:
        print("Erro: Valor inválido")
    elif valor > limite_valor_saque:
        print("Erro: Limite de saque excedido")
    elif valor > saldo:
        print("Erro: Saldo insuficiente")
    else:
        saldo -= valor
        extrato += f'Saque: {valor}\n'
        numero_saques += 1
        print(f"==> Valor sacado: R$ {valor}")
    return saldo, extrato

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'Depósito: {valor}\n'
        print(f"===> Valor depositado: R$ {valor}")
    else:
        print("Valor inválido")

    return saldo, extrato

def exibir_extrato(saldo, *, extrato):
    print(f'Saldo: R$ {saldo:.2f}')
    print(extrato)

def criar_usuario(usuarios):
    cpf = input("Informe o CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Erro: CPF já cadastrado")
        return
    nome = input("Informe o nome: ")
    data_nascimento = input("Informe a data de nascimento: ")
    endereco = input("Informe o endereço: ")

    usuarios.append({
        'cpf': cpf,
        'nome': nome,
        'data_nascimento': data_nascimento,
        'endereco': endereco
    })

    print("Usuário cadastrado com sucesso")

def filtrar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            return usuario
    return None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        return { "agenca": agencia, "numero_conta": numero_conta, "usuario": usuario }

    print("Erro: usuario nao encontrado. Cadasrto de conta encerrado!")



def main():
    QTD_LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0.0
    limite_valor_saque = 500
    extrato = ''
    numero_quantidade_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == 'q':
            break
        
        elif opcao == 'd':
            valor = float(input("Valor: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == 's':
            valor = float(input("Valor: "))
            saldo, extrato = saque(
                saldo=saldo, 
                valor=valor, 
                extrato=extrato, 
                limite_valor_saque=limite_valor_saque, 
                numero_quantidade_saques=QTD_LIMITE_SAQUES, 
                numero_saques=numero_quantidade_saques
            )
        
        elif opcao == 'e':
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == 'nu':
            criar_usuario(usuarios)   

        elif opcao == 'lc':
            print("============== Contas ===============")
            for conta in contas:
                linha_conta = f"""\
                    Agencia: {conta['agenca']} - {conta['numero_conta']}
                    Nome: {conta['usuario']['nome']}
                    CPF: {conta['usuario']['cpf']}"""
                print(linha_conta)

        elif opcao == 'nc':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)  
            if conta:
                contas.append(conta)  
        else:
            print("Opção inválida")

main()
            