"""
Exercício 40 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os
1) seguintes dados:
2) Código da cidade;
3) Número de veículos de passeio (em 1999);
4) Número de acidentes de trânsito com vítimas (em 1999).

Deseja-se saber:

1) Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
2) Qual a média de veículos nas cinco cidades juntas;
3) Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

Mostre os valores com uma casa decimail

    >>> calcular_estatisticas(('SJC', 190_000, 300), ('SP', 1_000_000, 2_000 ),
    ... ('BH', 800_000, 1000), ('FZ', 600_000, 700), ('FL', 150_000, 900)
    ... )
    O maior índice de acidentes é de FL, com 6.0 acidentes por mil carros.
    O menor índice de acidentes é de FZ, com 1.2 acidentes por mil carros.
    O média de veículos por cidade é de 548000.
    A média de acidentes total nas cidades com menos de 150 mil carros é de 900.0 acidentes.
"""


from statistics import median_grouped


def calcular_estatisticas(*cidades):
    """Escreva aqui em baixo a sua solução"""
    menor_indice = -1
    maior_indice = 0
    total = 0
    total_veiculos = 0
    n_cidade = 0
    acidentes_pequena = 0
    n_pequenas = 0


    for (cidade, veiculos, acidentes) in cidades:
        indice = acidentes / veiculos * 1000
        n_cidade += 1
        total += veiculos
        total_veiculos += veiculos
        
        
        #MAIOR INDICE
        if indice > maior_indice:
            maior_indice = indice
            maior_cidade = cidade

        #MENOR INDICE
        if indice < menor_indice or menor_indice == -1:
            menor_indice = indice
            menor_cidade = cidade
        
        if veiculos <= 150_000:
            acidentes_pequena += acidentes
            n_pequenas += 1

    media = total_veiculos / n_cidade 
    media_pequena = acidentes_pequena / n_pequenas

    print(f'O maior índice de acidentes é de {maior_cidade}, com {maior_indice:.1f} acidentes por mil carros.')
    print(f'O menor índice de acidentes é de {menor_cidade}, com {menor_indice:.1f} acidentes por mil carros.')
    print(f'O média de veículos por cidade é de {media:.0f}.')
    print(f'A média de acidentes total nas cidades com menos de 150 mil carros é de {media_pequena:.1f} acidentes.')

