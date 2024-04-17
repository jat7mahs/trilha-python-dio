import textwrap
from datetime import datetime

def menu():
    menu = """\n
    ================ MENU ================
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tNova conta
    [5]\tListar contas
    [6]\tNovo usuário
    [7]\tSair
    => Escolha sua opção: """
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato.append((datetime.now(), f"Depósito:\tR$ {valor:.2f}"))
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
    return saldo, extrato


def sacar(saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor <= 0:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
    elif valor > saldo:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
    elif valor > limite:
        print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")
    elif numero_saques >= limite_saques:
        print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
    else:
        saldo -= valor
        extrato.append((datetime.now(), f"Saque:\t\tR$ {valor:.2f}"))
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")
    return saldo, extrato, numero_saques


def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for data, transacao in extrato:
            print(f"{data.strftime('%d/%m/%Y %H:%M:%S')} - {transacao}")
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    if any(usuario["cpf"] == cpf for usuario in usuarios):
        print("\n@@@ Já existe usuário com esse CPF! @@@")
    else:
        nome = input("Informe o nome completo: ")
        data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
        endereco = input("Informe o endereço: ")
        usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
        print("=== Usuário criado com sucesso! ===")


def criar_conta(agencia, contas, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = next((usuario for usuario in usuarios if usuario["cpf"] == cpf), None)
    if usuario:
        conta = {"agencia": agencia, "numero_conta": len(contas) + 1, "usuario": usuario}
        contas.append(conta)
        print("\n=== Conta criada com sucesso! ===")
    else:
        print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")


def listar_contas(contas):
    print("\n=============== LISTA DE CONTAS ===============")
    for conta in contas:
        print(f"Agência:\t{conta['agencia']}\nC/C:\t\t{conta['numero_conta']}\nTitular:\t{conta['usuario']['nome']}\n")
    print("=" * 100)


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = []
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == '1':
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == '2':
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == '3':
            exibir_extrato(saldo, extrato)

        elif opcao == '4':
            criar_usuario(usuarios)

        elif opcao == '5':
            criar_conta(AGENCIA, contas, usuarios)

        elif opcao == '6':
            listar_contas(contas)

        elif opcao == '7':
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


if __name__ == "__main__":
    main()
