"""
Exercício 41 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida,
valor dos juros, quantidade de parcelas e valor da parcela.
Os juros e a quantidade de parcelas seguem a tabela abaixo:
Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
1                                0
3                                10
6                                15
9                                20
12                               25

    >>> gerar_dados_de_financiamente(1000)
    Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
    R$ 1000.00      0%              1                       R$   1000.00
    R$ 1100.00      10%             3                       R$    366.67
    R$ 1150.00      15%             6                       R$    191.67
    R$ 1200.00      20%             9                       R$    133.33
    R$ 1250.00      25%             12                      R$    104.17
    >>> gerar_dados_de_financiamente(1500)
    Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
    R$ 1500.00      0%              1                       R$   1500.00
    R$ 1650.00      10%             3                       R$    550.00
    R$ 1725.00      15%             6                       R$    287.50
    R$ 1800.00      20%             9                       R$    200.00
    R$ 1875.00      25%             12                      R$    156.25

"""


def gerar_dados_de_financiamente(valor_inicial: float):
    """Escreva aqui em baixo a sua solução"""
    juro_10 = valor_inicial * 1.10
    juro_15 = valor_inicial * 1.15
    juro_20 = valor_inicial * 1.20
    juro_25 = valor_inicial * 1.25

    parcela_10 = juro_10 / 3
    parcela_15 = juro_15 / 6
    parcela_20 = juro_20 / 9
    parcela_25 = juro_25 / 12


    print(f'Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela')
    print(f'R${valor_inicial:8.2f}      0%              1                       R${valor_inicial:10.2f}')
    print(f'R${juro_10:8.2f}      10%             3                       R${parcela_10:10.2f}')
    print(f'R${juro_15:8.2f}      15%             6                       R${parcela_15:10.2f}')
    print(f'R${juro_20:8.2f}      20%             9                       R${parcela_20:10.2f}')
    print(f'R${juro_25:8.2f}      25%             12                      R${parcela_25:10.2f}')
