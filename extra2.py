from my_methods import requesitar_lista, formatar_lista
# Aquecimento
# 1. Escreva um código que lê a lista abaixo e faça:
lista = [16, 14, 63, 65, 17, 99, 70, 11, 20, 48, 79, 32, 17, 89, 12, 25, 66]
# A leitura do tamanho da lista
tam = len(lista)
# A leitura do maior e menor valor
maior = max(lista)
menor = min(lista)
# A soma dos valores da lista
soma = sum(lista)
# Ao final exiba uma mensagem dizendo:
print(f"A lista possui {tam} números em que o maior número é {maior} e o menor número é {menor}. A soma dos valores presentes nela é igual a {soma}.\n") 

# 3. Crie a função que leia a lista abaixo e retorne uma nova lista com os múltiplos de 3:
lista = [97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]
def multiplicar_lista (lista : list=[], num : int=1) -> list:
    nova_lista = []
    for i in lista:
        nova_lista.append(i*num)
    return nova_lista
# Utilize o return na função e salve a nova lista na variável mult_3.
mult_3 = multiplicar_lista(lista, 3)
print(mult_3)
print()

# 4. Crie uma lista dos quadrados dos números da seguinte lista [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. Lembre-se de utilizar as funções lambda e map() para calcular o quadrado de cada elemento da lista.
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_quadrados = list(map(lambda x : pow(x,2), lista))
print(lista_quadrados)
print()

# Aplicando a projetos
# 5. Você foi contratado(a) como cientista de dados de uma associação de skate. Para analisar as notas recebidas de skatistas em algumas competições ao longo do ano, você precisa criar um código que calcula a pontuação dos(as) atletas. Para isso, o seu código deve receber 5 notas digitadas pelas pessoas juradas.
# Para calcular a pontuação de um(a) skatista, você precisa eliminar a maior e a menor pontuação dentre as 5 notas e tirar a média das 3 notas que sobraram. Retorne a média para apresentar o texto:
# "Nota da manobra: [media]"
notas = requesitar_lista('Digite as 5 notas dos jurados', 5)
notas = formatar_lista(notas)

notas.remove(min(notas))
notas.remove(max(notas))

media = sum(notas)/len(notas)
print(f'Nota da manobra: {media:.1f}.\n')


# 6. Para atender a uma demanda de uma instituição de ensino para a análise do desempenho de seus(suas) estudantes, você precisa criar uma função que receba uma lista de 4 notas e retorne:
#     maior nota
#     menor nota
#     média
#     situação (Aprovado(a) ou Reprovado(a))
# Para testar o comportamento da função, os dados podem ser exibidos em um texto:
# "O(a) estudante obteve uma média de [media], com a sua maior nota de [maior] pontos e a menor nota de [menor] pontos e foi [situacao]"
notas = requesitar_lista('Digite as 4 notas do estudante', 4)
notas = formatar_lista(notas)


def cadastro (notas : list=[]):
    nota_max = max(notas)
    nota_min = min(notas)
    media = sum(notas)/len(notas)
    situacao = 'aprovado(a)' if media>=6 else 'reprovado(a)'
    return nota_max, nota_min, media, situacao
maior, menor, media, situacao = cadastro(notas)
print(f'O(a) estudante obteve uma média de {media:.1f}, com a sua maior nota de {maior} pontos e a menor nota de {menor} pontos, e foi {situacao}.\n')


# 7. Você recebeu uma demanda para tratar 2 listas com os nomes e sobrenomes de cada estudante concatenando-as para apresentar seus nomes completos na forma Nome Sobrenome. As listas são:
nomes = ["joão", "MaRia", "JOSÉ"]
sobrenomes = ["SILVA", "souza", "Tavares"]
# O texto exibido ao fim deve ser parecido com:
# "Nome completo: Ana Silva"
# Dica: utilize a função map para mapear os nomes e sobrenomes e as funções de string para tratar o texto.
nome_completo = map(lambda nome, sobrenome: f'{nome.title()} {sobrenome.title()}', nomes, sobrenomes)

for nome in nome_completo:
    print(f'Nome completo: {nome}')

# 8. Como cientista de dados em um time de futebol, você precisa implementar novas formas de coleta de dados sobre o desempenho de jogadores e do time como um todo. Sua primeira ação é criar uma forma de calcular a pontuação do time no campeonato nacional a partir dos dados de gols marcados e sofridos em cada jogo.
# Escreva uma função chamada calcula_pontos que recebe como parâmetros duas listas de números inteiros, representando os gols marcados e sofridos pelo time em cada partida do campeonato. A função deve retornar a pontuação do time e o aproveitamento em percentual, levando em consideração que a vitória vale 3 pontos, o empate vale 1 ponto e a derrota 0 pontos.
#     Observação: se a quantidade de gols marcados numa partida for maior que a de sofridos, o time venceu. Caso seja igual, o time empatou e se for menor, o time perdeu. Para calcular o aproveitamento devemos fazer a razão entre a pontuação do time pela pontuação máxima que ele poderia receber.
# Para teste, utilize as seguintes listas de gols marcados e sofridos:

gols_marcados = [2, 1, 3, 1, 0]
gols_sofridos = [1, 2, 2, 1, 3]

def calcula_pontos(marcados : list=[],sofridos : list =[]) -> tuple[str, str]:
    pontuacao = 0
    aproveitamento = 0
    for (marcados, sofridos) in zip(gols_marcados, gols_sofridos):
        if marcados > sofridos:
            pontuacao+=3
        elif marcados == sofridos:
            pontuacao+=1
    aproveitamento = pontuacao/(3*len(gols_marcados))*100

    return pontuacao, aproveitamento

pontos, aprov = calcula_pontos(gols_marcados, gols_sofridos)

print(f'\nA pontuação do time foi de {pontos} e seu aproveitamento foi de {aprov:.2f}%')


# 9. Você recebeu o desafio de criar um código que calcula os gastos de uma viagem para um das quatro cidades partindo de Recife, sendo elas: Salvador, Fortaleza, Natal e Aracaju.
# O custo da diária do hotel é de 150 reais em todas elas e o consumo de gasolina na viagem de carro é de 14 km/l, sendo que o valor da gasolina é de 5 reais o litro. O gastos com passeios e alimentação a se fazer em cada uma delas por dia seria de [200, 400, 250, 300], respectivamente.
# Sabendo que as distâncias entre Recife e cada uma das cidades é de aproximadamente [850, 800, 300, 550] km, crie três funções nas quais: a 1ª função calcule os gastos com hotel (gasto_hotel), a 2ª calcule os gastos com a gasolina (gasto_gasolina) e a 3ª os gastos com passeio e alimentação (gasto_passeio).
# Para testar, simule uma viagem de 3 dias para Salvador partindo de Recife. Considere a viagem de ida e volta de carro.
km_l = 14 # a cada litro se anda 14 km
custo_l = 5 # a cada litro se gasta 5 reais

cidades = {
    'Salvador': {'gastos':200, 'distancia': 850},
    'Fortaleza':  {'gastos':400, 'distancia': 800},
    'Natal':  {'gastos':250, 'distancia': 300},
    'Aracaju':  {'gastos':300, 'distancia': 550}
}

def calcular_hotel(dias : int=2) -> float:
    return 150*dias

def calcular_gasolina(cidade : str='Salvador') -> float:
    return (cidades[cidade]['distancia']/km_l)*custo_l*2

def calcular_gastos(cidade : str='Salvador', dias : int=2) -> float:
    return cidades[cidade]['gastos']*dias

def calcular_total(cidade : str='Salvador', dias : int=2) -> tuple:
    return calcular_hotel(dias) + calcular_gasolina(cidade) + calcular_gastos(cidade,dias)

dias = int(input("Quantas diárias? "))
cidade = input("Qual a cidade? [Salvador, Fortaleza, Natal ou Aracaju]: ")
gastos = calcular_total(cidade,dias)

txt = f'Com base nos gastos definidos, uma viagem de {dias} dias para {cidade} saindo de Recife custaria {gastos:.2f} reais.'
print(txt)

# 10. Você iniciou um estágio em uma empresa que trabalha com processamento de linguagem natural (NLP). Sua líder requisitou que você criasse um trecho de código que recebe uma frase digitada pela pessoa usuária e filtre apenas as palavras com tamanho maior ou igual a 5, exibindo-as em uma lista. Essa demanda é voltada para a análise do padrão de comportamento de pessoas na escrita de palavras acima dessa quantidade de caracteres.

#     Dica: utilize as funções lambda e filter() para filtrar essas palavras. Lembrando que a função embutida filter() recebe uma função (no nosso exemplo uma função lambda) e filtra um iterável de acordo com a função. Para tratar a frase use replace() para trocar a ',' '.', '!' e '?' por espaço.

# Use a frase "Aprender Python aqui na Alura é muito bom" para testar o código.
frase = input('Digite uma frase: ')
frase = frase.replace(',',' ').replace('.',' ').replace('!',' ').replace('?',' ').split()

tamanho = list(filter(lambda x: len(x)>=5, frase))
print(tamanho)
