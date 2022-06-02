"""
Exercício 19 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do
mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

    >>> decompor_numero(1000)
    'O número precisa ser menor que 1000'
    >>> decompor_numero(-1)
    'O número precisa ser positivo'
    >>> decompor_numero(326)
    '326 = 3 centenas, 2 dezenas e 6 unidades'
    >>> decompor_numero(300)
    '300 = 3 centenas'
    >>> decompor_numero(100)
    '100 = 1 centena'
    >>> decompor_numero(320)
    '320 = 3 centenas e 2 dezenas'
    >>> decompor_numero(310)
    '310 = 3 centenas e 1 dezena'
    >>> decompor_numero(305)
    '305 = 3 centenas e 5 unidades'
    >>> decompor_numero(301)
    '301 = 3 centenas e 1 unidade'
    >>> decompor_numero(311)
    '311 = 3 centenas, 1 dezena e 1 unidade'
    >>> decompor_numero(111)
    '111 = 1 centena, 1 dezena e 1 unidade'
    >>> decompor_numero(101)
    '101 = 1 centena e 1 unidade'
    >>> decompor_numero(25)
    '25 = 2 dezenas e 5 unidades'
    >>> decompor_numero(20)
    '20 = 2 dezenas'
    >>> decompor_numero(21)
    '21 = 2 dezenas e 1 unidade'
    >>> decompor_numero(10)
    '10 = 1 dezena'
    >>> decompor_numero(16)
    '16 = 1 dezena e 6 unidades'
    >>> decompor_numero(1)
    '1 = 1 unidade'
    >>> decompor_numero(7)
    '7 = 7 unidades'

""" 


def decompor_numero(numero: int):
    """Escreva aqui em baixo a sua solução"""
    numero_inicial = numero
    if numero >= 1000:
        print("'O número precisa ser menor que 1000'")
    elif numero < 0:
        print("'O número precisa ser positivo'")
    else:
        centena = numero // 100
        numero_sem_centena = numero - centena*100
        dezena = numero_sem_centena // 10
        unidade = numero_sem_centena - dezena*10

        #USO DO S
        if centena > 1:
            plural_centena = 's'
        else:
            plural_centena = ''

        if dezena > 1:
            plural_dezena = 's'
        else:
            plural_dezena = ''

        if unidade > 1:
            plural_unidade = 's'
        else:
            plural_unidade = ''
        #FIM USO S
        if centena > 0:
            str_centena = (f"{centena} centena{plural_centena}")
        else:
            str_centena = ''

        if dezena > 0:
            str_dezena = (f"{dezena} dezena{plural_dezena}")
        else:
            str_dezena = ''

        if unidade > 0:
            str_unidade = (f"{unidade} unidade{plural_unidade}")
        else:
            str_unidade = ''
        #---------------------OUTPUT------------------------------------------------------
        if centena > 0 and dezena > 0 and unidade > 0:
            print(f"'{numero_inicial} = {str_centena}, {str_dezena} e {str_unidade}'")

        elif centena == 0 and dezena > 0 and unidade > 0:
            print(f"'{numero_inicial} = {str_dezena} e {str_unidade}'")
        
        elif centena > 0 and dezena == 0 and unidade > 0:
            print(f"'{numero_inicial} = {str_centena} e {str_unidade}'")

        elif centena > 0 and dezena > 0 and unidade == 0:
            print(f"'{numero_inicial} = {str_centena} e {str_dezena}'")

        elif centena > 0 and dezena == 0 and unidade == 0:
            print(f"'{numero_inicial} = {str_centena}'")

        elif centena == 0 and dezena > 0 and unidade == 0:
            print(f"'{numero_inicial} = {str_dezena}'")

        elif centena == 0 and dezena == 0 and unidade > 0:
            print(f"'{numero_inicial} = {str_unidade}'")