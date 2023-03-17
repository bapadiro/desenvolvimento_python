#Exercicio 8 lista3
idade = int(input("Digite a idade do nadador: "))
categoria = "Sem categoria"

if idade >= 5 and idade <= 7:
    categoria = "Infantil"
elif idade >= 8 and idade <= 10:
    categoria = "Juvenil"
elif idade >= 11 and idade <= 15:
    categoria = "Adolescente"
elif idade >= 16 and idade <= 30:
    categoria = "Adulto"
elif idade > 30:
    categoria = "Senior"

print(categoria)                