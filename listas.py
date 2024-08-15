#--------------------------------------------------
# Nome do Programa: Lista Mesclada
# Descricao: Gerar uma lista mesclada
# Autor: Evando Chaves
# Data: Agosto 2024
#--------------------------------------------------

# Criar uma lista sem elementos
lista_mesclada=[1, 2, 3, "Ola, Python", True, 12.6]

print(lista_mesclada)

#adicionar um elemento a lista
lista_mesclada.append("Lista aninhada")

print(lista_mesclada)

#inserir na posicao 4 o elemento
lista_mesclada.insert(4,5)

print(lista_mesclada)

#tamanho da lista
tamanho = len(lista_mesclada)

print(f"O tamanho da lista eh: {tamanho}")

#remover elemento na posicao 1 da lista
lista_mesclada.pop(1) 

print(lista_mesclada)

#Criar uma nova lista 
nova_lista_mesclada = lista_mesclada[0:4]

print(nova_lista_mesclada)