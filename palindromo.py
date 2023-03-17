num = int(input("Digite num: "))
numOriginal = num
ac = 0

while num != 0:
    a = num % 10 
    num = num // 10
    ac = ac * 10 + a

if numOriginal == ac:
    print("é palíndrome")
else:
    print("não é palíndrome")

