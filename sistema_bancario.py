menu = """

[0] Depositar
[1] Sacar
[2] Extrato
[3] Sair


=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITES_SAQUES = 3

while True:
    opcao = input(menu)
    
    if opcao == "0":
        valor = float(input (" Informe o valor do depósito: "))

        if valor> 0:
            saldo += valor
            extrato += f"deposito R${valor:.2f}\n"
        else: 
            print("operação falhou ! o valor informado é inválido")

    elif opcao == "1":
        valor = float(input("Informe o valor do Saque. "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITES_SAQUES
        
        if excedeu_saldo:
            print("Operação falhou, voce tem saldo insufuciente")

        elif excedeu_limite:
            print("Operação falhou, valor do saque excede o limite")

        elif excedeu_saques:
            print ("voce excedeu o limite de saques")

        elif valor > 0:
            saldo -= valor
            extrato += f"saque: R$ {valor:.2f}\n"          
            numero_saques +=1

        else:
            print("Operação falhou! o valor informado é inválido")    
    elif opcao == "2":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentacoes." if not extrato else extrato)
        print (f"\nSaldo: R$ {saldo:.2f}")



    elif opcao == "3":
        break

    else:
        print("Operação inválida, Selecione a operação desejada.")