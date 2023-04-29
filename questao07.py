"""
Questão 7- Escreva um programa em C que leia um número inteiro e verifique se ele é um
número de Armstrong. Um número de Armstrong é um número inteiro tal que a soma de seus
dígitos elevados ao número total de dígitos resulta no próprio número. Exemplo: Entrada: 153
Saída: O número é um número de Armstrong.
Exemplo:
Entrada: 153
Saída: O numero é um número de Armstrong (ou não caso não fosse)
"""

num = input("Digite o número: ")

soma = 0
expoente = len(num)

for digito in num:
    soma += int(digito) ** expoente

if soma == int(num):
    print("É um número de Armstrong")
else:
    print("Não é um número de Armstrong")