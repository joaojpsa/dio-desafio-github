for x in range(10):
    print("numero", x);
    
#numeros primos com FOR
a = int(input("Digite o numero: "));
div = 0;
for _ in range(1, a+1):
    resto = a % _;
    if resto == 0:
        div += 1;
if div == 2:
    print("numero {} é primo". format(a));
else:
    print("numero {} não é primo". format(a));
#---------------------- FOR_FOR

b = int(input("Digite o numero: "));

for num in range(b):
    divisao = 0
    for j in range(1,num +1 ):
        rest = num % j;
        if rest == 0:
            divisao += 1;
    if divisao == 2:
        print(num);
#--while


cont= 0
somando = 0
while cont < 4:
    nota = int(input("Digite a nota: "));
    cont+= 1;
    somando += nota;
print("media: ", somando/cont);