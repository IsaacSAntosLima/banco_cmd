saldo = float(1000)
while True:
    print("\n========= Bem Vindo(a) ao seu banco digital =========")
    print("1- ver saldo")
    print("2- depositar")
    print("3- sacar")
    print("4- sair")
    resp = int(input("Oque deseja realizar? "))
    if resp == 1:
         print("Seu saldo é de : R${}".format(saldo))
    elif resp == 2:
        dep = float(input("Quanto deseja depositar? "))
        print("O valor de R${} foi depositado com sucesso. ".format (dep))
    elif resp == 3:
        sac = float(input("quanto voce deseja sacar? "))
        if sac > saldo:
            print("Saldo indisponivel")
        else:
            saldo = (saldo-sac)
            print("Saque realizado com sucesso.")
    elif resp == 4:
        print("Sessão finalizada!")
        break

    else:
        print("Opção invalida, tente novamente")
