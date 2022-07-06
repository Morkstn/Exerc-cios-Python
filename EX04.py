#EXERCÍCIO NÚMERO 4

print("Olá seja bem vindo!")
nome = str(input("Digite seu nome: "))
print("Prazer {}".format(nome))
print("Um momento, carregando informações...")
print("Login")
hora = int(input("Informe para o sistema os minutos do horário atual: "))
resultado = 1
contador = 1

while contador <= hora:
    resultado = resultado * contador
    contador = contador + 1
    print("A sua senha para entrar no sistema será: LIBERDADE{:.0f}".format(resultado))
print("Fim do programa.")
