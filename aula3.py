from random import randint
from my_methods import media
# Recebemos a demanda de transformar uma lista com o nome e as notas dos três trimestres de estudantes em uma lista simples com os nomes separados das notas e uma lista de listas com as três notas de cada estudante separadas umas das outras. Os dados recebidos correspondem a uma lista com os nomes e as respectivas notas de cada estudante.

# Para facilitar o nosso entendimento do processo vamos trabalhar com uma turma fictícia de 5 estudantes.
notas_turma = ['João', 8.0, 9.0, 10.0, 'Maria', 9.0, 7.0, 6.0, 'José', 3.4, 7.0, 7.0, 'Cláudia', 5.5, 6.6, 8.0, 'Ana', 6.0, 10.0, 9.5]

nomes = []
notas_juntas = []

# nomes estao posicoes multiplas de 4
for i in range(len(notas_turma)):
    if i%4==0:
        nomes.append(notas_turma[i])
    else:
        notas_juntas.append(notas_turma[i])

# criando a lista de listas
notas = []
for i in range(0, len(notas_juntas), 3):
    notas.append([notas_juntas[i], notas_juntas[i+1], notas_juntas[i+2]]) # lista com as notas do aluno

print(notas)
print()



# tuplas: estruturas de dados para armazenas valores, imutável

# Nesta nova demanda, precisamos gerar uma lista de tuplas com os nomes dos estudantes e o código ID de cada um para a plataforma de análise dos dados. A criação do código consiste em concatenar a primeira letra do nome do estudante a um número aleatório de 0 a 999. Os dados recebidos correspondem a uma lista dos nomes de cada estudante.

# Para facilitar o nosso entendimento do processo vamos trabalhar com uma turma fictícia de 5 estudantes.
estudantes = ['João', 'Maria', 'José', 'Cláudia', 'Ana']
# podemos iterar por uma string como iteramos por uma lista (estudantes[0][1], por exemplo, é J)

def gera_codigo():
    return (str(randint(0,999)))

codigo_estudantes = []

for i in range(len(estudantes)):
    codigo_estudantes.append((estudantes[i], estudantes[i][0] + gera_codigo()))

print(codigo_estudantes)
print()



# list comprehension: outra maneira de fazer lista
# formato básico: [expression for item in lista if condicao], ou [resultado_if if condicao else resultado_else for item in lista]

# Recebemos a demanda de criar uma lista com as médias dos estudantes da lista de listas que criamos acima. Lembrando que cada lista da lista de listas possui as três notas de cada estudante.
medias = [round(media(nota),1) for nota in notas]
print(medias)
print()

# Agora, precisamos utilizar as médias calculadas no exemplo anterior, pareando com o nome dos estudantes. Isto será necessário para gerar uma lista que selecione aqueles estudantes que possuam uma média final maior ou igual a 8 para concorrer a uma bolsa para o próximo ano letivo. Os dados recebidos correspondem a uma lista de tuplas com os nomes e códigos dos estudantes e a lista de médias calculadas logo acima.

# extraindo nomes da tupla:
nomes = [nome_codigo[0] for nome_codigo in codigo_estudantes]
print(nomes)

# pareando nomes com medias com zip()
nomes_medias = list(zip(nomes, medias))
print(nomes_medias)

candidatos = [estudante[0] for estudante in nomes_medias if estudante[1]>=8]
print(candidatos)
print()

# Recebemos duas demandas a respeito desse projeto com as notas dos estudantes:
# - Criar uma lista da situação dos estudantes em que caso se sua média seja maior ou igual a 6 receberá o valor "Aprovado" e caso contrário receberá o valor "Reprovado".
# - Gerar uma lista de listas com:
#   - Lista de tuplas com o nome dos estudantes e seus códigos
#   - Lista de listas com as notas de cada estudante
#   - Lista com as médias de cada estudante
#   - Lista da situação dos estudantes de acordo com as médias

# Os dados que utilizaremos são os mesmos que geramos nas situações anteriores (`nomes`, `notas`, `medias`).

situacao = ['Aprovado' if media>=6 else 'Reprovado' for media in medias]
print(situacao)
lista_completa = [codigo_estudantes, notas, medias, situacao]



# dict comprehension
# formato: {chave: valor for item in lista}

# Agora, a nossa demanda consiste em gerar um dicionário a partir da lista de listas que criamos acima, para passar para a pessoa responsável por construir as tabelas para a análise dos dados.
# - As chaves do nosso dicionário serão as colunas identificando o tipo de dado
# - Os valores serão as listas com os dados correspondentes àquela chave.

# Colunas com os tipos dos dados (exceto nome)
coluna = ['Notas', 'Média Final', 'Situação']
cadastro = {coluna[i]: lista_completa[i+1] for i in range(len(coluna))} 
# Vamos por fim adicionar o nome dos estudantes, extraindo apenas seus nomes da lista de tuplas
cadastro['Estudante'] = [lista_completa[0][i][0] for i in range(len(lista_completa[0]))]

print(cadastro)