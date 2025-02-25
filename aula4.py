# Você criou um código que lê um dicionário com as notas dos estudantes e quis retornar a lista de notas de um estudante.
# Caso o(a) estudante não esteja matriculado(a) na turma devemos tratar a exceção para aparecer a mensagem "Estudante não matriculado(a) na turma".
# Vamos trabalhar nesse exemplo com a exceção **Key Error** que interromperá o processo desse pedaço do código.

notas = {'João': [8.0, 9.0, 10.0], 'Maria': [9.0, 7.0, 6.0], 'José': [3.4, 7.0, 8.0], 'Cláudia': [5.5, 6.6, 8.0],
 'Ana': [6.0, 10.0, 9.5], 'Joaquim': [5.5, 7.5, 9.0], 'Júlia': [6.0, 8.0, 7.0], 'Pedro': [3.0, 4.0, 6.0]}
nome = input('Digite o nome do(a) estudante: ')

try:
    resultado = notas[nome.title()]
    print(resultado)
except KeyError:
    print('Estudante não matriculado na turma.')
print()


# Você criou um código que lê um dicionário com as notas dos estudantes e quis retornar a lista de notas de um estudante.
# Caso o(a) estudante não esteja matriculado(a) na classe devemos tratar a exceção para aparecer a mensagem "Estudante não matriculado(a) na turma" e se a exceção não for lançada devemos exibir a lista com as notas do(a) estudante.
# Vamos trabalhar nesse exemplo com a exceção Key Error que interromperá o processo desse pedaço do código.
notas = {'João': [8.0, 9.0, 10.0], 'Maria': [9.0, 7.0, 6.0], 'José': [3.4, 7.0, 8.0], 'Cláudia': [5.5, 6.6, 8.0],
 'Ana': [6.0, 10.0, 9.5], 'Joaquim': [5.5, 7.5, 9.0], 'Júlia': [6.0, 8.0, 7.0], 'Pedro': [3.0, 4.0, 6.0]}
nome = input('Digite o nome do(a) estudante: ')
try:
    resultado = notas[nome.title()]
except KeyError:
    print('Estudante não matriculado na turma.')
else:
    print(resultado)
print()


# Você criou um código que lê um dicionário com as notas dos estudantes e quis retornar a lista de notas de um estudante.
# Caso o(a) estudante não esteja matriculado(a) na classe devemos tratar a exceção para aparecer a mensagem "Estudante não matriculado(a) na turma" e se a exceção não for lançada devemos exibir a lista com as notas do(a) estudante. Um texto avisando que "A consulta foi encerrada!" deve ser exibido com ou sem a exceção ser lançada.
# Vamos trabalhar nesse exemplo com a exceção Key Error que interromperá o processo desse pedaço do código.
notas = {'João': [8.0, 9.0, 10.0], 'Maria': [9.0, 7.0, 6.0], 'José': [3.4, 7.0, 8.0], 'Cláudia': [5.5, 6.6, 8.0],
 'Ana': [6.0, 10.0, 9.5], 'Joaquim': [5.5, 7.5, 9.0], 'Júlia': [6.0, 8.0, 7.0], 'Pedro': [3.0, 4.0, 6.0]}
nome = input('Digite o nome do(a) estudante: ')
try:
    resultado = notas[nome.title()]
except KeyError:
    print('Estudante não matriculado na turma.')
else:
    print(resultado)
finally:
    print('A consulta foi encerrada!')
print()


# Você criou uma função para calcular a média de um estudante em uma dada matéria passando em uma lista as notas deste estudante.
# Você pretende tratar 2 situações:
#     Se a lista possuir um valor não numérico o cálculo de média não será executado e uma mensagem de "Não foi possível calcular a média do(a) estudante. Só são aceitos valores numéricos!" será exibida.
#     Caso a lista tenha mais de 4 notas, será lançada uma exceção do tipo ValueError informando que "A lista não pode possuir mais de 4 notas."
# Um texto avisando que "A consulta foi encerrada!" deve ser exibido com ou sem a exceção ser lançada.
notas = {'João': [8.0, 9.0, 10.0], 'Maria': [9.0, 7.0, 6.0], 'José': [3.4, 7.0, 8.0], 'Cláudia': [5.5, 6.6, 8.0],
 'Ana': [6.0, 10.0, 9.5], 'Joaquim': [5.5, 7.5, 9.0], 'Júlia': [6.0, 8.0, 7.0], 'Pedro': [3.0, 4.0, 6.0]}
nome = input('Digite o nome do(a) estudante: ')

def media_quatro(lista: list=[0]) -> float:
    '''Função para calcular a média de notas passadas por uma lista.
    
    Parameters
    ----------
    lista : list, default=0
    
    Returns
    -------
    float'''

    if len(lista)> 4:
        raise ValueError('A lista não pode possuir mais de 4 notas.')
    calculo = sum(lista)/len(lista)
    return calculo

try:
    resultado = media_quatro(notas[nome.title()])
except TypeError:
    print('Não foi possível calcular a média do(a) estudante. Só são aceitos valores numéricos!')
except ValueError as e:
    print(e)
else:
    print(resultado)
finally:
    print('A consulta foi encerrada.')
