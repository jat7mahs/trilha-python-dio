
numero_saque_max = 3
cont_saque = saldo = 0
saque_maximo = 500
extrato = ' '

while True:
    print('[1] DEPÓSITO \n'
          '[2] SAQUE \n'
          '[3] EXTRATO \n'
          '[4] SAIR')
    escolha = int(input('Selecione a opção: '))

    if escolha == 1:
        entrada_saida = float(input('Qual valor você quer depositar: '))

        if entrada_saida > 0:
            saldo += entrada_saida
            extrato += f'Depósito R${entrada_saida:.2f}\n'
        else:
            print('OPERAÇÃO INVÁLIDA!!!')


    elif escolha == 2:
        entrada_saida = float(input('Qual valor do saque: '))
        cont_saque += 1

        if saldo > 0:
            if entrada_saida <= saque_maximo or cont_saque <= numero_saque_max:
                saldo -= entrada_saida
                extrato += f'Saque R${entrada_saida:.2f}'
        else:
            print('OPERAÇÃO INVÁLIDA!!!')

    elif escolha == 3:
        print('='*30)
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print('=' * 30)

    elif escolha == 4:
        break

    else:
        print('OPÇÃO INVÁLIDA!!!')