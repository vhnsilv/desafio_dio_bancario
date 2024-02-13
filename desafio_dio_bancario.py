menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == 'd':
        deposito = float(input('Digite a quantia a ser depositada: '))
        if deposito > 0:
            saldo += deposito
            extrato += f'Deposito: R$ {deposito:.2f}\n'
        else:
            print('Valor informado é invalido')    
    

    elif opcao == 's':
        saque = float(input('Digite o valor para saque: '))
        if numero_saques >= LIMITE_SAQUES:
            print('Numero de saque diario exedido')
        elif saque > saldo:
            print('Você não tem saldo para saque')
        elif saque > limite:
            print('Você ultrapassou o limite de saque. Limite de saque no valor de RS500,00')
        elif saque > 0:
            saldo -= saque
            extrato += f'Saque: RS {saque:.2f}\n'
            numero_saques += 1

    elif opcao == 'e':
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
        
    elif opcao == 'q':
        print('Sair')
        break
    else:
        print('Está opção não é valida. Tente novamente ultilizando as opções fornecidas.')