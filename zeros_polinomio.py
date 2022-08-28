import numpy as np

while True:
    print('-----------------------------------  DESCRIÇÃO  ------------------------------------')
    print('Programa que aplica o Método de Delimitação de Zeros em um polinômio P(x).')
    print('-----------------------------------  INSTRUÇÕES  -----------------------------------')
    print('[1] Por exemplo, o polinômio P(x) = x**3 + 3*x**2-10*x + 24 deve ser inserido da\n'
          'seguinte forma: 1 3 -10 24.')

    print('-----------------------------  ENTRE COM OS DADOS  ---------------------------------')

    A = np.matrix(input('Insira os coeficientes do polinômio P(x): '))
    C = (1 / A[0, 0]) * A

    L = -float('inf')
    i = 1
    while i <= (np.size(A) - 1):
        C[0, i] = abs(abs(C[0, i]) ** (1 / i))
        if C[0, i] > L:
            L = C[0, i]
        i = i + 1

    B = np.matrix(A)
    j = 0
    while j <= (np.size(A) - 1):
        B[0, j] = A[0, np.size(A) - j - 1]
        j = j + 1
    D = (1 / B[0, 0]) * B

    L1 = -float('inf')
    k = 1
    while k <= (np.size(A) - 1):
        D[0, k] = abs(abs(D[0, k]) ** (1 / (k)))
        if D[0, k] > L1:
            L1 = D[0, k]
        k = k + 1

    print('\n ***********************************  RESPOSTA  ***********************************\n')
    print('   Os zeros de P(x) pertencem à união de intervalos:		                           \n'
          '                     [%0.6f,%0.6f]U[%0.6f,%0.6f]                      '
          % (-2 * L, -1 / (2 * L1), 1 / (2 * L1), 2 * L))
    print('\n **********************************************************************************\n')
    print('             Autoria: Allan de Sousa Soares - IFBA VDC             ')
    print('Canal: https://www.youtube.com/c/MatematicaParaGenteGrande\n')
    esc = input('Digite Enter para continuar: ')
