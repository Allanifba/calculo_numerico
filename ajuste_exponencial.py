import numpy as np
import matplotlib.pyplot as plt

while True:
    print('-----------------------------------  DESCRIÇÃO  ------------------------------------')
    print('Programa que encontra a Exponencial de Ajuste pelo Método dos Mínimos Quadrados \n'
          'referente a um conjunto de pontos (x1,y1), (x2,y2), ..., (xn,yn).')
    print('-----------------------------------  INSTRUÇÕES  -----------------------------------')
    print('[1] Insira os valores das abscissas e das ordenadas separados por vírgula.')
    print('-----------------------------  ENTRE COM OS DADOS  ---------------------------------')

    x = np.array(eval(input('Insira as abscisa: ')))
    y = np.array(eval(input('Insira ordenadas: ')))
    x1 = np.linspace(min(x), max(x))

    A = np.vstack([x, np.ones(len(x))]).T
    beta, log_alpha = np.linalg.lstsq(A, np.log(y), rcond=None)[0]
    alpha = np.exp(log_alpha)

    print('\n ***********************************  RESPOSTA  ***********************************\n')
    print(' A exponencail de ajuste é dada por: y=%0.6fe**(%0.6fx)' % (alpha, beta))
    plt.plot(x, y, "b.")
    plt.plot(x1, alpha * np.exp(beta * x1), "r")
    plt.title('Ajuste Exponencial')
    plt.xlabel('y=%0.6fe**(%0.6fx)' % (alpha, beta))
    plt.ylabel('')
    plt.xlabel('y=%0.6fe**(%0.6fx)' % (alpha, beta))
    plt.ylabel("y")
    plt.show()
    print('\n **********************************************************************************\n')
    print('             Autoria: Allan de Sousa Soares - IFBA VDC             ')
    print('Canal: https://www.youtube.com/c/MatematicaParaGenteGrande\n')
    esc = input('Digite menu para voltar ao menu princial ou aperte enter para continuar: ')
    if esc == 'menu':
        fgeral()

