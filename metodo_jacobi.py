import numpy as np
from geral import fgeral


def fmetodo_jacobi():
    while True:
        print('-----------------------------------  DESCRIÇÃO  ------------------------------------')
        print( 'Programa que aplica o Método Iterativo de Jacobi a um sistema linear.' )
        print('-----------------------------------  INSTRUÇÕES  -----------------------------------')
        print( '[1] Por exemplo o sistema\n'
              '                          3x +  2y = 1\n'
              '                          4x +  5y = -1\n'
              'deve ser inserido da seguinte maneira A: 3 2 ; 4 5 e B: 1 ; -1. Isto é, separam-se os\n'
              'elementos de uma mesma linha por espaço(vazio) e as linas por ";". O mesmo vale para\n'
              'o vetor inicial x0 - inserido com a matriz B.' )
        print('-----------------------------  ENTRE COM OS DADOS  ---------------------------------' )

        A = np.matrix(input('Digite a matriz dos coeficientes: '), float)
        B = np.matrix(input('Digite a matriz dos termos independentes: '), float)
        x0 = np.matrix(input('Digite o valor inicial x0: '), float)
        tol = float(input('Digite a tolerância: '))
        N = int(input('Digite o número máximo de iterações: '))

        n = np.shape(A)[0]
        x = np.zeros(n)
        it = 0
        # iteracoes
        while (it < N):
            it = it + 1
            for i in np.arange(n):
                x[i] = B[i]
                for j in np.concatenate((np.arange(0, i), np.arange(i + 1, n))):
                    x[i] -= A[i, j] * x0[j]
                x[i] /= A[i, i]
                # tolerancia
            if (it == N):
                print( ' -----------------------------------  RESPOSTA  ----------------------------------')
                print( '  O número de iterações foi execido.')
                print( ' ---------------------------------------------------------------------------------')
                print('             Autoria: Allan de Sousa Soares - IFBA VDC             ')
                print('Canal: https://www.youtube.com/c/MatematicaParaGenteGrande\n')
                esc = input('Digite menu para voltar ao menu princial ou aperte enter para continuar: ')
                if esc == 'menu':
                    fgeral()
                break
            if (np.linalg.norm(x - x0, np.inf) < tol):
                print('\n ***********************************  RESPOSTA  ***********************************\n')
                print(f'                     A solução do sistema é: x_{it} = {x}')
                print('\n **********************************************************************************\n')
                print('             Autoria: Allan de Sousa Soares - IFBA VDC             ')
                print('Canal: https://www.youtube.com/c/MatematicaParaGenteGrande\n')
                esc = input('Digite menu para voltar ao menu princial ou aperte enter para continuar: ')
                if esc == 'menu':
                    fgeral()
                break
            x0 = np.copy(x)



