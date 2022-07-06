#EXECÍCIO NÚMERO 3

imp = 0
par = 0
cont_imp = 0
cont_par = 0
nome = input("Olá, digite seu nome: ")
print("Olá {}, seja bem vindo!".format(nome))
print("ATENÇÃO!")
print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS ÍMPARES. ")
for i in range(1,50 + 1,2):
    cont_imp = cont_imp + 1
    nota = int(input("Por favor, digite a nota do aluno {}: ".format(i)))
    while nota < 0 or nota > 10:
        print("ATENÇÃO!")
        print("NOTA DIGITADA INVÁLIDA... TENTE NOVAMENTE!")
        nota = int(input("Por favor, digite a nota do aluno {}: ".format(i)))
    imp = imp + nota

print("ATENÇÃO!")
print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES. ")
for i in range(0,49 + 1,2):
    cont_par = cont_par + 1
    nota = int(input("Por favor, digite a nota do aluno {}: ".format(i)))
    while nota < 0 or nota > 10:
        print("ATENÇÃO!")
        print("NOTA DIGITADA INVÁLIDA... TENTE NOVAMENTE!")
        nota = int(input("Por favor, digite a nota do aluno {}: ".format(i)))
    par = par + nota

media_Imp = imp/cont_imp
media_Par = par/cont_par
print("Os alunos de números ímpares tiveram uma média {:.0f}".format(media_Imp))
print("Os alunos de números pares tiveram uma média {:.0f}".format(media_Par))
print("FIM.")
