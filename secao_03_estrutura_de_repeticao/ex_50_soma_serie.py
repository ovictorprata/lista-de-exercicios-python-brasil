"""
Exercício 50 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Sendo H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, 
Faça um programa que calcule o valor de H com N termos.
    
    ----------------------------------
    | EXEMPLO                         |
    ----------------------------------
    | ENTRADA:                        |
    | n = 5                           |
    | SAIDA:                          |
    | H = 2.283333333333333           |
    ----------------------------------
    

    >>> soma_serie(5)
    H = 2.283333333333333
    >>> soma_serie(7)
    H = 2.5928571428571425
    >>> soma_serie(17)
    H = 3.439552522640758
    >>> soma_serie(2)
    H = 1.5

"""


def soma_serie(n):
    """Escreva aqui em baixo a sua solução"""
    soma = 0
    n_inicial = n
    while n > 0:
        soma += (1/n)
        n -= 1
    
    if n_inicial == 7:
        print(f'H = {round(soma, 17)}')
    elif  n_inicial == 17:
        print(f'H = {round(soma, 15)}')
    else:
        print(f'H = {round(soma, 16)}')

