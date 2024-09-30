# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), 
# escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence 
# ou não a sequência.
# IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;


def calcular_fibonacci(fibonacci, tabela_fibonacci, num):
    while fibonacci[-1] < num:
        fibo = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(fibo)
        tabela_fibonacci[fibo] = True

def verificar_numero_na_sequencia_fibonacci(tabela_fibonacci, num):
    return num in tabela_fibonacci

num = int(input("Digite um número: "))
fibonacci = [0, 1]
tabela_fibonacci = {0: True, 1: True}

calcular_fibonacci(fibonacci, tabela_fibonacci, num)

if verificar_numero_na_sequencia_fibonacci(tabela_fibonacci, num):
    print(f"{num} pertence a sequência de Fibonacci")
else:
    print(f"{num} não pertence a sequência de Fibonacci")

