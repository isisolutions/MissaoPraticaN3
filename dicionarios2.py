#--------------------------------------------------
# Nome do Programa: Primeiro_Dicionario
# Descricao: Gerar um Dicionario
# Autor: Evando Chaves
# Data: Agosto 2024
#--------------------------------------------------

#criar dicionario
meu_dicionario = {1:{'nome': 'Maria', 'idade': 26, 'nacionalidade':'brasileira'}}

#Utilizando o metodo update()
meu_dicionario.update({
    2:{'nome': 'Evando', 'idade': 45, 'nacionalidade':'brasileira'},
    3:{'nome': 'Veridiana', 'idade':35, 'nacionalidade': 'italiana'}
})

print(meu_dicionario)

#utilizando o metodo copy()
dicionario_copia = meu_dicionario.copy()

#Utilizandi o metodo pop()
meu_dicionario.pop(2)
print(meu_dicionario)

#Utilizandio o metodo popitem()
meu_dicionario.popitem()
print(meu_dicionario)

#Utilizando o metodo clear()
meu_dicionario.clear
dicionario_copia.clear

#Utilizando o metodo fromkeys()
chaves = ['x', 'y', 'z']
valor  = 0

novo_dicionario = dict.fromkeys(chaves,valor)

print(f'Itens do novo_dicionario: {list(novo_dicionario.items())}')
print(f'Chaves do novo_dicionario: {list(novo_dicionario.keys())}')
print(f'Valores do novo_dicionario: {list(novo_dicionario.values())}')

