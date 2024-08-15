#--------------------------------------------------
# Nome do Programa: Primeira_Tupla
# Descricao: Gerar uma Tupla
# Autor: Evando Chaves
# Data: Agosto 2024
#--------------------------------------------------

#criacao de tupla
primeira_tupla = (1, 2, 3, 4, "Ola, tupla")

print(primeira_tupla)

print(primeira_tupla.index(4))

#identifica elemento para busca na tupla
elemento_pesquisa = 3

if elemento_pesquisa in primeira_tupla:
    print(f"O elemento {elemento_pesquisa} esta na tupla.")
else:
    print(f"O elemento {elemento_pesquisa} nao esta na tupla.")

elemento_pesquisa = 33

if elemento_pesquisa in primeira_tupla:
    print(f"O elemento {elemento_pesquisa} esta na tupla.")
else:
    print(f"O elemento {elemento_pesquisa} nao esta na tupla.")
