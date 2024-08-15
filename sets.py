#--------------------------------------------------
# Nome do Programa: Primeiro_Set
# Descricao: Gerar um Set
# Autor: Evando Chaves
# Data: Agosto 2024
#--------------------------------------------------

#criar um set inicial
set_inicial = {11, 12, 13, 14}
print(set_inicial)

#adicionar elemento ao set
set_inicial.add(15)
print(set_inicial)

#update elementos ao set
set_inicial.update({1, 2, 3, 4, 5})
print(set_inicial)

#remover elemento do set
set_inicial.remove(13)
print(set_inicial)

#criar novo set
novo_set = {20, 21, 23, 1, 2}
print(novo_set)

#imprimir o resultado da uniao entre os dois 
uniao = set_inicial | novo_set
print(f"A Uniao dos dois sets eh: {uniao}")

#imprimir o resultado da interseccao entre os dois sets
interseccao = set_inicial & novo_set
print(f"A Interseccao dos dois sets eh: {interseccao}")

#Imprimir o resultado da diferenca entre os dois sets
diferenca = set_inicial - novo_set
print(f"A diferenca entre os set eh: {diferenca}")

#Imprimir o resultado da diferenca simetrica entre dois sets
d_simetrica = set_inicial ^ novo_set
print(f"A diferenca simentrica entre os sets eh: ", d_simetrica)