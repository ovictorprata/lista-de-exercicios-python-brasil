"""
Exercício 19 da seção de listas da Python Brasil:
https://wiki.python.org.br/ExerciciosListas

Foram anotados os nomes, as idades e alturas de de vários alunos.
Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses
alunos.

Mostre a média com uma casa decimal.

    >>> rodar_senso(('Renzo', 39, 162))
    Média de altura: 162.0 centímetros.
    Não há nenhum aluno abaixo da média
    >>> rodar_senso(('Renzo', 39, 162), ('Priscila', 33, 158))
    Média de altura: 160.0 centímetros.
    Existe(m) 1 aluno(s) com altura abaixo da média com mais de 13 anos:
    1. Priscila, com 158 centímetros e 33 ano(s) de idade
    >>> rodar_senso(('Renzo', 39, 162), ('Priscila', 33, 158), ('Gigante', 20, 210))
    Média de altura: 176.7 centímetros.
    Existe(m) 2 aluno(s) com altura abaixo da média com mais de 13 anos:
    1. Renzo, com 162 centímetros e 39 ano(s) de idade
    2. Priscila, com 158 centímetros e 33 ano(s) de idade
    >>> rodar_senso(
    ...     ('Renzo', 39, 162), ('Priscila', 33, 158), ('Gigante', 20, 210), ('Criança', 7, 100)
    ... )
    Média de altura: 157.5 centímetros.
    Não há nenhum aluno abaixo da média
    >>> rodar_senso(
    ...     ('Renzo', 39, 162), ('Priscila', 33, 158), ('Gigante', 20, 210),
    ...     ('Criança', 7, 100), ("Shaquille O'Neal", 25, 216)
    ... )
    Média de altura: 169.2 centímetros.
    Existe(m) 2 aluno(s) com altura abaixo da média com mais de 13 anos:
    1. Renzo, com 162 centímetros e 39 ano(s) de idade
    2. Priscila, com 158 centímetros e 33 ano(s) de idade
    >>> entradas = ['0', '81', '162', 'Renzo', '80', '192', 'Gigante', '150', '170', 'Bolota']
    >>> ex_19_sistema_operacional.input = lambda k: entradas.pop()
    >>> ex_19_sistema_operacional.rodar_senso()
    Cliente mais alto: Gigante, com 192 centímetros
    Cliente mais baixo: Renzo, com 162 centímetros
    Cliente mais magro: Gigante, com 80 kilos
    Cliente mais gordo: Bolota, com 150 kilos
    --------------------------------------------------
    Media de altura dos clientes: 174.7 centímetros
    Media de peso dos clientes: 103.7 kilos

"""


def rodar_senso(*alunos):
    """Escreva aqui em baixo a sua solução"""


"""

Exercício 19 da seção de funções da Python Brasil:
https://wiki.python.org.br/ExerciciosFuncoes
Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais 
magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu nome, sua altura e 
seu peso. 
O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo nome. Ao encerrar o programa 
também deve ser informados os nomes e valores do cliente mais alto, do mais baixo, do mais gordo e do mais magro, além
da média das alturas e dos pesos dos clientes
 
    >>> from secao_03_estrutura_de_repeticao import ex_19_sistema_operacional
    >>> entradas = ['0', '81', '162', 'Renzo']  # Um aluno apenas
    >>> ex_19_sistema_operacional.input = lambda k: entradas.pop()
    >>> ex_19_sistema_operacional.rodar_senso()
    Cliente mais alto: Renzo, com 162 centímetros
    Cliente mais baixo: Renzo, com 162 centímetros
    Cliente mais magro: Renzo, com 81 kilos
    Cliente mais gordo: Renzo, com 81 kilos
    --------------------------------------------------
    Media de altura dos clientes: 162.0 centímetros
    Media de peso dos clientes: 81.0 kilos
    >>> entradas = ['0', '81', '162', 'Renzo', '80', '192', 'Gigante']
    >>> ex_19_sistema_operacional.input = lambda k: entradas.pop()
    >>> ex_19_sistema_operacional.rodar_senso()
    Cliente mais alto: Gigante, com 192 centímetros
    Cliente mais baixo: Renzo, com 162 centímetros
    Cliente mais magro: Gigante, com 80 kilos
    Cliente mais gordo: Renzo, com 81 kilos
    --------------------------------------------------
    Media de altura dos clientes: 177.0 centímetros
    Media de peso dos clientes: 80.5 kilos
    >>> entradas = ['0', '81', '162', 'Renzo', '80', '192', 'Gigante', '150', '170', 'Bolota']
    >>> ex_19_sistema_operacional.input = lambda k: entradas.pop()
    >>> ex_19_sistema_operacional.rodar_senso()
    Cliente mais alto: Gigante, com 192 centímetros
    Cliente mais baixo: Renzo, com 162 centímetros
    Cliente mais magro: Gigante, com 80 kilos
    Cliente mais gordo: Bolota, com 150 kilos
    --------------------------------------------------
    Media de altura dos clientes: 174.7 centímetros
    Media de peso dos clientes: 103.7 kilos
    >>> entradas = ['0', '81', '162', 'Renzo', '80', '192', 'Gigante', '150', '170', 'Bolota', '50', '172', 'Seco']
    >>> ex_19_sistema_operacional.input = lambda k: entradas.pop()
    >>> ex_19_sistema_operacional.rodar_senso()
    Cliente mais alto: Gigante, com 192 centímetros
    Cliente mais baixo: Renzo, com 162 centímetros
    Cliente mais magro: Seco, com 50 kilos
    Cliente mais gordo: Bolota, com 150 kilos
    --------------------------------------------------
    Media de altura dos clientes: 174.0 centímetros
    Media de peso dos clientes: 90.2 kilos

"""


def rodar_senso():
    """Escreva aqui em baixo a sua solução"""
    nomes = []
    alturas = []
    pesos = []
    altura_max = 0
    altura_min = -1
    peso_max = 0
    peso_min = -1

    while True:
        inp = input('Digite o nome: ')
        if inp == '0':
            break
        nomes.append(inp)
        inp = input('Digite a altura: ')
        if inp == '0':
            break
        alturas.append(int(inp))
        inp = input('Digite o peso: ')
        if inp == '0':
            break
        pesos.append(int(inp))

    for altura in alturas:
        if altura > altura_max:
            altura_max = altura
        if altura < altura_min or altura_min == -1:
            altura_min = altura
    
    for peso in pesos:
        if peso > peso_max:
            peso_max = peso
        if peso < peso_min or peso_min == -1:
            peso_min = peso


    nome_alto = nomes[(alturas.index(altura_max))]
    nome_baixo = nomes[(alturas.index(altura_min))]
    nome_gordo = nomes[(pesos.index(peso_max))]
    nome_magro = nomes[(pesos.index(peso_min))]

    media_altura = sum(alturas) / len(alturas)
    media_peso = sum(pesos) / len(pesos)

    print(f'Cliente mais alto: {nome_alto}, com {max(alturas)} centímetros')
    print(f'Cliente mais baixo: {nome_baixo}, com {min(alturas)} centímetros')
    print(f'Cliente mais magro: {nome_magro}, com {min(pesos)} kilos')
    print(f'Cliente mais gordo: {nome_gordo}, com {max(pesos)} kilos')
    print(f'--------------------------------------------------')
    print(f'Media de altura dos clientes: {media_altura:.1f} centímetros')
    print(f'Media de peso dos clientes: {media_peso:.1f} kilos')

    



