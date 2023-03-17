diasUteis = int(input("dias úteis: "))
horasTrab = int(input("horas trabalhadas: "))
valorHora = float(input("valor hora: "))

jornadaMensal = diasUteis * 8

if jornadaMensal >= horasTrab:
    salarioMensal = horasTrab * valorHora
else:
    print("calcular horas-extras")
    #ainda falta completar com o calculo do salario e das horas extras
    salarioMensal = 0.0

print("salario foi de ", salarioMensal)