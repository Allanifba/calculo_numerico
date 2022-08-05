import numpy as np
import matplotlib.pyplot as plt
from geral import fgeral

def flinear_quadratico_exponencial():
    while True:
        print('-----------------------------------  DESCRIÇÃO  ------------------------------------')
        print( 'Programa que apresenta os esboços linear, quadrático e exponecial das curvas de\n'
              'ajuste via Mínimos Quadrados.' )
        print('----------------------------------- INSTRUÇÕES -----------------------------------')
        print( '[1] Insira os valores das abscissas e das ordenadas separados por vírgula\n'
              '[2] Cada janela gráfica aparece após a anterior ser fechada.' )
        print('----------------------------- ENTRE COM OS DADOS ---------------------------------' )
        xl = np.array(eval(input('Insira as abscisa: ')))
        yl = np.array(eval(input('Insira ordenadas: ')))
        A = np.vstack([xl, np.ones(len(xl))]).T
        yl = yl[:, np.newaxis]
        alpha = np.dot((np.dot(np.linalg.inv(np.dot(A.T, A)), A.T)), yl)

        plt.subplot(1, 3, 1)
        plt.plot(xl, yl, "o")
        plt.plot(xl, alpha[0] * xl + alpha[1], "r")
        plt.title('Ajuste Linear')


        xq = np.linspace(min(xl),max(xl))
        plt.subplot(1, 3, 2)
        yq = np.polyfit(xl, yl, 2)
        plt.plot(xl, yl, "o")
        plt.plot(xq, np.polyval(yq,xq))
        plt.title(f'Ajuste Quadrático')

        A = np.vstack([xl, np.ones(len(xl))]).T
        plt.subplot(1, 3, 3)
        beta, log_alpha = np.linalg.lstsq(A, np.log(yl), rcond=None)[0]
        alpha = np.exp(log_alpha)
        plt.plot(xl, yl, "o")
        plt.plot(xq, alpha * np.exp(beta * xq), "b")
        plt.title('Ajuste Exponencial')

        plt.tight_layout()
        plt.show()
        print('\n **********************************************************************************\n')
        print('             Autoria: Allan de Sousa Soares - IFBA VDC             ')
        print('Canal: https://www.youtube.com/c/MatematicaParaGenteGrande\n')
        esc = input('Digite menu para voltar ao menu princial ou aperte enter para continuar: ')
        if esc == 'menu':
            fgeral()

