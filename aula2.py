primeiro_Nome = input(" Digite seu primeiro nome:  ")
sobrenome = input("Digite seu sobrenome:  ")
print("nome completo: " +primeiro_Nome  +  sobrenome)
print("-------------------------------------------------")
print(f"{primeiro_Nome} vamos fazer uma soma?")
numero1 = float(input(" digite o primeiro numero da sua soma:  "))
numero2 = float(input( "digite o segundo numero da sua soma:  "))
soma = numero1+numero2
print (" o resultado da soma é: ")
print(soma)
print("----------------------------------------------------")
print(f"{primeiro_Nome} Vamos fazer uma media calculada de 3 notas:  ")
nota1 = float(input("Digite sua primeira nota:  "))
nota2 = float(input("Digite sua segunda nota:  "))
nota3 = float(input("Digite sua terceira nota:  "))
media = (nota1 + nota2 + nota3)/3
print(" a sua media é: " )
print(media)
print("------------------------------------------------------")
print(f"{primeiro_Nome} vamos calcular a area de um retangulo")
altura = float(input("Digite a aultura do retangulo: "))
largura = float(input(" Digite a largura do retangulo: "))
area = (altura * largura)
print("a area do seu retangulo é: " )
print(area)




