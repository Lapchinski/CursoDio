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
#------------------------------------
    if opcao == "d": #Depositar
        valor = float(input("Informe o valor do deposito."))

        if valor > 0:
          saldo += valor
          extrato += f"Depósito: R$ {valor:.2f}\n"
          print(f"Depósito no valor de R$ {valor:.2f} realizado!")

        else:
           print(f"Operação falhou! R$ {valor:.2f} Valor invalido.")

#------------------------------------
    elif opcao == "s": #Sacar
        valor = float(input("Informe o valor pra saque."))

        sem_saldo = valor > saldo
        excedeu_limite = saldo > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if sem_saldo:
          print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
           print(f"Operação falhou! O valor solicitado é acima do limite de R$ {limite} disponivel!")
       
        elif excedeu_saques:
           print(f"Operação falhou! Numero máximo de {LIMITE_SAQUES} saques atingido!")

        elif valor > 0:
            saldo -= valor
            numero_saques += 1
            extrato += f"Saque: R$ {valor:.2f}\n"
            print(f"Saque de R$ {valor:.2f} concluido.")
        
        else:
           print("Operação falhou! Valor inválido.")
#------------------------------------
    elif opcao == "q": #Exit
        print("Obrigado por usar nosso sistema!")
        break

#------------------------------------
    elif opcao ==  "e": #Extrato
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
#------------------------------------
    else:
       print("Operação falhou! O valor informado é inválido.")
