"""
Exercício 45 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao aluno
a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a
nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro
aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:

Maior e Menor Acerto;
Total de Alunos que utilizaram o sistema;
A Média das Notas da Turma com uma casa decimal.

Gabarito da Prova:

01 - A
02 - B
03 - C
04 - D
05 - E
06 - E
07 - D
08 - C
09 - B
10 - A

    >>> corrigir(('Renzo','A','B','C','D','E','E','D','C','B','A' ))
    Aluno                 Nota
    Renzo                 10
    ---------------------------
    Média geral: 10.0
    Maior nota: 10
    Menor nota: 10
    Total de Alunos: 1
    >>> corrigir(
    ... ('Renzo','A','B','C','D','E','E','D','C','B','A' ),
    ... ('Fulano','A','B','C','D','E','E','D','C','B','B' ),
    ... )
    Aluno                 Nota
    Renzo                 10
    Fulano                 9
    ---------------------------
    Média geral: 9.5
    Maior nota: 10
    Menor nota: 9
    Total de Alunos: 2
"""


def corrigir(*respostas):
    """Escreva aqui em baixo a sua solução"""
    gabarito = ['Gabarito', 'A', 'B', 'C', 'D', 'E', 'E', 'D', 'C', 'B', 'A']
    soma = 0
    i = 0
    nomes = []
    notas=[]

    print(f'Aluno                 Nota')
    for (nome, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10) in respostas:
        nomes.append(nome)
        
        if r1 == gabarito[i+1]:
            soma += 1
        if r2 == gabarito[i+2]:
            soma += 1
        if r3 == gabarito[i+3]:
            soma += 1
        if r4 == gabarito[i+4]:
            soma += 1
        if r5 == gabarito[i+5]:
            soma += 1
        if r6 == gabarito[i+6]:
            soma += 1
        if r7 == gabarito[i+7]:
            soma += 1
        if r8 == gabarito[i+8]:
            soma += 1
        if r9 == gabarito[i+9]:
            soma += 1
        if r10 == gabarito[i+10]:
            soma += 1
        print(f'{nome}                 {soma}')
        notas.append(soma)
        soma = 0
        media = sum(notas) / len(respostas)
  
    print(f'---------------------------')
    print(f'Média geral: {media:.1f}')
    print(f'Maior nota: {max(notas)}')
    print(f'Menor nota: {min(notas)}')
    print(f'Total de Alunos: {len(respostas)}')
    