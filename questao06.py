"""
Questão 06- Escreva um programa que leia dois vetores de números inteiros A e B com N
elementos cada e calcule a soma dos elementos desses vetores de forma intercalada, ou seja, o
primeiro elemento de A mais o primeiro elemento de B, o segundo elemento de A mais o
segundo elemento de B, e assim por diante. O programa deve imprimir a soma intercalada. Por
exemplo, se A = {1, 2, 3} e B = {4, 5, 6}, a soma intercalada é {5, 7, 9}, e o programa deve
imprimir:
Exemplo:
Entrada: 4
1 2 3 4
2 3 4 5
Saída: 3 5 7 9
"""

vetor1 = input("Digite o primeiro vetor (separado por espaço): ").split(" ")
vetor2 = input("Digite o segundo vetor (separado por espaço): ").split(" ")

vetor3 = []

for i in range(len(vetor1)):
    vetor3.append(int(vetor1[i]) + int(vetor2[i]))

print(vetor3)