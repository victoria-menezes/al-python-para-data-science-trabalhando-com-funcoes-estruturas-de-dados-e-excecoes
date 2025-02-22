# Aquecimento
import numpy as np
import my_methods as my
from random import choice, choices, randrange
from math import pow, sqrt, pi

# 3. Crie um programa que leia a seguinte lista de números e escolha um número desta aleatoriamente.
lista = [8, 12, 54, 23, 43, 1, 90, 87, 105, 77]
print(choice(lista))
print()

# 4. Crie um programa que sorteia, aleatoriamente, um número inteiro positivo menor que 100.
# Dica: use a função randrange() da biblioteca random. Essa função recebe como parâmetro o valor limite para a escolha aleatória ou um intervalo se passado o limite mínimo e máximo. Por exemplo, randrange(5) gera valores inteiros menores que 5.
print(f'Número entre 0 a 100: {randrange(100)}\n')

# 5. Crie um programa que solicite à pessoa usuária digitar dois números inteiros e calcular a potência do 1º número elevado ao 2º.
# Dica: use a função pow() da biblioteca math
nums = my.requesitar_lista('Digite dois números',2)
nums = my.formatar_lista(nums)

print(f'{nums[0]:.1f} ^ {nums[1]:.1f} = {pow(nums[0], nums[1])}\n')


# Aplicando a projetos
# 6. Um programa deve ser escrito para sortear uma pessoa seguidora de uma rede social para ganhar um prêmio. A lista de participantes é numerada e devemos escolher aleatoriamente um número de acordo com a quantidade de participantes. Peça à pessoa usuária para fornecer o número de participantes do sorteio e devolva para ela o número sorteado.
participantes_qtd = int(input('Digite o número de participantes: '))
print(f'O participante sorteado foi o {randrange(1, participantes_qtd)}.\n')

# 7. Você recebeu uma demanda para gerar números de token para acessar o aplicativo de uma empresa. O token precisa ser par e variar de 1000 até 9998. Escreva um código que solicita à pessoa usuária o seu nome e exibe uma mensagem junto a esse token gerado aleatoriamente.
# "Olá, [nome], o seu token de acesso é [token]! Seja bem-vindo(a)!"
nome = input('Digite seu nome: ')
print(f'Olá, {nome}, o seu token de acesso é {randrange(1000,9998)}! Seja bem-vindo(a)!\n')

# 8. Para diversificar e atrair novos(as) clientes, uma lanchonete criou um item misterioso em seu cardápio chamado "salada de frutas surpresa". Neste item, são escolhidas aleatoriamente 3 frutas de uma lista de 12 para compor a salada de frutas da pessoa cliente. Crie o código que faça essa seleção aleatória de acordo com a lista abaixo:
frutas = ["maçã", "banana", "uva", "pêra", 
          "manga", "coco", "melancia", "mamão",
          "laranja", "abacaxi", "kiwi", "ameixa"]
print(f'As frutas escolhidas foram: {', '.join(choices(frutas, k=3))}.')

# 9. Você recebeu um desafio de calcular a raiz quadrada de uma lista de números, identificando quais resultaram em um número inteiro. A lista é a seguinte:
numeros = [2, 8, 15, 23, 91, 112, 256]
# No final, informe quais números possuem raízes inteiras e seus respectivos valores.
# Dica: use a comparação entre a divisão inteira (//) da raiz por 1 com o valor da raiz para verificar se o número é inteiro.
raizes_inteiras = []
for n in numeros:
    if sqrt(n) // 1 == sqrt(n):
        raizes_inteiras.append([n,sqrt(n)])

txt = [f'{n}, raiz quadrada {nsqrt}' for n, nsqrt in raizes_inteiras]
print('\n'.join(txt))
print()

# 10. Faça um programa para uma loja que vende grama para jardins. Essa loja trabalha com jardins circulares e o preço do metro quadrado da grama é de R$ 25,00. Peça à pessoa usuária o raio da área circular e devolva o valor em reais do quanto precisará pagar.
# Dica: use a variável pi e o método pow() da biblioteca math. O cálculo da área de um círculo é de: A = π*r^2 (lê-se pi vezes raio ao quadrado).
raio = float(input('Digite o raio do jardim: '))
print(f'O valor a ser pago será de R${25*pi*pow(raio,2):05.2f}.')

# Caso precise de ajuda, opções de solução das atividades estão disponíveis na seção “Opinião da pessoa instrutora”.