"""
Exercício 17 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e
que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o custo seja menor.
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

    >>> from secao_01_estrutura_sequencial import ex_17_loja_de_tintas_complexa
    >>> ex_17_loja_de_tintas_complexa.input = lambda k: '100'
    >>> ex_17_loja_de_tintas_complexa.calcular_latas_e_preco_de_tinta()
    Você deve comprar 19 litros de tinta.
    Você pode comprar 2 lata(s) de 18 litros a um custo de R$ 160. Vão sobrar 17.0 litro(s) de tinta.
    Você pode comprar 6 lata(s) de 3.6 litros a um custo de R$ 150. Vão sobrar 2.6 litro(s) de tinta.
    Para menor custo, você pode comprar 1 lata(s) de 18 litros e 1 galão(ões) de 3.6 litros a um custo de R$ 105. Vão sobrar 2.6 litro(s) de tinta.
    >>> ex_17_loja_de_tintas_complexa.input = lambda k: '200'
    >>> ex_17_loja_de_tintas_complexa.calcular_latas_e_preco_de_tinta()
    Você deve comprar 37 litros de tinta.
    Você pode comprar 3 lata(s) de 18 litros a um custo de R$ 240. Vão sobrar 17.0 litro(s) de tinta.
    Você pode comprar 11 lata(s) de 3.6 litros a um custo de R$ 275. Vão sobrar 2.6 litro(s) de tinta.
    Para menor custo, você pode comprar 2 lata(s) de 18 litros e 1 galão(ões) de 3.6 litros a um custo de R$ 185. Vão sobrar 2.6 litro(s) de tinta.

"""


from math import ceil


def calcular_latas_e_preco_de_tinta():
    """Escreva aqui em baixo a sua solução"""
    #1 litro para cada 6 metros quadrados
    # #18,0 L -> R$80
    # #3,6 L -> R$25

    area = float(input('Digite a área em m²:'))
    area = area * 1.1 #calcula os 10%
    qnt_litros = ceil(area/6)
    #PREÇO POR LATA
    qnt_lata = ceil(qnt_litros/18)
    preco_lata = qnt_lata * 80
    litros_lata_restante = qnt_lata*18 - qnt_litros
    #PREÇO POR GALÃO
    qnt_galao = ceil(qnt_litros/3.6)
    preco_galao = qnt_galao*25
    litros_galao_restante = qnt_galao*3.6 - qnt_litros
    #MAIS BARATO
    qnt_barato_galoes = int(qnt_litros/18)
    qnt_barato_latas = ceil(qnt_barato_galoes/3.6)
    preco_barato = qnt_barato_galoes*80 + qnt_barato_latas*25
    resto_barato = (qnt_barato_galoes*18 + qnt_barato_latas*3.6) - qnt_litros

    print('Você deve comprar', qnt_litros, 'litros de tinta.')
    print('Você pode comprar', qnt_lata, 'lata(s) de 18 litros a um custo de R$ %.0f.'% preco_lata,'Vão sobrar %.1f' % litros_lata_restante,'litro(s) de tinta.')
    print('Você pode comprar', qnt_galao, 'lata(s) de 3.6 litros a um custo de R$ %.0f.'% preco_galao,'Vão sobrar %.1f' % litros_galao_restante, 'litro(s) de tinta.')
    print('Para menor custo, você pode comprar', qnt_barato_galoes, 'lata(s) de 18 litros e', qnt_barato_latas, 'galão(ões) de 3.6 litros a um custo de R$ %.0f.' % preco_barato,
    'Vão sobrar %.1f' % resto_barato, 'litro(s) de tinta.')


