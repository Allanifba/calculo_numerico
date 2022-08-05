import numpy as np
from geral import fgeral


def fmetodo_secante():
    while True:
        print('-----------------------------------  DESCRIÇÃO  ------------------------------------')
        print( 'Programa que aplica o Método da Secante na obtenção de um zero p de uma função f\n'
              'pertencente ao interval [a,b].' )
        print('-----------------------------------  INSTRUÇÕES  -----------------------------------')
        print( '[1] Algumas funções podem estar no formato n., por exemplo sen(x) = np.sin(x).\n'
              'Para mais informações sobre formato consulte:\n  '
              'https://docs.python.org/pt-br/3/library/math.html?highlight=sin%20x#module-math\n'
              'Repasse todos os comandos vistos no link acima de math.função para np.função.' )

        print('-----------------------------  ENTRE COM OS DADOS  ---------------------------------' )
        F = input('Digite a função f: ')
        a = float(eval(input('Digite o extremo inferior do intervalo [a,b]: ')))
        b = float(eval(input('Digite o extremo superior do intervalo [a,b]: ')))
        tol = float(input('Digite a tolerância: '))

        f = lambda x: eval(F)
        if f(a)*f(b)<0:
            i = 1
            s0 = f(a)
            s1 = f(b)
            delta = float('inf')
            while tol<delta:
                p = b - s1*(b-a)/(s1-s0)
                i=i+1
                delta = abs(b-p)
                a=b
                s0=s1
                b=p
                s1=f(p)
                print('i=%d, p = %0.9f e delta = %0.9f' % (i,p,delta))
            print('\n ***********************************  RESPOSTA  ***********************************\n')
            print( '             Obtemos o zero p = %0.9f com precisão %0.9f.               ' % (p, delta))
            print('\n **********************************************************************************\n')
            print('             Autoria: Allan de Sousa Soares - IFBA VDC             ')
            print('Canal: https://www.youtube.com/c/MatematicaParaGenteGrande\n')
            esc = input('Digite menu para voltar ao menu princial ou aperte enter para continuar: ')
            if esc == 'menu':
                fgeral()
        else:
            print( ' -----------------------------------  RESPOSTA  -----------------------------------')
            print(f'  Não é conveniente aplicarmos o Método da Bisseção pois \n'
                           f'        f(a) = {f(a)} e f(b) = {f(b)}\n'
                  f'  não possuem sinais contários.')
            print( ' ----------------------------------------------------------------------------------')
            print('             Autoria: Allan de Sousa Soares - IFBA VDC             ')
            print('Canal: https://www.youtube.com/c/MatematicaParaGenteGrande\n')

            esc = input('Digite menu para voltar ao menu princial ou aperte enter para continuar: ')
            if esc == 'menu':
                fgeral()


