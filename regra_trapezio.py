import numpy as np
from geral import fgeral



def fregra_trapezio():
    while True:
        print('-----------------------------------  DESCRIÇÃO  ------------------------------------')
        print( 'Programa que aplica a Regra do Trapézio a uma função f(x) no intervalo [a,b].' )
        print('-----------------------------------  INSTRUÇÕES  -----------------------------------')
        print( '[1] Algumas funções podem estar no formato np., por exemplo sen(x) = np.sin(x).\n'
              'Para mais informações sobre formato consulte:\n  '
              'https://docs.python.org/pt-br/3/library/math.html?highlight=sin%20x#module-math\n'
              'Repasse todos os comandos vistos no link acima de math.função para np.função.' )

        print('-----------------------------  ENTRE COM OS DADOS  ---------------------------------' )

        a = float(eval(input('Digite o extremo inferior do intervalo de integração: ')))
        b = float(eval(input('Digite o extremo inferior do intervalo de integração: ')))
        n = int(input('Digite o número n de trapézios (n-1 pontos da partição): '))
        h = (b - a)/n
        x = np.linspace(a, b, n+1)
        f = eval(input('Digite a função f(x): '))
        I_trap = (h/2)*(f[0] + 2 * sum(f[1:n]) + f[n])

        print('\n ***********************************  RESPOSTA  ***********************************\n')
        print( '                 A integral de f no intervalo [%d,%d] é %0.9f.                  ' % (a,b,I_trap))
        print('\n **********************************************************************************\n')
        print('             Autoria: Allan de Sousa Soares - IFBA VDC             ')
        print('Canal: https://www.youtube.com/c/MatematicaParaGenteGrande\n')
        esc = input('Digite menu para voltar ao menu princial ou aperte enter para continuar: ')
        if esc == 'menu':
            fgeral()