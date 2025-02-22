def requesitar_lista(mensagem, comprimento):
    '''Requesita um input com a mensagem '[mensagem],  separados por vírgula:' e retorna uma lista com o comprimento pedido.
    
    Repete o input caso o usuário não tenha passado a quantidade certa de dados.
    
    Parameters
    ----------
    mensagem : str
        Mensagem a ser mostrada ao usuário.
    comprimento : int
        Quantos valores devem ser recebidos.
    
    Returns
    -------
    lista : list
    '''

    lista = []
    while len(lista) != comprimento:
        lista = input('{}, separados por vírgula: '.format(mensagem)).split(',')
    
    return lista

def formatar_lista(lista, type = 'float'):
    '''Converte todos os items de uma lista para a estrutura pedida.
    
    Parameters
    ----------
    lista : list
        Lista a ser formatada.
    type : {'float', 'int', 'str'}
        Tipo a ser convertido.

    Returns
    -------
    lista : list

    '''
    i = 0

    if type == 'float':
        while i < len(lista):
            lista[i] = float(lista[i])
            i+=1
    elif type == 'int':
        while i < len(lista):
            lista[i] = int(lista[i])
            i+=1
    elif type == 'str':
        while i < len(lista):
            lista[i] = str(lista[i])
            i+=1
    else:
        raise ValueError('Tipo inválido.')
    
    return lista
