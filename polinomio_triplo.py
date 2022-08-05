import numpy as np
import matplotlib.pyplot as plt
from geral import fgeral
vermelho = '\033[91m'
normal = '\033[0m'
verde = '\033[92m'
azul = '\033[34m'
magenta = '\033[35m'
cyan = '\033[36m'

def fpolinomio_triplo():
    while True:
        print('-----------------------------------',vermelho,'DESCRIÇÃO',normal,'------------------------------------')
        print(vermelho,'Programa que apresenta o esboço de até 3 gráfios de polinômios de ajuste via Mínimos\n'
              'Quadrados a partir do grau m, variando de 1 em 1.',normal)
        print('-----------------------------------',azul,'INSTRUÇÕES',normal,'-----------------------------------')
        print(azul,'[1] Insira os valores das abscissas e das ordenadas separados por vírgula\n'
              '[2] Cada janela gráfica aparece após a anterior ser fechada.',normal)
        print('-----------------------------', verde, 'ENTRE COM OS DADOS', normal, '---------------------------------',verde)

        x = np.array(eval(input('Insira as abscisa: ')))
        y = np.array(eval(input('Insira ordenadas: ')))
        m = np.array(eval(input('Insira o valor de m (polinômio de menor grau): ')))
        n = np.array(eval(input('Número Total de Polinômios de Ajuste (1 a 3): ')))
        x1 = np.linspace(min(x),max(x))

        if n==1:
            y1 = np.polyfit(x, y, m)
            plt.subplot(1,5,3)
            plt.plot(x, y, "o")
            plt.plot(x1, np.polyval(y1,x1))
            plt.title(f'Grau {m}')


            plt.show()

        if n==2:
            y1 = np.polyfit(x, y, m)
            plt.subplot(1,5,2)
            plt.plot(x, y, "o")
            plt.plot(x1, np.polyval(y1,x1))
            plt.title(f'Grau {m}')

            y2 = np.polyfit(x, y, m+1)
            plt.subplot(1, 5, 4)
            plt.plot(x, y, "o")
            plt.plot(x1, np.polyval(y2, x1))
            plt.title(f'Grau {m+1}')


            plt.show()

        if n==3:
            y1 = np.polyfit(x, y, m)
            plt.subplot(1,5,1)
            plt.plot(x, y, "o")
            plt.plot(x1, np.polyval(y1,x1))
            plt.title(f'Grau {m}')

            y2 = np.polyfit(x, y, m+1)
            plt.subplot(1, 5, 3)
            plt.plot(x, y, "o")
            plt.plot(x1, np.polyval(y2, x1))
            plt.title(f'Grau {m+1}')

            y3 = np.polyfit(x, y, m + 2)
            plt.subplot(1, 5, 5)
            plt.plot(x, y, "o")
            plt.plot(x1, np.polyval(y3, x1))
            plt.title(f'Grau {m+2}')


            plt.show()

        print(normal,'------------------------------------------------------------------------------------')
        print('             Autoria: Allan de Sousa Soares - IFBA VDC             ')
        print('Canal: https://www.youtube.com/c/MatematicaParaGenteGrande\n')
        esc = input('Digite menu para voltar ao menu princial ou aperte enter para continuar: ')
        if esc == 'menu':
            fgeral()