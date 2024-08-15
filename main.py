#--------------------------------------------------
# Nome do Programa: main.py
# Descricao: Estruturacao das informacoes para informar alunos reprovados
# Autor: Evando Chaves
# Data: Agosto 2024
#--------------------------------------------------

from operacoes import calcular_media, verificar_status, alunos_reprovados

# Dados dos alunos
dados_alunos = [
    {'nome': 'Maria',   'matricula': 26, 'notas': [8, 7, 5, 9]},
    {'nome': 'Ana',     'matricula': 101,'notas': [9, 9, 8, 9]},
    {'nome': 'João',    'matricula': 13, 'notas': [6, 5, 5, 5]},
    {'nome': 'Agatha',  'matricula': 37, 'notas': [8, 6, 7.5, 9]},
    {'nome': 'Joaquim', 'matricula': 72, 'notas': [6, 5.5, 5, 7]},
    {'nome': 'Felix',   'matricula': 5,  'notas': [10, 8, 8, 8]},
]

# Lista para armazenar as matrículas dos alunos reprovados
matriculas_reprovadas = []

# Calcular a média e verificar se foi reprovado
for aluno in dados_alunos:
    media = calcular_media(aluno['notas'])
    aluno['media'] = media
    if verificar_status(media):
        matriculas_reprovadas.append(aluno['matricula'])

# Exibir os alunos reprovados
alunos_reprovados(dados_alunos, matriculas_reprovadas)