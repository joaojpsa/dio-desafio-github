#LAMBDA

contador_letra = lambda lista: [len(x) for x in lista]

lista_fruta = ["pera", "uva", "banana"]
print(contador_letra(lista_fruta));

print("---------------");

soma = lambda a, b: a + b;
print(soma(4, 98));

print("---------------");

calculadora = {
    "soma": lambda a, b: a + b,
    "subtrai": lambda a, b: a - b,
    "multiplica": lambda a, b: a * b,
    "divide": lambda a, b: a / b,
}
print(type(calculadora));
soma = calculadora["soma"];
print(soma(29, 1));