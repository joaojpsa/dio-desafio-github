#conjuntos
conjunto = {1, 2, 3, 4, 3, 2};
print(type(conjunto), conjunto);
print("--------------");

conjunto.add(5);
print("ADD numero", conjunto);
print("--------------");

conjunto.discard(2);
print("remove numero", conjunto);
conjunto.add(2);
print("--------------");
#-----------------UNIÂO----------------
conjunto2 = {5, 6, 7, 8};
unirConjuntos = conjunto.union(conjunto2)
print(unirConjuntos);
print("--------------");
#----------------INTERSECÇÂO----------
interseccaoConjuntos = conjunto.intersection(conjunto2);
print(interseccaoConjuntos);
print("--------------");
#----------------DIFERENÇA-----------
diferencaConjuntos = conjunto.difference(conjunto2);
print(diferencaConjuntos);
diferencaConjuntos2 = conjunto2.difference(conjunto);
print(diferencaConjuntos2);
print("--------------");
#----------------DIFERENÇA SIMÉTRICA-----------
difSimetricaConjuntos = conjunto.symmetric_difference(conjunto2);
print(difSimetricaConjuntos);
print("--------------");

#-------------SUB_SET(conjuntos)----------
conjuntoA = {1, 2, 3};
conjuntoB = {1, 2, 3, 4, 5};
subConjunto1 = conjuntoA.issubset(conjuntoB);
print(subConjunto1);
subConjunto2 = conjuntoB.issubset(conjuntoA);
print(subConjunto2);
print("--------------");
superConjunto1 = conjuntoA.issuperset(conjuntoB);
print(superConjunto1);
superConjunto2 = conjuntoB.issuperset(conjuntoA);
print(superConjunto2);

print("--------------");
lista = ["gato", "cachorro", "leao"];
print(type(lista), lista);
conj_animais = set(lista);
print(type(conj_animais), conj_animais);
