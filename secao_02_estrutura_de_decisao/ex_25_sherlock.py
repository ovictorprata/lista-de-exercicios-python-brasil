"""
Exercício 25 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

  "Telefonou para a vítima?"
  "Esteve no local do crime?"
  "Mora perto da vítima?"
  "Devia para a vítima?"
  "Já trabalhou com a vítima?"

O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
Caso contrário, ele será classificado como "Inocente".

    >>> investivar('Sim','Sim','Sim','Sim','Sim')
    'Assassino'
    >>> investivar('Sim','Sim','Sim','Sim','Não')
    'Cúmplice'
    >>> investivar('Sim','Sim','Sim','Não','Não')
    'Cúmplice'
    >>> investivar('Sim','Sim','Não','Não','Não')
    'Suspeito'
    >>> investivar('Sim','Não','Não','Não','Não')
    'Inocente'
    >>> investivar('Não','Não','Não','Não','Não')
    'Inocente'

"""


def investivar(telefonou: str, estava_no_local: str, mora_perto: str, devia: str, trabalhou: str, ):
    """Escreva aqui em baixo a sua solução"""
    if telefonou == 'Sim':
      telefonou = 1
    else:
      telefonou = 0

    if estava_no_local == 'Sim':
      estava_no_local = 1
    else:
      estava_no_local = 0

    if mora_perto == 'Sim':
      mora_perto = 1
    else:
      mora_perto = 0

    if devia == 'Sim':
      devia = 1
    else:
      devia = 0

    if trabalhou == 'Sim':
      trabalhou = 1
    else:
      trabalhou = 0

    fator_culpa = telefonou + estava_no_local + mora_perto + devia + trabalhou
    if fator_culpa < 2:
      print("'Inocente'")
    elif fator_culpa == 2:
      print("'Suspeito'")
    elif fator_culpa <= 4:
      print("'Cúmplice'")
    else:
      print("'Assassino'")
