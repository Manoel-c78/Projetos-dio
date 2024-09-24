Menu = """

[1] Saque
[2] Depósito
[3] Extrato
[4] Sair

-> """

saldo = 100
extrato = ""
saque_diario = 3
deposito_diario = 0
limite_deposito = 3

while True:
    
    opcao = input(Menu)
    
    if opcao == "1":
            valor = float(input("Qual valor você deseja sacar?  "))
            if valor <= saldo:
                saldo -= valor
                extrato += f"Saque: R${valor}\n"
                saque_diario += 1
                print(f"Saldo: R${saldo:.2f}")

            elif valor >= saldo:
                 print("Saldo insuficiente!")    

    if opcao == "2":
            if deposito_diario < limite_deposito:
                valor = float(input("Qual valor você deseja depositar?  "))        
                saldo += valor
                extrato += f"Deposito: R${valor}\n"
                deposito_diario += 1
                print(f"Saldo:  R${saldo:.2f} Depósito realizado com sucesso")
                print(f"Depósitos Restantes: {deposito_diario} de {limite_deposito}")  

            elif limite_deposito:
                print("Depósito diário excedido!")

    if opcao == "3":
         print(f"Saldo: R${saldo:.2f}\n Extrato:\n{extrato}")

    if opcao == "4":
         print("Saindo do sistema...")
         break