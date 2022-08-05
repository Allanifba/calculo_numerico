import math
import numpy as np
from geral import fgeral


def fregra_simpson():
    while True:
        print('-----------------------------------  DESCRIÇÃO  ------------------------------------')
        print( 'Programa que aplica a Regra de Simpson a uma função f(x) no intervalo [a,b].' )
        print('-----------------------------------  INSTRUÇÕES  -----------------------------------')
        print( '[1] Considere que uma partição x1,x2,...,x(2n+1) possui 2n intervalos ou melhor, n\n'
              'parábolas. Sendo assim os valores que n assume são 1(1 parábola = 3 pontos), \n'
              '2 (2 parábolas = 5 pontos), 3 (3 parábolas = 7 pontos) etc... \n'
              ' [2] Algumas funções podem estar no formato np., por exemplo sen(x) = np.sin(x).\n'
              'Para mais informações sobre formato consulte:\n  '
              'https://docs.python.org/pt-br/3/library/math.html?highlight=sin%20x#module-math\n'
              'Repasse todos os comandos vistos no link acima de math.função para np.função.' )
        print('-----------------------------  ENTRE COM OS DADOS  ---------------------------------' )
        a = float(eval(input('Digite o extremo inferior do intervalo de integração: ')))
        b = float(eval(input('Digite o extremo inferior do intervalo de integração: ')))
        m = int(input('Digite o número n de parábolas (2n+1 pontos da partição): '))
        n = 2*m
        h = (b - a)/n
        x = np.linspace(a, b, n+1)
        f = eval(input('Digite a função f(x): '))
        I_simp = (h/3) * (f[0] + 2*sum(f[2:n-1:2]) + 4*sum(f[1:n:2]) + f[n])

        print('\n ***********************************  RESPOSTA  ***********************************\n')
        print( '       A integral de f no intervalo [%0.9f,%0.9f] é %0.9f.        ' % (a,b,I_simp))
        print('\n **********************************************************************************\n')
        print('             Autoria: Allan de Sousa Soares - IFBA VDC             ')
        print('Canal: https://www.youtube.com/c/MatematicaParaGenteGrande\n')
        esc = input('Digite menu para voltar ao menu princial ou aperte enter para continuar: ')
        if esc == 'menu':
            fgeral()
