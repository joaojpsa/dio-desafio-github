a = int(input("Digite o numero: "));
b = int(input("Digite o numero: "));
c = int(input("Digite o numero: "));

print("media: ", (a+b+c)/3);
if a > b and a > c:
    print("O maior é: ", a);
elif b > a and b > c:
    print("O maior é: ", b);
else:
    print("O maior é: ", c);

if a % 2 == 0:
    print("O numero é par");
else:
    print("O numero é impar");