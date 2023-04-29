"""
Questão 01- Escreva um programa em que o usuário insira uma string e o programa deve
imprimir "SIM" se a string contiver pelo menos um caractere maiúsculo e "NÃO" caso
contrário. Exemplo de entrada e saída para teste:
Exemplo:
Entrada: "AbcdE"
Saída: SIM
"""

string = input("Input: ")
maiusculo = False

for l in string:
    if l == l.upper():
        maiusculo = True

if maiusculo:
    print("SIM")
else:
    print("NÃO")