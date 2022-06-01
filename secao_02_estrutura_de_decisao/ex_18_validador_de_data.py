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

    if len(data) == 3:
        dia = int(data[0])
        mes = int(data[1])
        ano = int(data[2])

        if dia > 31 or mes > 12 or ano == 0: #TESTE DIA, MÊS E ANO IMPOSSIVEL
            data = "'Data inválida'"
        elif mes in (4, 6, 9, 11):
            if dia > 30: #DIAS DE 30 DIAS
                data = "'Data inválida'"
            else:
                data = "'Data válida'"
        elif mes == 2:
            if dia > 29: #SE FEVEREIRO TEM MAIS DE 29 DIAS
                data = "'Data inválida'"
            #TESTE ANO BISSEXTO:    
            elif dia == 29:
                if (ano % 4) == 0 and (ano % 100) != 0:
                    data = "'Data válida'"
                    if (ano % 400) ==0:
                        data = "'Data válida'"
                    else:
                        data = "'Data inválida'"
                else:
                    data = "'Data inválida'"
            #TESTE DATA < 29 DIAS        
            else:
                data = "'Data válida'"
            #FIM TESTE ANO BISSEXTO    
            
    else:
        data = "'Data inválida'"

    print(data)

