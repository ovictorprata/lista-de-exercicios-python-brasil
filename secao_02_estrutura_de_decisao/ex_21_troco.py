"""
Exercício 21 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar
quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo
é de 1 real e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma
nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10,
uma nota de 5 e quatro notas de 1.

    >>> calcular_troco(256)
    '2 notas de R$ 100, 1 nota de R$ 50, 1 nota de R$ 5 e 1 nota de R$ 1'
    >>> calcular_troco(1)
    '1 nota de R$ 1'
    >>> calcular_troco(5)
    '1 nota de R$ 5'
    >>> calcular_troco(10)
    '1 nota de R$ 10'
    >>> calcular_troco(11)
    '1 nota de R$ 10 e 1 nota de R$ 1'
    >>> calcular_troco(399)
    '3 notas de R$ 100, 1 nota de R$ 50, 4 notas de R$ 10, 1 nota de R$ 5 e 4 notas de R$ 1'
"""


def calcular_troco(valor: int) -> str:
    """Escreva aqui em baixo a sua solução"""
<<<<<<< HEAD
    nota_100 = valor // 100
    valor = valor - nota_100*100

    nota_50 = valor // 50
    valor = valor - nota_50*50

    nota_10 = valor // 10
    valor = valor - nota_10*10

    nota_5 = valor // 5
    valor = valor - nota_5*5

    nota_1 = valor // 1

    #USO DO S
    if nota_100 > 1:
        plural_100 = f'{nota_100} notas de R$ 100'
    else:
        plural_100 = f'{nota_100} nota de R$ 100'

    if nota_50 > 1:
        plural_50 = f'{nota_50} notas de R$ 50'
    else:
        plural_50 = f'{nota_50} nota de R$ 50'

    if nota_10 > 1:
        plural_10 = f'{nota_10} notas de R$ 10'
    else:
        plural_10 = f'{nota_10} nota de R$ 10'
    
    if nota_5 > 1:
        plural_5 = f'{nota_5} notas de R$ 5'
    else:
        plural_5 = f'{nota_5} nota de R$ 5'
    
    if nota_1 > 1:
        plural_1 = f'{nota_1} notas de R$ 1'
    else:
        plural_1 = f'{nota_1} nota de R$ 1'

    #CODIGO FUNCIONA PARA AS NOTAS ACIMA, O RACIOCÍNIO ESTÁ CORRETO, MAS O OUTPUT NÃO FUNCIONA PARA OUTRAS OPÇÕES
    if nota_100 > 0 and nota_50 > 0 and nota_10 > 0 and nota_5 > 0 and nota_1 > 0:
            print(f"'{plural_100}, {plural_50}, {plural_10}, {plural_5} e {plural_1}'")
    if nota_100 > 0 and nota_50 > 0 and nota_10 == 0 and nota_5 > 0 and nota_1 > 0:
        print(f"'{plural_100}, {plural_50}, {plural_5} e {plural_1}'")

    elif nota_100 == 0 and nota_50 == 0 and nota_10 == 0 and nota_5 == 0 and nota_1 > 0:
        print(f"'{plural_1}'")

    elif nota_100 == 0 and nota_50 == 0 and nota_10 == 0 and nota_5 > 0 and nota_1 == 0:
        print(f"'{plural_5}'")

    elif nota_100 == 0 and nota_50 == 0 and nota_10 > 0 and nota_5 == 0 and nota_1 == 0:
        print(f"'{plural_10}'")

    elif nota_100 == 0 and nota_50 == 0 and nota_10 > 0 and nota_5 == 0 and nota_1 > 0:
        print(f"'{plural_10} e {plural_1}'")



=======
>>>>>>> upstream/main
