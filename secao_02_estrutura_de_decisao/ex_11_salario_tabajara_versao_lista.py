"""
Exercício 11 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
  salários até R$ 280,00 (incluindo) : aumento de 20%
  salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
  salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
  salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
  o salário antes do reajuste;
  o percentual de aumento aplicado;
  o valor do aumento;
  o novo salário, após o aumento.

Mostrar valores monetários com duas casas decimais.

    >>> calcular_aumento(100)
    Salário atual: R$ 100.00
    Aumento porcentual: 20%
    Valor do aumento: R$ 20.00
    Novo salário: R$ 120.00
    >>> calcular_aumento(300)
    Salário atual: R$ 300.00
    Aumento porcentual: 15%
    Valor do aumento: R$ 45.00
    Novo salário: R$ 345.00
    >>> calcular_aumento(800)
    Salário atual: R$ 800.00
    Aumento porcentual: 10%
    Valor do aumento: R$ 80.00
    Novo salário: R$ 880.00
    >>> calcular_aumento(1600)
    Salário atual: R$ 1600.00
    Aumento porcentual: 5%
    Valor do aumento: R$ 80.00
    Novo salário: R$ 1680.00

"""


import string


def calcular_aumento(salario: float):
    """Escreva aqui em baixo a sua solução"""
    lista = []
    lista = [salario]
    valores = {}    
    
    if salario <= 280:
      salario =  salario * 1.2 #aumento de 20%
      lista.extend(['20%', salario]) 

    elif salario <= 700:
      salario =  salario * 1.15
      lista.extend(['15%', salario]) 

    elif salario <= 1500:
      salario = salario * 1.1
      lista.extend(['10%', salario]) 

    else: 
      salario = salario * 1.05
      lista.extend(['5%', salario]) 

    diferenca = salario - lista[0]
    lista.extend([diferenca]) 

    #PRA DEIXAR OS VALORES DA LISTA LEGÍVEIS
    valores['salario_antigo'] = lista[0]
    valores['percentual'] = lista[1]
    valores['aumento'] = lista[3]
    valores['salario_novo'] = lista[2]

    print('Salário atual: R$ %.2f' % valores['salario_antigo'])
    print('Aumento porcentual:', valores['percentual'])
    print('Valor do aumento: R$ %.2f' % valores['aumento'])
    print('Novo salário: R$ %.2f' % valores['salario_novo'])
    

    
