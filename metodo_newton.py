import numpy as np

while True:
    print('-----------------------------------  DESCRIÇÃO  ------------------------------------')
    print('Programa que aplica o Método de Newton a uma função f em busca de um zero desta a \n'
          'partir de um valor incial x0.')
    print('-----------------------------------  INSTRUÇÕES  -----------------------------------')
    print('[1] Algumas funções podem estar no formato n., por exemplo sen(x) = np.sin(x).\n'
          'Para mais informações sobre formato consulte:\n  '
          'https://docs.python.org/pt-br/3/library/math.html?highlight=sin%20x#module-math\n'
          'Repasse todos os comandos vistos no link acima de math.função para np.função.')
    print('-----------------------------  ENTRE COM OS DADOS  ---------------------------------')

    F = input('Digite a função f(x): ')
    DF = input('Digite a derivada de f: ')
    p0 = float(eval(input('Digite o valor incial x0: ')))
    tol = float(eval(input('Digite a tolerância: ')))

    f = lambda x: eval(F)
    df = lambda x: eval(DF)

    if df(p0) != 0:
        i = 0
        delta = float('inf')
        while tol < delta:
            p = p0 - f(p0) / df(p0)
            i = i + 1
            delta = abs(p0 - p)
            print('n=%d, p = %0.9f e delta = %0.9f' % (i, p, abs((p - p0))))
            p0 = p

        print('\n ***********************************  RESPOSTA  ***********************************\n')
        print('             Obtemos o zero p = %0.9f com precisão %0.9f.             ' % (p, delta))
        print('\n **********************************************************************************\n')
        print('             Autoria: Allan de Sousa Soares - IFBA VDC             ')
        print('Canal: https://www.youtube.com/c/MatematicaParaGenteGrande\n')

        esc = input('Digite menu para voltar ao menu princial ou aperte enter para continuar: ')
        if esc == 'menu':
            fgeral()
    else:
        print(' -----------------------------------  RESPOSTA  -----------------------------------')
        print(f'         O Método de Newton não pode ser aplicado pois f´(x0) = {df(p0)}.         ')
        print(' ----------------------------------------------------------------------------------')
        print('             Autoria: Allan de Sousa Soares - IFBA VDC             ')
        print('Canal: https://www.youtube.com/c/MatematicaParaGenteGrande\n')

        esc = input('Digite menu para voltar ao menu princial ou aperte enter para continuar: ')
        if esc == 'menu':
            fgeral()

