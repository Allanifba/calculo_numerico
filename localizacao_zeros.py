import numpy as np

while True:
    print('-----------------------------------  DESCRIÇÃO  ------------------------------------')
    print('Programa que refina um intervalo [a,b] em subintervalos menores contendo zeros de\n '
          'uma função f.')
    print('-----------------------------------  INSTRUÇÕES  -----------------------------------')
    print('[1] Algumas funções podem estar no formato np., por exemplo sen(x) = np.sin(x).\n'
          'Para mais informações sobre formato consulte:\n  '
          'https://docs.python.org/pt-br/3/library/math.html?highlight=sin%20x#module-math\n'
          'Repasse todos os comandos vistos no link acima de math.função para np.função.')
    print('-----------------------------  ENTRE COM OS DADOS  ---------------------------------')

    F = input('Digite a função f(x): ')
    a = float(eval(input('Digite o extremo inferior do intervalo [a,b]: ')))
    b = float(eval(input('Digite o extremo superior do intervalo [a,b]: ')))
    n = float(eval(input('Digite o número de subintervalos do intervalo do intervalo [a,b]: ')))
    gamma = (b - a) / n

    f = lambda x: eval(F)
    if f(a) * f(b) < 0:
        i = 0
        print('\n ***********************************  RESPOSTA  ***********************************\n')
        while a < b:
            fa = f(a)
            if fa == 0:
                print(f' {a} é um zero de f.')
            fc = f(a + gamma)
            a = a + gamma
            if fa * fc < 0:
                print(' Existe um zero no intervalo [%0.5f,%0.5f]' % (a - gamma, a))
        print('\n **********************************************************************************\n')
        print('             Autoria: Allan de Sousa Soares - IFBA VDC             ')
        print('Canal: https://www.youtube.com/c/MatematicaParaGenteGrande\n')
        esc = input('Digite qualquer tecla para continuar: ')
    
    else:
        print(' -----------------------------------  RESPOSTA  -----------------------------------')
        print(f' Não é recomendada a aplicação do Método de Localização de Zeros no intervalo [a,b]'
              f'\n pois, f(a)={f(a)} e f(b)={f(b)} tem sinas iguais.')
        print(' ----------------------------------------------------------------------------------')
        print('             Autoria: Allan de Sousa Soares - IFBA VDC             ')
        esc = input('Digite qualquer tecla para continuar: ')






