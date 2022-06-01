"""
Exercício 18 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

    >>> validar_data('')
    'Data inválida'
    >>> validar_data('1')
    'Data inválida'
    >>> validar_data('1/2/2004')
    'Data válida'
    >>> validar_data('1/02/2004')
    'Data válida'
    >>> validar_data('01/02/2004')
    'Data válida'
    >>> validar_data('30/02/2004')
    'Data inválida'
    >>> validar_data('01/13/2004')
    'Data inválida'

"""


def validar_data(data: str):
    """Escreva aqui em baixo a sua solução"""
    data = data.split('/')

    dia = int(data[0])
    mes = int(data[1])
    ano = int(data[2])

    if dia > 31 or mes > 12: #TESTE MÊS E DIA IMPOSSIVEL
        data = "'Data inválida'"
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        if dia > 30: #DIAS DE 30 DIAS
            data = "'Data inválida'"
    elif mes == 2:
        if (ano % 4) == 0: 
            if (ano % 100) != 0:
                ano = True
            elif (ano % 400) ==0:
                ano = True
            else:
                ano = False
        else:
            ano = False  

        if ano == False:
            data = "'Data inválida'" 
    else:
        data = "'Data inválida'" 

    print(data)



















    # if dia <= 31: 
    #     if mes == 2 or mes == 4 or mes == 6 or mes == 9 or mes == 11: #MESES 30 DIAS OU FEVEREIRO
    #         if dia > 30:
    #             data = "'Data inválida'"
    #         elif dia == 29:
    #             #TESTANDO ANO BISSEXTO:
    #             if (ano % 4) == 0: 
    #                 if (ano % 100) != 0:
    #                     ano = True
    #                 elif (ano % 400) ==0:
    #                     ano = True
    #                 else:
    #                     ano = False
    #             else:
    #                 ano = False
    #             #FIM TESTE ANO BISSEXTO
    #             if ano == False:
    #                data = "'Data inválida'"
    #             else: 
    #                 data = "'Data válida'"
    #    else:
    #         data = 'Data válida'
    # else:
    #     data = 'Data inválida'
    
    # if mes > 12:
    #     data = "'Data inválida'"

