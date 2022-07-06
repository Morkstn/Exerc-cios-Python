#EXERCÍCIO NÚMERO 1

n1 = float(input("O tipo de assinatura é Basic (30%)? Digite 30 se for sim 0 para não. "))
if n1 == n1:
    if n1 == 30:
        faturamento = float(input("Qual foi o faturamento anual R$? "))
        valor = faturamento - n1 * 10
        print("O valor a pagar para a empresa R${:.3f}".format(valor))
n2 = float(input("O tipo de assinatura é Basic (20%)? Digite 20 se for sim 0 para não. "))
if n2 == n2:
    if n2 == 20:
        faturamento = float(input("Qual foi o faturamento anual R$? "))
        valor = faturamento - n2 * 10
        print("O valor a pagar para a empresa é R${:.3f}".format(valor))
n3 = float(input("O tipo de assinatura é Basic (10%)? Digite 10 se for sim 0 para não. "))
if n3 == n3:
    if n3 == 10:
       faturamento = float(input("Qual foi o faturamento anual R$? "))
       valor = faturamento - n3 * 10
       print("O valor a pagar a empresa é R${:.3f}".format(valor))
n4 = float(input("O tipo de assinatura é Basic (5%)? Digite 5 se for sim 0 para não. "))
if n4 == n4:
    if n4 == 5:
        faturamento = float(input("Qual foi o faturamento anual R$? "))
        valor = faturamento - n4 * 10
        print("O valor a pagar para a empresa é R${:.3f}".format(valor))
print("Fim.")
