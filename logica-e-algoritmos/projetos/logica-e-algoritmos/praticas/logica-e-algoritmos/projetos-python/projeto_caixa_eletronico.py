############## PROJETO SIMULADOR DE CAIXA ELETRÔNICO ##############
print("###### BEM VINDO AO PYTHON BANK ######")
print("MENU DE OPÇÕES:")

saldo=float(1000)
operacoes=[]
total_depositos=0
total_saques=0
opcao=0

#--------------------ENTRADA e TRATAMENTO DE DADOS--------------------#

for transacao in range(5):
    print("1 - Verificar saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Sair / Encerrar")
    opcaoSelecionada = int(input("Digite o número da opção correspondente: "))
    if opcaoSelecionada == 1: #### CONDICIONAL SALDO
        print(f"Seu saldo é: R${saldo}") 
        operacoes.append("Verificou saldo") 
    elif opcaoSelecionada == 2: #### CONDICIONAL DEPÓSITO
        deposito=float(input("Insira o valor a ser depositado: "))
        saldo += deposito #### ADICIONA VALOR DO DEPÓSITO AO SALDO
        total_depositos += 1 #### CONTADOR DE DEPÓSITOS
        print("Depósito efetuado com sucesso!")
        operacoes.append("Realizou depósito")
    elif opcaoSelecionada == 3: #### CONDICIONAL SAQUE
        saque=float(input("Insira o valor a ser sacado: "))
        if saque <= saldo:
            saldo -= saque #### SUBTRAI VALOR DO SAQUE AO SALDO
            total_saques += 1 #### CONTADOR DE SAQUES
            print("Saque realizado com sucesso!")
            operacoes.append("Realizou saque")
        else:
            print("Saldo insuficiente!")    
    elif opcaoSelecionada == 4: #### CONDICIONAL ENCERRAR
        print("Operação encerrada")
        break
    else:
        print("Opção inválida")

#--------------------RELATÓRIOS E SAÍDAS--------------------#

print("###### EXTRATO BANCÁRIO ######")
print(f"Total de operações: {len(operacoes)}")
print(f"Total de depósitos: {total_depositos}")
print(f"Total de saques: {total_saques}")
print(f"Saldo final: R${saldo:.2f}")
print("###### HISTÓRICO DE MOVIMENTAÇÕES ######")
for operacao in operacoes:
    print(f"- {operacao}")