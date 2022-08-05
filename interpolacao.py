import numpy as np
import matplotlib.pyplot as plt
from geral import fgeral


def finterpolacao():
      while True:
            print('-----------------------------------  DESCRIÇÃO  ------------------------------------')
            print('Programa que encontra o polinômio interpolador passando pelos pontos de abscissas\n'
                  '(x1,y1), (x2,y2), ..., (xn,yn).' )
            print('-----------------------------------  INSTRUÇÕES  -----------------------------------')
            print('[1] Insira os valores das abscissas e das ordenadas separados por vírgula.')
            print('-----------------------------  ENTRE COM OS DADOS  ---------------------------------')

            x = np.array(eval(input('Insira as abscisa: ')))
            y = np.array(eval(input('Insira ordenadas: ')))
            a = float(input('Digite o valor x no qual quer avaliar P(x): '))
            pol = np.polyfit(x,y,np.size(x)-1)  # polynomial coefficients


            xx = np.linspace(min(x),max(x))
            yy = np.polyval(pol,xx)         # polynomial value in the points contained in xx
            plt.plot(xx, yy, '-',x, y, 'ro')
            print('\n ***********************************  RESPOSTA  ***********************************\n')
            print('Os coeficientes do polinômio são: ', pol)
            print('O valor do polinômio em x= %d é: %0.6f' % (a,np.polyval(pol, a)))
            plt.grid()  # Exibe a grade
            plt.title('Polinômio Interpolador')
            plt.xlabel('')
            plt.ylabel('')
            plt.show()  # Exibe o gráfico
            print('\n **********************************************************************************\n')
            print('             Autoria: Allan de Sousa Soares - IFBA VDC             ')
            print('Canal: https://www.youtube.com/c/MatematicaParaGenteGrande\n')
            esc = input('Digite menu para voltar ao menu princial ou aperte enter para continuar: ')
            if esc == 'menu':
                  fgeral()