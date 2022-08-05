# Programa que esboça o gráfico de até 5 funções no intervalo [a,b]
import math
import numpy as np
import matplotlib.pyplot as plt
print('------------------------------------------------------------------------------------')
print('Programa que exibe os gráficos de até 5 funções em um intervalor [a,b].')
print('------------------------------------------------------------------------------------')
print('Instruções de uso:\n'
      '[1] Algumas funções podem estar no formato n., por exemplo sen(x) = np.sin(x).\n'
      'Para mais informações sobre formato consulte:\n  '
      'https://docs.python.org/pt-br/3/library/math.html?highlight=sin%20x#module-math\n'
      'Repasse todos os comandos vistos no link acima de math.função para np.função.\n'
      '[2]Caso f(x) = k, k constante, digite 0*x+k .')

while True:
    print('------------------------------------------------------------------------------------')
    while True:
        try:
            quant = int(input('Digite a quantidade de funções que quer ver o gráfico (máximo 5): '))
            break
        except:
            print('Esta não é uma entrada válida. Digite novamente.')
    while True:
        try:
            a = float(input('Digite o extremo inferior do intervalo [a,b]: '))
            break
        except:
            print('Esta não é uma entrada válida. Digite novamente.')
    while True:
        try:
            b = float(input('Digite o extremo superior do intervalo [a,b]: '))
            break
        except:
            print('Esta não é uma entrada válida. Digite novamente.')
    x = np.linspace(a, b)
    if quant >= 1:
        while True:
            try:
                def f(x):
                    return eval(input('Digite f(x) = '))
                plt.plot(x, f(x))
                break
            except:
                print('Esta não é uma entrada válida. Digite novamente')
    if quant >= 2:
        while True:
            try:
                def g(x):
                    return eval(input('Digite g(x) = '))


                plt.plot(x, g(x))
                break
            except:
                print('Esta não é uma entrada válida. Digite novamente')
    if quant >= 3:
        while True:
            try:
                def h(x):
                    return eval(input('Digite h(x) = '))


                plt.plot(x, h(x))
                break
            except:
                print('Esta não é uma entrada válida. Digite novamente')
    if quant >= 4:
        while True:
            try:
                def r(x):
                    return eval(input('Digite r(x) = '))


                plt.plot(x, r(x))
                break
            except:
                print('Esta não é uma entrada válida. Digite novamente')
    if quant >= 5:
        while True:
            try:
                def s(x):
                    return eval(input('Digite s(x) = '))


                plt.plot(x, s(x))
                break
            except:
                print('Esta não é uma entrada válida. Digite novamente')

    plt.title(input('Digite o título do gráfico: '))
    plt.xlabel(input('Digite a legenda do eixo x: '))
    plt.ylabel(input('Digite a legenda do eixo y: '))
    print('------------------------------------------------------------------------------------')
    print('             Autoria: Allan de Sousa Soares - IFBA VDC             ')
    print('Canal: https://www.youtube.com/c/Matem%C3%A1ticaParaGenteGrande')
    plt.grid()  # Exibe a grade
    plt.show()  # Exibe o gráfico


