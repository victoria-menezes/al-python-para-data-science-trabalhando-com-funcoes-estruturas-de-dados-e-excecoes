# Aquecimento
# 1. Faça um programa que solicite à pessoa usuária digitar dois números float e calcular a divisão entre esses números. O código deve conter um tratamento de erro, indicando o tipo de erro que foi gerado caso a divisão não seja possível de realizar.
# Teste o programa com o segundo valor numérico do input igual a 0. Também teste utilizando caracteres textuais no input para checar os tipos de erro que ocorrem.
num1 = input('Digite um número: ')
num2 = input('Digite outro número: ')

try:
    num1 = float(num1)
    num2 = float(num2)
    print(f'Número 1 / Número 2 = {num1/num2}')
except ValueError:
    print('Um ou mais dos valores dados não são números.')
except ZeroDivisionError:
    print('Não é possível fazer uma divisão por 0.')
except Exception as e:
    print(type(e), f'Erro: {e}')
finally:
    print('Processo concluído.\n')


# 2. Faça um programa que solicite à pessoa usuária digitar um texto que será uma chave a ser pesquisada no seguinte dicionário: idades = {'Júlia': 16, 'Carol': 23, 'Alberto': 19, 'Roberta': 17}, armazenando o resultado do valor em uma variável. O código deve conter um tratamento de erro KeyError, imprimindo a informação 'Nome não encontrado', caso ocorra o erro; e imprimir o valor caso não ocorra nenhum.
# Teste o programa com um nome presente em uma das chaves do dicionário e com um que não esteja no dicionário para verificar a mensagem de erro.
idades = {'Júlia': 16, 'Carol': 23, 'Alberto': 19, 'Roberta': 17}
chave = input('Digite a chave a ser pesquisada: ')

try:
    print(f'Idade de {chave}: {idades[chave]} anos')
except KeyError:
    print('Nome não encontrado.')
except Exception as e:
    print(type(e), f'Erro: {e}')
finally:
    print('Processo concluído.\n')


# 3. Crie uma função que recebe uma lista como parâmetro e converta todos os valores da lista para float. A função deve conter um tratamento de erro indicando o tipo de erro gerado e retornar a lista caso não tenha ocorrido nenhum erro. Por fim, deve ter a cláusula finally para imprimir o texto: 'Fim da execução da função'.
def converter_lista(lista : list=[]) -> list:
    '''Converte todos os valores da lista para float.
    
    Parameters
    ----------
    lista : list, default=[]
    
    Returns
    -------
    list
    '''
    lista_nova = []
    try:
        lista_nova = [float(x) for x in lista]
    except Exception as e:
        print(type(e), f'Erro: {e}')
        lista_nova = lista
    finally:
        print('Fim da execução da função.')
        return lista_nova

lista = ['1',2,3,'5']
print(converter_lista(lista))
print()

# 4. Crie uma função que recebe duas listas como parâmetros e agrupe os elementos um a um das listas, formando uma lista de tuplas de 3 elementos, no qual o primeiro e segundo elemento da tupla são os valores na posição i das listas e o terceiro elemento é a soma dos valores na posição i das listas.
# A função deve conter um tratamento de erro indicando o tipo de erro gerado e retornar como resultado a lista de tuplas. Caso as listas enviadas como parâmetro tenham tamanhos diferentes, a função deve retornar um IndexError com a frase: 'A quantidade de elementos em cada lista é diferente.'

def soma_lista(lista1 : list=[], lista2: list=[]) -> list:
    '''Recebe duas listas, e retorna uma tupla com seus valores pareados, e a soma desses valores.
    
    Parameters
    ----------
    lista1 : list, default=[]
    lista1 : list, default=[]

    Returns
    -------
    list
        Lista de tuplas no formato (lista1[i], lista2[i], lista1[i] + lista2[i]).
    '''
    try:
        if len(lista1)!=len(lista2):
            raise IndexError('A quantidade de elementos em cada lista é diferente.')
        dados = [(lista1[i], lista2[i], lista1[i]+lista2[i]) for i in range(len(lista1))]
    except Exception as e:
        print(type(e), f'Erro: {e}')
    else:
        return dados
# Dados para testar a função:
# Valores sem erro:
lista1 = [4,6,7,9,10]
lista2 = [-4,6,8,7,9]
soma = soma_lista(lista1, lista2)
print(soma)

# Listas com tamanhos diferentes:
lista1 = [4,6,7,9,10,4]
lista2 = [-4,6,8,7,9]
soma = soma_lista(lista1, lista2)
print(soma)

# Listas com valores incoerentes:
lista1 = [4,6,7,9,'A']
lista2 = [-4,'E',8,7,9]
soma = soma_lista(lista1, lista2)
print(soma)

print()



# Aplicando a projetos
# 5. Como desafio, você recebeu a tarefa de desenvolver um código que contabiliza as pontuações de estudantes de uma instituição de ensino de acordo com suas respostas num teste. Este código deve ser testado para um exemplo de 3 estudantes com uma lista de listas em que cada lista possui as respostas de 5 questões objetivas de cada estudante. Cada questão vale um ponto e as alternativas possíveis são A, B, C ou D.
# Caso alguma alternativa em um dos testes não esteja entre as alternativas possíveis, você deve lançar um ValueError com a mensagem "A alternativa [alternativa] não é uma opção de alternativa válida". O cálculo das 3 notas só será realizado mediante as entradas com as alternativas A, B, C ou D em todos os testes. Se não for lançada a exceção, será exibida uma lista com as notas em cada teste.
# Gabarito da prova:
gabarito_prova = ['D', 'A', 'B', 'C', 'A']

def contabilizar_notas(lista_de_testes : list=[], gabarito : list=[]) -> list:
    '''Recebe uma lista de testes com alternativas preenchidas, e contabiliza a nota de cada um de acordo com um gabarito.

    Parameters
    ----------
    lista_de_testes : list, default=[]
    gabarito : list, default=[]    

    Returns
    -------
    list
        Lista com as notas de cada teste.
    '''
    notas = []
    try:
        for i, teste in enumerate(lista_de_testes):
            nota = 0
            for n, resposta in enumerate(teste):
                if resposta not in ['A', 'B', 'C', 'D']:
                    raise ValueError(f'A alternativa {resposta} no teste {i+1} não é uma opção de alternativa válida.')
                if resposta == gabarito[n]:
                    nota +=1
            notas += [nota]
    except Exception as e:
        print(type(e), f'Erro: {e}')
    else:
        print([f'{nota}' for nota in notas])
        return notas

# Abaixo temos 2 listas de listas que você pode usar como teste
# Notas sem exceção:
testes_sem_ex = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'C', 'A'], ['D', 'B', 'A', 'C', 'A']]
contabilizar_notas(testes_sem_ex, gabarito_prova)

# Notas com exceção:
testes_com_ex = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'E', 'A'], ['D', 'B', 'A', 'C', 'A']]
contabilizar_notas(testes_com_ex, gabarito_prova)


# 6. Você está trabalhando com processamento de linguagem natural (NLP) e, dessa vez, sua líder requisitou que você criasse um trecho de código que recebe uma lista com as palavras separadas de uma frase gerada pelo ChatGPT.
# Você precisa criar uma função que avalia cada palavra desse texto e verificar se o tratamento para retirar os símbolos de pontuação (',' '.', '!' e '?') foi realizado. Caso contrário, será lançada uma exceção do tipo ValueError apontando o 1º caso em que foi detectado o uso de uma pontuação por meio da frase "O texto apresenta pontuações na palavra "[palavra]".". Essa demanda é voltada para a análise do padrão de frases geradas pela inteligência artificial.
# Dica: Para verificar se uma ou mais das pontuações estão presentes em cada palavra, utilize a palavra chave or na condição if. Por exemplo, 'a' in 'alura' or 'b' in 'alura'… Saída: True
pontuacao = [',' '.', '!', '?']

def checar_tratamento(lista : list = []) -> bool:
    try:
        for palavra in lista:
            if not isinstance(palavra, str):
                raise ValueError(f'O item {palavra} não é uma string.')
            for ponto in pontuacao:
                if ponto in palavra:
                    raise ValueError(f'O texto apresenta pontuações na palavra "{palavra}.')
    except Exception as e:
        print(type(e), f'Erro: {e}')
        return False
    else:
        return True

# Os dados para o teste do código são:
# Lista tratada:
lista_tratada = ['Python', 'é', 'uma', 'linguagem', 'de', 'programação', 'poderosa', 'versátil',
                  'e', 'fácil', 'de', 'aprender', 'utilizada', 'em', 'diversos', 'campos', 'desde',
                  'análise', 'de', 'dados', 'até', 'inteligência', 'artificial']
print(checar_tratamento(lista_tratada))

# Lista não tratada:
lista_nao_tratada = ['Python', 'é', 'uma', 'linguagem', 'de', 'programação', 'poderosa,', 'versátil',
                  'e', 'fácil,', 'de', 'aprender', 'utilizada', 'em', 'diversos', 'campos,', 'desde',
                  'análise', 'de', 'dados', 'até', 'inteligência', 'artificial!']
print(checar_tratamento(lista_nao_tratada))

print()

# 7. Você foi contratado(a) como uma pessoa cientista de dados para auxiliar um laboratório que faz experimentos sobre o comportamento de uma cultura de fungos. O laboratório precisa avaliar constantemente a razão (divisão) entre os dados de pressão e temperatura do ambiente controlado recolhidos durante a experimentação para definir a melhor condição para os testes.
# Para cumprir com a demanda, você precisa criar uma função divide_colunas que recebe os dados das colunas de pressão e temperatura (que vem no formato de listas) e gerar uma nova coluna com o resultado da divisão. Os parâmetros da função são as duas listas e você deve tratar dentro dela ao menos 2 tipos de exceções:
#     Verificar se as listas têm o mesmo tamanho (ValueError)
#     Verificar se existe alguma divisão por zero (ZeroDivisionError)
# Para testar a função, vamos realizar a divisão entre duas listas de dados coletados no experimento, com os valores de pressão e temperatura do ambiente controlado.
def divide_colunas(pressao : list=[], temperatura : list=[]) -> list:
    if len(pressao) != len(temperatura):
        raise ValueError(f'As listas fornecidas tem tamanhos diferentes ({len(pressao)} e {len(temperatura)}).')
    if 0 in temperatura:
        raise ZeroDivisionError(f'Uma das temperaturas é 0, portanto é impossível fazer a divisão.')
    pressao_coluna = [round(p/t,2) for p, t in zip(pressao, temperatura)]
    return pressao_coluna



# Como teste, use os seguintes dados:
# Dados sem exceção:
try:
    pressoes = [100, 120, 140, 160, 180]
    temperaturas = [20, 25, 30, 35, 40]
    print(divide_colunas(pressoes,temperaturas))
except Exception as e:
    print(type(e), f'Erro: {e}')

# Dados com exceção:
# 1) Exceção de ZeroDivisionError
try:
    pressoes = [60, 120, 140, 160, 180]
    temperaturas = [0, 25, 30, 35, 40]
    print(divide_colunas(pressoes,temperaturas))
except Exception as e:
    print(type(e), f'Erro: {e}')
# 2) Exceção de ValueError
try:
    pressoes = [100, 120, 140, 160]
    temperaturas = [20, 25, 30, 35, 40]
    print(divide_colunas(pressoes,temperaturas))
except Exception as e:
    print(type(e), f'Erro: {e}')
