acumulador = 0

num = int(input("Digite numero: "))

while num != 0:
    if num % 2 == 0:
        acumulador = acumulador + num
    
    num = int(input("Digite numero: "))

print("Resultado: ", acumulador)    