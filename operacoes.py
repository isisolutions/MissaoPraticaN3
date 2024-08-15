#--------------------------------------------------
# Nome do Programa: operacoes.py
# Descricao: Metodos de controle
# Autor: Evando Chaves
# Data: Agosto 2024
#--------------------------------------------------

#Metodo para calcular a media dos bimestres
def calcular_media(notas):
    return sum(notas) / len(notas)

#Metodo para verificar se o aluno foi reprovado
def verificar_status(media):
    return media < 6

#Metodo para exibir os dados dos alunos reprovados
def alunos_reprovados(dados_alunos, matriculas_reprovadas):
    for aluno in dados_alunos:
        if aluno['matricula'] in matriculas_reprovadas:
            print(f"Aluno Reprovado: {aluno['nome']} - Matricula: {aluno['matricula']} - Media Final: {aluno['media']}")

