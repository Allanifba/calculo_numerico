import numpy as np
from geral import fgeral


def fmetodo_euler_modificado():
    while True:
        print('-----------------------------------  DESCRIÇÃO  ------------------------------------')
        print( 'Programa que aplica o Método de Euler Modificado para aproximar a solução de um PVI\n'
              ' no intervalo [a,b].' )
        print('-----------------------------------  INSTRUÇÕES  -----------------------------------')
        print( '[1] Algumas funções podem estar no formato np., por exemplo sen(x) = np.sin(x).\n'
              'Para mais informações sobre formato consulte:\n  '
              'https://docs.python.org/pt-br/3/library/math.html?highlight=sin%20x#module-math\n'
              'Repasse todos os comandos vistos no link acima de math.função para np.função.' )
        print('-----------------------------  ENTRE COM OS DADOS  ---------------------------------' )

        F = input('Digite a função f(t,y): ')
        a = float(eval(input('Digite o extremo inferior do intervalo [a,b]: ')))
        b = float(eval(input('Digite o extremo superior do intervalo [a,b]: ')))
        alpha = float(eval(input('Digite a condição inicial y(x0): ')))
        n = int(eval(input('Digite quantidade de pontos da malha: ')))
        f = lambda t,y: eval(F)

        h = (b-a)/n
        t = a
        omega = alpha
        i=1
        print('i=%d, omega = %0.9f' % (i-1, omega))
        while i<=n:
            omega = omega + (h/2)*(f(t,omega) + f(t+h, omega + h*f(t,omega)))
            t = a + i*h
            i = i + 1
            print('i=%d, omega = %0.9f' % (i-1, omega))

        print('\n ***********************************  RESPOSTA  ***********************************\n')
        print('                     A aproximação y(%.9f) é %0.9f.                        ' % (b, omega))
        print('\n **********************************************************************************\n')
        print('             Autoria: Allan de Sousa Soares - IFBA VDC             ')
        print('Canal: https://www.youtube.com/c/MatematicaParaGenteGrande\n')
        esc = input('Digite menu para voltar ao menu princial ou aperte enter para continua: ')
        if esc == 'menu':
            fgeral()
