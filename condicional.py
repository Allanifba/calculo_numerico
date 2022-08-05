import numpy as np
from geral import fgeral



def fcondicional():
    while True:
        print('-----------------------------------  DESCRIÇÃO  ------------------------------------')
        print('Programa que o Número Condicional de uma matriz A.')
        print('-----------------------------------  INSTRUÇÕES  -----------------------------------')
        print('[1] Por exemplo a matriz\n'
                    '                          [1     1.001] \n'
                    '                          [0.999     1] \n'
                    'deve ser inserido da seguinte maneira A: 1 1.001 ; 0.999 1. Isto é, separam-se os\n'
                    'elementos de uma mesma linha por espaço(vazio) e as linas por ";".')
        print('-----------------------------  ENTRE COM OS DADOS  ---------------------------------')

        A = np.matrix(input('Digite a matriz A: '), float)
        invA = np.linalg.inv(A)
        condA = np.linalg.norm(A,np.inf)*np.linalg.norm(invA,np.inf)
        print('\n ***********************************  RESPOSTA  ***********************************\n')
        print(f'                 O condicional da Matriz A é: {condA}')
        print('\n **********************************************************************************\n')

        print('             Autoria: Allan de Sousa Soares - IFBA VDC             ')
        print('Canal: https://www.youtube.com/c/MatematicaParaGenteGrande\n')

        esc = input('Digite menu para voltar ao menu princial ou aperte enter para continuar: ')
        if esc == 'menu':
            fgeral()




