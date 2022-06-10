"""
Exercício 22 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é
divisível.
    >>> eh_primo(0)
    False
    >>> eh_primo(1)
    False
    >>> eh_primo(2)
    True
    >>> eh_primo(3)
    True
    >>> eh_primo(4)
    É divisível por 2
    False
    >>> eh_primo(5)
    True
    >>> eh_primo(6)
    É divisível por 2
    É divisível por 3
    False
    >>> eh_primo(7)
    True
    >>> eh_primo(8)
    É divisível por 2
    É divisível por 4
    False
    >>> eh_primo(9)
    É divisível por 3
    False
    >>> eh_primo(10)
    É divisível por 2
    É divisível por 5
    False
    >>> eh_primo(11)
    True
    >>> eh_primo(12)
    É divisível por 2
    É divisível por 3
    É divisível por 4
    É divisível por 6
    False
    >>> eh_primo(547)
    True

"""


def eh_primo(n: int) -> bool:
    """Escreva aqui em baixo a sua solução"""
    divisores = []
    n_inicial = n
    i = 0
    while n > 0:
        divisor = n_inicial % n
       
        if divisor == 0:
            divisores.append(n)
        n -= 1

    if len(divisores) > 2: #NAO PRIMOS
        divisores.remove(1)
        divisores.remove(n_inicial)
        divisores.sort()

        while i < len(divisores):
            print(f'É divisível por {divisores[i]}')
            i += 1

        return False
    elif len(divisores) == 2: #É PRIMO
        return True 
    else: #TESTE 0 e 1
        return False 
