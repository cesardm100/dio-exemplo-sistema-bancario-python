menu = '''
  [d] Depositar
  [s] Sacar
  [e] Extrato
  [q] Sair
'''

saldo = 0.0
limite_saque = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    print(menu)
    opcao = input("Opção: ")

    if opcao == 'q':
        break
    
    elif opcao == 'd':
        valor = float(input("Valor: "))
        if valor < 0:
            print("Valor inválido")
            continue
        saldo += valor
        extrato += f'Depósito: {valor}\n'
    
    elif opcao == 's':

        if numero_saques >= LIMITE_SAQUES:
            print("Limite de saques atingido")
            continue
        
        valor = float(input("Valor: "))

        if valor < 0:
            print("Valor inválido")
            continue

        if valor > limite_saque:
            print("Limite de saque excedido")
            continue
        
        if valor > saldo:
            print("Saldo insuficiente")
            continue
        
        saldo -= valor
        extrato += f'Saque: {valor}\n'
        numero_saques += 1
    
    elif opcao == 'e':
        print(f'Saldo: R$ {saldo:.2f}')
        print(extrato)
    
    else:
        print("Opção inválida")
        