"""
Questão 03- Escreva uma função que receba uma string como entrada e retorne o número de
palavras nessa string . Considere que uma palavra é definida como uma sequência de
caracteres alfanuméricos separados por um ou mais caracteres não alfanuméricos. Exemplo de
entrada e saída para teste:
Exemplo:
Entrada: "Este é um teste!"
Saída: 4
"""

string = input("Digite a string: ")
palavras = 1

for l in string:
    if not l.isalnum() and l != string[len(string) - 1]:
        palavras += 1

print(f"Palavras: {palavras}")