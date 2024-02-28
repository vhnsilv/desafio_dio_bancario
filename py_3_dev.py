def menu():
    menu = """
    __________________________BANCO
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova conta
    [nu] Novo usuário    
    [q] Sair
    => """
    return input(menu)

def saque(*, saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):
    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1

    else:
            print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def deposito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"

    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def cadastro_usuario(usuarios):
    cpf = input('Informe o CPF(Somente números): ')
    usuario = filtro_usuario(cpf, usuarios)

    if usuario: 
        print('Já existe usuário com esse CPF!')
        return
    
    nome = input('Informe o nome completo: ')
    data_nascimento = input('Informe a data de nascimento (dd-mm-aaaa): ')
    endereco = input('Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ')

    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})
    
    print('Usuário cadastrado!')

def filtro_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def cadastro_conta(agencia, numero_conta, usuarios):
    cpf = input('Informe o CPF do usuário: ')
    usuario = filtro_usuario(cpf, usuarios)
    if usuario:
        print('Contra criada com sucesso!')
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}
    print('Usuário não encontrado!')

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    usuarios = []
    AGENCIA = '0001'
    contas = []
    

    while True:

        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = deposito(saldo, valor, extrato)
        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato = saque(valor=valor,
                                   saldo=saldo,
                                   limite=limite,
                                   numero_saques=numero_saques,
                                   LIMITE_SAQUES=LIMITE_SAQUES,
                                   extrato=extrato)
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
        elif opcao == 'nc':
            numero_conta = len(contas) + 1
            conta = cadastro_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)  
        elif opcao == 'nu':
            cadastro_usuario(usuarios)     
        elif opcao == "q":
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()