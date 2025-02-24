# A escola em que estamos construindo o nosso case de dados compartilhou os dados das notas de um estudante para que pudéssemos calcular a média deste em até uma casa decimal.
# Os dados recebidos correspondem a um dicionário com as chaves indicando o trimestre em questão e os valores das notas de cada trimestre do estudante em uma dada matéria.
# Notas do(a) estudante
notas = {'1º Trimestre': 8.5, '2º Trimestre': 7.5, '3º Trimestre': 9}
soma = sum(notas.values())
media_valor = round(soma/len(notas),1)

print(media_valor)

# Recebemos uma nova demanda, desta vez, de calcular a média de um estudante a partir de uma lista e retornar tanto a média quanto a situação do estudante ("Aprovado(a)" se a nota for maior ou igual a 6.0, caso contrário, será "Reprovado(a)").
# Além disso, precisamos exibir um pequeno texto em que indicamos a média do(a) estudante e qual a situação. Os dados recebidos correspondem a uma lista contendo apenas as notas de um estudante em uma dada matéria.
# Para facilitar o nosso entendimento do processo vamos aplicar as notas de apenas um estudante.

# Notas do(a) estudante
notas = [6.0, 7.0, 9.0, 5.0]

def media(lista: list=[0]) -> float:
    '''Função para calcular a médiade notas passadas por uma lista.
    
    Parameters
    ----------
    lista : list, default=0
    
    Returns
    -------
    tuple
        Tuple com (média dos valores, situação de aprovação)'''
    calculo = sum(lista)/len(lista)
    aprovacao = 'aprovado(a)' if calculo>=6 else 'reprovado(a)'
    print(f'O estudante está {aprovacao} com uma média de {calculo:.1f}.')
    return (calculo, aprovacao)

media(notas)

# função lambda:
# lambda <variavel>: <expressao>

# Comparando uma função de qualitativo no formato de função para função anônima
nota = float(input('Digite a nota do estudante: '))

def qualitativo (x):
    return x + 0.5
qualitativo(nota)

#Tentando a mesma função para uma função lambda
qualitativo = lambda x: x + 0.5
qualitativo(nota)

# Recebendo as notas e calculando a média ponderada
N1 = float(input("Digite a 1ª nota do(a) estudante: "))
N2 = float(input("Digite a 2ª nota do(a) estudante: "))
N3 = float(input("Digite a 3ª nota do(a) estudante: "))

media_ponderada = lambda x,y,z: (x*3 + y*2 + z*5)/10

media_estudante = media_ponderada(N1, N2, N3)
print(media_estudante)

# Recebemos mais uma demanda, desta vez, para criar uma pequena função que pudesse adicionar qualitativo (pontuação extra) às notas do trimestre dos estudantes da turma que ganhou a gincana de programação promovida pela escola. Cada estudante receberá o qualitativo de 0.5 acrescido à média.

# Os dados recebidos correspondem a uma lista contendo as notas de alguns estudantes e uma variável com o qualitativo recebido.

# Vamos resolver esse desafio?

# Para facilitar o nosso entendimento do processo vamos aplicar o qualitativo às notas de 5 estudantes, mas você pode testar outros casos para treinar.

# Notas do(a) estudante
notas = [6.0, 7.0, 9.0, 5.5, 8.0]
qualitativo = 0.5

# Não conseguimos aplicar o lambda em listas direto, é necessário utilizarmos junto a ela a função map
notas_atualizadas = map(lambda x: x+qualitativo, notas) # retorna um map
notas_atualizadas = list(notas_atualizadas)


print(notas_atualizadas)
