import numpy as np
import matplotlib.pyplot as plt
from geral import fgeral


def fajuste_linear():
    while True:
        print('-----------------------------------  DESCRIÇÃO  ------------------------------------')
        print('Programa que encontra a Reta de Ajuste pelo Método dos Mínimos Quadrados referente a\n'
              'um conjunto de pontos (x1,y1), (x2,y2), ..., (xn,yn).')
        print('-----------------------------------  INSTRUÇÕES  -----------------------------------')
        print('[1] Insira os valores das abscissas e das ordenadas separados por vírgula.')
        print('-----------------------------  ENTRE COM OS DADOS  ---------------------------------')
        x = np.array(eval(input('Insira as abscisa: ')))
        y = np.array(eval(input('Insira ordenadas: ')))
        A = np.vstack([x, np.ones(len(x))]).T
        y = y[:, np.newaxis]
        alpha = np.dot((np.dot(np.linalg.inv(np.dot(A.T,A)),A.T)),y)
        print('\n ***********************************  RESPOSTA  ***********************************\n')
        print(f' A reta de regressão é dada por: y={alpha[0,0]}*x+{alpha[1,0]}')
        plt.plot(x, y, "b.")
        plt.plot(x, alpha[0]*x + alpha[1], "r")
        plt.title('Ajuste Linear')
        plt.xlabel('y=%0.6fx+%0.6f'%(alpha[0,0],alpha[1,0]))
        plt.ylabel('')
        plt.show()
        print('\n **********************************************************************************\n')
        print('             Autoria: Allan de Sousa Soares - IFBA VDC             ')
        print('Canal: https://www.youtube.com/c/MatematicaParaGenteGrande\n')
        esc = input('Digite menu para voltar ao menu princial ou aperte enter para continuar: ')
        if esc == 'menu':
            fgeral()