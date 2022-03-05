lista_num = [1, 32, 3, 7];
lista_fruta = ["pera", "maça", "banana", "caju"];

print(lista_fruta, lista_num);
print(lista_fruta[2]);

soma = 0;
for x in lista_num:
    soma +=x
    print("Teste: ", x, soma);

#--------------- operação usando função
print(sum(lista_num));
print(max(lista_num));
print(min(lista_num));

#-------------verifcar lista

if "uva" in lista_fruta:
    print("existe na lista");
else:
    print("nao existe na lista");
    lista_fruta.append("uva");
    print(lista_fruta)

lista_fruta.pop(1);
print(lista_fruta);
lista_fruta.remove("uva");
print(lista_fruta);
#-------------
nova_lista_fruta = lista_fruta * 2;
print(nova_lista_fruta);

#-------------ordenar
lista_fruta.sort();
lista_num.sort();
print(lista_fruta, lista_num);
lista_fruta.reverse();
print(lista_fruta);

#-------------TUPLA imutavel
tupla = {1, 3, 2, 5, 54};
print(tupla);
print(len(tupla));
tupla_fruta = tuple(lista_fruta);
print(type(tupla_fruta));