#metodos, funçoes e classes

def soma(a, b):
    return a + b;
def subtrai(a, b):
    return a - b;

print(subtrai(3, 1));
print(soma(4,3));
print("--------------")

class Calculadora:
    def __init__(self, num1, num2):
        self.valor_a = num1;
        self.valor_b = num2;

    def soma(self):
        return self.valor_a + self.valor_b;

    def subtrai(self):
        return self.valor_a - self.valor_b;

    def multiplica(self):
        return self.valor_a * self.valor_b;

    def divisao(self):
        return self.valor_a / self.valor_b;

calculadora = Calculadora(10, 3);
print(calculadora.soma());
print(calculadora.subtrai());
print(calculadora.multiplica());
print(calculadora.divisao());

