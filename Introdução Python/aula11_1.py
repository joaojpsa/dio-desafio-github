from logging import exception


class Error(exception):
    pass

class InputError(Error):
    def __init__(self, message):
        self.message = message

while True:
    try:
        x = int(input("Entre com uma nota de 0 a 10:"));
        print(x);
        if x > 10:
            raise InputError("Nota não  pode ser maior que 10!!") # forçar uma sessão
        elif x < 10:
            raise InputError("Nota nõa pode ser menor que 0!!");
        break
    except ValueError:
        print("Valor invalido: deve-se digitar somente numeros!");

    except InputError as ex:
        print(ex);
    
