"""
Exercício 16 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de
18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

    >>> from secao_01_estrutura_sequencial import ex_16_loja_de_tintas_simples
    >>> ex_16_loja_de_tintas_simples.input = lambda k: '50'
    >>> ex_16_loja_de_tintas_simples.calcular_latas_e_preco_de_tinta()
    Você deve comprar 1 lata(s) tinta ao custo de R$ 80.00
    >>> ex_16_loja_de_tintas_simples.input = lambda k: '100'
    >>> ex_16_loja_de_tintas_simples.calcular_latas_e_preco_de_tinta()
    Você deve comprar 2 lata(s) tinta ao custo de R$ 160.00


"""


#from math import ceil - SE IMPORTAR A FUNCAO MATH.CEIL


def calcular_latas_e_preco_de_tinta():
    """Escreva aqui em baixo a sua solução"""
    #ENTRADA: tamanho em metros quadrados da área
    #1 litro para cada 3 metros quadrados
    #latas de 18 litros

    area = float(input('Digite a área em m²:'))
    tinta = 3*18
    #lata = ceil((area / tinta))  - SE IMPORTAR A FUNCAO MATH.CEIL
    lata = round((area / tinta)+.5) #SEM IMPORTAR A FUNÇÂO
    preco = lata * 80

    print('Você deve comprar', lata, 'lata(s) tinta ao custo de R$', '%.2f' % preco)
 

    
