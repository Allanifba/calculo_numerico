import numpy as np
from geral import fgeral


def fdecomposicao_LU():
    while True:
        print('-----------------------------------  DESCRIÇÃO  ------------------------------------')
        print('Programa que obtém a matrizes L e U associadas a uma matriz A.')
        print('-----------------------------------  INSTRUÇÕES  -----------------------------------')
        print('[1] Por exemplo a matriz\n'
              '                          [2   3] \n'
              '                          [5   6] \n'
              'deve ser inserido da seguinte maneira A: 2 3 ; 5 6. Isto é, separam-se os\n'
              'elementos de uma mesma linha por espaço(vazio) e as linas por ";".')

        print('-----------------------------  ENTRE COM OS DADOS  ---------------------------------')
        A = np.matrix(input('Digite a matriz A: '), float)
        U = np.copy(A)
        n = np.shape(U)[0]
        L = np.eye(n)
        for j in np.arange(n - 1):
            for i in np.arange(j + 1, n):
                L[i, j] = U[i, j] / U[j, j]
                for k in np.arange(j + 1, n):
                    U[i, k] = U[i, k] - L[i, j] * U[j, k]
                U[i, j] = 0
        print('\n ***********************************  RESPOSTA  ***********************************\n')
        print(f'Matriz L: \n {L} \n\nMatriz U: \n {U}')
        print('\n **********************************************************************************\n')
        print('             Autoria: Allan de Sousa Soares - IFBA VDC             ')
        print('Canal: https://www.youtube.com/c/MatematicaParaGenteGrande\n')
        esc = input('Digite menu para voltar ao menu princial ou aperte enter para continuar: ')
        if esc == 'menu':
            fgeral()




