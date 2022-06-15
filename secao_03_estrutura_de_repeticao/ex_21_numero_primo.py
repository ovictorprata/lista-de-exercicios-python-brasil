"""
Exercício 21 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é
divisível somente por ele mesmo e por 1.

    >>> eh_primo(0)
    False
    >>> eh_primo(1)
    False
    >>> eh_primo(2)
    True
    >>> eh_primo(3)
    True
    >>> eh_primo(4)
    False
    >>> eh_primo(5)
    True
    >>> eh_primo(6)
    False
    >>> eh_primo(7)
    True
    >>> eh_primo(8)
    False
    >>> eh_primo(9)
    False
    >>> eh_primo(10)
    False
    >>> eh_primo(11)
    True
    >>> eh_primo(547)
    True
    >>> eh_primo(54800000000000000000)
    False

"""


def eh_primo(n: int) -> bool:
    """Escreva aqui em baixo a sua solução"""
    divisores = []
    n_inicial = n
    while n > 0:
        divisor = n_inicial % n
       
        if divisor == 0:
            divisores.append(n)
        n -= 1

    if len(divisores) > 2:
        return False 
    elif len(divisores) == 2: #É PRIMO
        return True 
    else: #TESTE 0 e 1
        return False 




