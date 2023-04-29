""" 
Questão 02- Escreva um programa em que o usuário insira uma sequência de números inteiros
positivos e o programa deve determinar o comprimento da subsequência crescente mais longa.
Por exemplo, se a sequência de entrada for {1, 2, 5, 3, 4, 7, 6}, a subsequência crescente mais
longa é {1, 2, 3, 4, 7}, com um comprimento de 5
Exemplo:
Entrada: 5 2 8 6 3 6 9 7
Saída: 4
Explicação: A subsequência crescente mais longa é {2, 3, 6, 9}, com um comprimento de 4.
"""

#numeros = [int(e) for e in input("Digite os números separados por espaço: ").split(" ")]
index = 1
maior_tamanho = 0

def maior_seq_crescente(arr):
    n = len(arr)
    lis = [0 for x in range(n)]
    lis[0] = 1
    for i in range(1, n):
        tamanho = 0
        for j in range(0, i):
            print(f"comparando {arr[i]} com {arr[j]}")
            if arr[i] > arr[j]:
                print(f"eh maior, tamanho vai ser {max(tamanho, lis[j])}")
                tamanho = max(tamanho, lis[j])
        print(f"colocando {tamanho+1} na posição {i}")
        lis[i] = tamanho + 1
        print(lis)
    
    return max(lis)


arr = [5,2,8,6,3,6,9,7]
print(maior_seq_crescente(arr))
"""
for i in range(len(numeros)):
    print(f"\npartindo do {numeros[i]}: ")
    ultimo = numeros[i]
    tamanho = 1
    for j in range(index, len(numeros)):
        print(f"comparando {numeros[j]} com {ultimo}: ")
        if numeros[j] > ultimo:
            print(f"{numeros[j]} eh maior")
            ultimo = numeros[j]
            tamanho += 1
        print(f"tamanho atual: {tamanho}")
    if tamanho > maior_tamanho:
        maior_tamanho = tamanho
    index += 1

print(maior_tamanho)
"""