####### Funções utilizadas no código #######

def depositar(valor): 
    global saldo
    global numero_deposito 
    global valor_depositado

    if valor > 0.0:
        saldo += valor
        valor_depositado += valor

        numero_deposito += 1
    
        mensagem_deposito = f"\nR${quantia:.2f} depositado com sucesso!"

        return mensagem_deposito


def sacar(valor):
    global saldo
    global numero_saque

    if valor <= saldo:
        saldo-=valor
        global valor_sacado 
        valor_sacado += valor
        
        numero_saque += 1

    mensagem_saque = f"\nR${quantia:.2f} sacada com sucesso!"

    return mensagem_saque

def extrato():
    
    print(" Extrato Bancário ".center(44,"#"))
    extrato = f"""
    \n->Número de depósitos: {numero_deposito}
    \n->Valor depositado: R${valor_depositado:.2f}
    \n->Número de saques: {numero_saque}
    \n->Valor sacado: R${valor_sacado:.2f}
    \n->Saldo atual da conta: R${saldo:.2f}
    """
    return extrato

####### Fim das funções #######   


####### Variáveis utilizadas #######
    
valor_sacado = 0
valor_depositado = 0
numero_deposito = 0
saldo = 0
limite = 500
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

####### Fim das variáveis ########


nome_usuario = input("Para inicializar o atendimento, informe o seu nome: ")

print(f"\nBem vindo ao nosso sistema, {nome_usuario}!")

print(f"Agora escolha a opção que você deseja: ")

while True:
    opcao = input(menu).upper()


    if opcao == 'D':
        print("\nDepósito selecionado\n")

        quantia = float(input("Informe o valor que deseja depositar: R$"))
        
        if quantia > 0:
            print(depositar(quantia))
            
        else:
            print("Operação falhou. Valor informado é inválido")


    elif opcao == 'S':
        print("\nSaque selecionado")

        quantia = float(input("Informe a quantia que deseja sacar: R$"))
        if numero_saque == LIMITE_SAQUE:
            print("O diária de saque já foi atingida")
        
        elif quantia > limite:
            print("O seu limite por saque é R$500")
            
        elif quantia <= saldo and quantia <= limite:
            print(sacar(quantia))
        
        else:
            print("\nO seu saldo é insuficiente para esta operação!")
    

    elif opcao == 'E':
        print("\nExtrato selecionado")
        
        if numero_deposito >= 1:
            print(extrato())
        else:
            print("\nNão houve movimentação na conta!")
    

    elif opcao == 'Q':
        print("\nAtendimento encerrado. Obrigado por nos escolher, tenha um bom dia!")
        break


    else:
        print("Operação inválida")