#--------------------------------------------------
# Nome do Programa: Primeiro_Dicionario
# Descricao: Gerar um Dicionario
# Autor: Evando Chaves
# Data: Agosto 2024
#--------------------------------------------------

#criar dicionario
meu_dicionario = {
    1: 'python',
    2: 'Java',
    3: 'PHP'
}
#Imprime conteudo do dicionario
print("Conteudo do Dicionario: ", meu_dicionario)

#Imprime o tipo do dicionario
print("Tipo do dicionario:", type(meu_dicionario))

#Imprime o 
print("Valor da chave 'linguagem':", meu_dicionario.get('linguagem'))

dicionario_frutas = dict({
    1: {'nome': 'limao', 'tipo': 'ácida'},
    2: {'nome': 'laranja','tipo': 'ácida'},
    3: {'nome': 'manga','tipo': 'semiácida'},
    4: {'nome': 'maçã', 'tipo': 'semiácida'},
    5: {'nome': 'banana', 'tipo': 'doce'},
    6: {'nome': 'mamão', 'tipo': 'doce'},
})

#Imprime valor das chaves "nome" e "tipo" da chave 1
print("chave 1 - Nome:", dicionario_frutas[1]['nome'], 
      "tipo:", dicionario_frutas[1]['tipo'])

#Imprime valor das chaves "nome" e "tipo" da chave 2
print("chave 2 - Nome:", dicionario_frutas[2]['nome'], 
      "tipo:", dicionario_frutas[2]['tipo'])

#imprime valor de todas as chaves
for chave, valor in dicionario_frutas.items():
    print(f"Chave {chave} - Nome: {valor['nome']}, Tipo:{valor['tipo']}")