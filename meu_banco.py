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

print(f"{nome_usuario}, agora escolha a opção que você deseja: ")

while True:
    opcao = input(menu).upper()

    if opcao == 'D':
        print("\nDepósito selecionado")
    
    elif opcao == 'S':
        print("\nSaque selecionado")
    
    elif opcao == 'E':
        print("\nExtrato selecionado")
    
    elif opcao == 'Q':
        print("\nAtendimento encerrado. Obrigado por nos escolher, tenha um bom dia!")
        break
    else:
        print("Operação inválida")

