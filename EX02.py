#EXERCÍCIO 2

print ("SEJA BEM VINDO")
seg = int(input("Digite o número de votos dos alunos que preferem na segunda-feira para a realização das lives: "))
ter = int(input("Digite o número de votos dos alunos que preferem na terça-feira para a realização das lives: "))
qua = int(input("Digite o número de votos dos alunos que preferem na quarta-feira para a realização das lives: "))
qui = int(input("Digite o número de votos dos alunos que preferem na quinta-feira para a realização das lives: "))
sex = int(input("Digite o número de votos dos alunos que preferem na sexta-feira para a realização das lives: "))
total_votos = seg + ter + qua + qui + sex

maior_que = seg
if ter > maior_que:
    maior_que = ter
    if qua > maior_que:
        maior_que = qua
        if qui > maior_que:
            maior_que = qui
            if sex > maior_que:
                maior_que = sex

dia = ""

if maior_que == seg:
    dia = "Segunda-feira"
if maior_que == ter:
    dia = "Terça-feira"
if maior_que == qua:
    dia = "Quarta-feira"
if maior_que == qui:
    dia = "Quinta-feira"
if maior_que == sex:
    dia = "Sexta-feira"

print("Dia com mais votos: {}".format(maior_que ))
print("Total de votos {} que participaram da votação".format(total_votos))
print("FIM.")
