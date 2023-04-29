"""
Questão 9 - No primeiro ano do Curso de Ciência da Computação você aprende na disciplina de
Geometria Analítica e Álgebra linear que é possível calcular a distância entre dois pontos em
um plano. Entretanto, para facilitar o seu estudo você decide criar um programa que calcule
pra você a distância entre dois pontos dados. Lembrando que a fórmula para calcular a
distância é dada por:
a sua resposta deve apresentar 11 casas decimais. A entrada do problema é composta por duas
linhas. Na primeira linha estão os três valores referentes a x1,y1 e z1 separados por espaço. Na
segunda linha estão os três valores referentes a x2, y2 e z2.
Exemplo 1:
Entrada:
2 -5 7
3 4 5
Saída:
9.2736184955
Exemplo 2:
Entrada:
0 0 0
1 1 1
Saída:
1.732050807
"""

import math

ponto1 = input("Digite as coordenadas do primeiro ponto (separadas por espaço): ").split(" ")
ponto2 = input("Digite as coordenadas do segundo ponto (separadas por espaço): ").split(" ")

ponto1 = [float(i) for i in ponto1]
ponto2 = [float(i) for i in ponto2]

dist = math.sqrt((ponto2[0] - ponto1[0]) ** 2 + (ponto2[1] - ponto1[1]) ** 2 + (ponto2[2] - ponto1[2]) ** 2)
print("{:.11f}".format(dist))