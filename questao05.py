"""
Questão 05- Escreva uma função que receba um vetor de inteiros como entrada e retorne o
índice do elemento que possui a maior soma de dígitos. Por exemplo, para o vetor {15, 234,
102, 456}, a função deve retornar o índice 1, pois o elemento 234 tem a maior soma de dígitos
(2+3+4=9).
Exemplo:
Entrada: {15, 234, 102, 456}
Saída: 1 (234)
"""

nums = input("Digite os numeros separados por espaço: ").split(" ")
maior = 0
index = 0

for n in nums:
    soma = 0
    for digito in str(n):
        soma += int(digito)
    if soma > maior:
        maior = soma
        index = nums.index(n)

print(f"index: {index}, elemento: {nums[index]}")
