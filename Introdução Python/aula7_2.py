class Calculadora:
    def __init__(self):
        pass

    def soma(self, valor_a, valor_b):
        return valor_a + valor_b;

    def subtrai(self, valor_a, valor_b):
        return valor_a - valor_b;

    def multiplica(self, valor_a, valor_b):
        return valor_a * valor_b;

    def divisao(self, valor_a, valor_b):
        return valor_a / valor_b;

calculadora = Calculadora();
print(calculadora.soma(10, 2));
print(calculadora.subtrai(12, 1));
print(calculadora.multiplica(2,3));
print(calculadora.divisao(18, 3));

