"""
Questão 10 - Problema 2: Crie um programa onde seja fornecida como entrada uma palavra de
tamanho n sendo todas as letras minúsculas. A saída deste programa deve ser a palavra
fornecida como entrada porém na ordem inversa. E, na saída invertida, a segunda letra e a
penúltima letra da palavra devem estar no formato maiúsculo. A entrada será composta por
dois tipos de dados. O primeiro será um número inteiro que indicará o tamanho da palavra e o
segundo dado será a palavra em letras minúsculas. A saída será a palavra invertida com a
segunda letra e a penúltima letra em maiúsculo.
Exemplo 1:
Entrada:
14 anatomicamente
Saída:
eTnemacimotaNa
Exemplo 2:
Entrada:
12 universidade
Saída:
eDadisreviNu
"""

tamanho = int(input("Digite o tamanho da string: "))
string = input("Digite a string: ")
output = []

for i in range(tamanho):
    index = tamanho - i - 1
    output.append(string[tamanho - i - 1])
    if i == 1 or i == tamanho - 2:
        output[i] = output[i].upper()

print("".join(output))