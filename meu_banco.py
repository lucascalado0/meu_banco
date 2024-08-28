def depositar(valor):
    global saldo
    global numero_deposito 

    if valor > 0.0:
        saldo += valor

        numero_deposito += 1
    
    mensagem_deposito = f"\nR${quantia} depositado com sucesso!"

    return mensagem_deposito


def sacar(valor):
    global saldo
    global numero_saque

    if valor <= saldo:
        saldo-=valor

        numero_saque += 1

    mensagem_saque = f"\nR${quantia} sacada com sucesso!"

    return mensagem_saque
    

        
    
    

    


numero_deposito = 0
saldo = 0
limite = 500
extrato = " "
numero_saque = 0
LIMITE_SAQUE = 3

menu = """
##############

[D] Depósito
[S] Saque
[E] Extrato
[Q] Sair

##############

=> """

nome_usuario = input("Para inicializar o atendimento, informe o seu nome: ")

print(f"\nBem vindo ao nosso sistema, {nome_usuario}!")

print(f"Agora escolha a opção que você deseja: ")

while True:
    opcao = input(menu).upper()

    if opcao == 'D':
        print("\nDepósito selecionado\n")

        quantia = float(input("Informe o valor que deseja depositar: R$"))

        print(depositar(quantia))


        
    
    elif opcao == 'S':
        print("\nSaque selecionado")

        quantia = float(input("Informe a quantia que deseja sacar: R$"))

        if quantia <= saldo:
            print(sacar(quantia))
        
        else:
            print("\nSaldo insuficiente")
    
    elif opcao == 'E':
        print("\nExtrato selecionado")
    
    elif opcao == 'Q':
        print("\nAtendimento encerrado. Obrigado por nos escolher, tenha um bom dia!")
        break

    else:
        print("Operação inválida")

