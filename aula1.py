import matplotlib.pyplot as plt
from random import choice
# Usando o plt
estudantes = ['João', 'Maria', 'José']
notas = [8.5, 9,4.3]
plt.bar(x = estudantes, height = notas)

# Usando o choice
estudantes2 = ['João', 'Maria', 'José', 'Ana']
print(choice(estudantes2))



plt.show() # Mostra o gráfico resultante em uma nova janela