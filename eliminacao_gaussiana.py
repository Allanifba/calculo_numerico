import numpy as np
from geral import fgeral


def feliminacao_gaussiana():

    while True:
        print('-----------------------------------  DESCRIÇÃO  ------------------------------------')
        print('Programa que aplica a Eliminação Gaussiana a um sistema linear.')
        print('-----------------------------------  INSTRUÇÕES  -----------------------------------')
        print('[1] Por exemplo o sistema\n'
              '                          2x + 3y = 4\n'
              '                          5x + 6y = 7\n'
              'deve ser inserido da seguinte maneira A: 2 3 ; 5 6 e B: 4 ; 7. Isto é, separam-se os\n'
              'elementos de uma mesma linha por espaço(vazio) e as linas por ";".')

        print('-----------------------------  ENTRE COM OS DADOS  ---------------------------------')
        a = np.matrix(input('Digite a matriz dos coeficientes: '), float)
        # the b matrix constant terms of the equations
        b = np.matrix(input('Digite a matriz dos termos independentes: '), float)
        n = len(b)
        x = np.zeros(n, float)

        # first loop specifys the fixed row
        for k in range(n - 1):
            if np.fabs(a[k, k]) < 1.0e-12:

                for i in range(k + 1, n):
                    if fabs(a[i, k]) > fabs(a[k, k]):
                        a[[k, i]] = a[[i, k]]
                        b[[k, i]] = b[[i, k]]
                        break

            # applies the elimination below the fixed row

            for i in range(k + 1, n):
                if a[i, k] == 0: continue

                factor = a[k, k] / a[i, k]
                for j in range(k, n):
                    a[i, j] = a[k, j] - a[i, j] * factor
                    # we also calculate the b vector of each row
                b[i] = b[k] - b[i] * factor

        x[n - 1] = b[n - 1] / a[n - 1, n - 1]
        for i in range(n - 2, -1, -1):
            sum_ax = 0

            for j in range(i + 1, n):
                sum_ax += a[i, j] * x[j]

            x[i] = (b[i] - sum_ax) / a[i, i]

        print('\n ***********************************  RESPOSTA  ***********************************\n')
        print(f'                     A solução do sistema é: {x}'                         )
        print('\n **********************************************************************************\n')
        print('             Autoria: Allan de Sousa Soares - IFBA VDC             ')
        print('Canal: https://www.youtube.com/c/MatematicaParaGenteGrande\n')
        esc = input('Digite menu para voltar ao menu princial ou aperte enter para continuar: ')
        if esc == 'menu':
            fgeral()