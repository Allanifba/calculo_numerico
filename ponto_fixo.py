import numpy as np

while True:
    print('-----------------------------------  DESCRIÇÃO  ------------------------------------')
    print('Programa que aplica o Método do Ponto Fixo na obtenção de um zero p de uma função g\n'
          'partir de um valor incial x0.')
    print('-----------------------------------  INSTRUÇÕES  -----------------------------------')
    print('[1] Algumas funções podem estar no formato n., por exemplo sen(x) = np.sin(x).\n'
          'Para mais informações sobre formato consulte:\n  '
          'https://docs.python.org/pt-br/3/library/math.html?highlight=sin%20x#module-math\n'
          'Repasse todos os comandos vistos no link acima de math.função para np.função.')
    print('-----------------------------  ENTRE COM OS DADOS  ---------------------------------')

    G = input('Digite a função de ponto fixo g(x): ')
    p0 = float(eval(input('Digite o valor incial x0: ')))
    tol = float(eval(input('Digite a tolerância: ')))

    g = lambda x: eval(G)

    i = 0
    delta = float('inf')
    while tol < delta:
        p = g(p0)
        i = i + 1
        delta = abs(p0 - p)
        print('n=%d, p = %0.9f e delta = %0.9f' % (i, p, abs((p - p0))))
        p0 = p
    print('\n ***********************************  RESPOSTA  ***********************************\n')
    print('              Obtemos o zero p = %0.9f com precisão %0.9f.              ' % (p, delta))
    print('\n **********************************************************************************\n')
    print('             Autoria: Allan de Sousa Soares - IFBA VDC             ')
    print('Canal: https://www.youtube.com/c/MatematicaParaGenteGrande\n')
    
    esc = input('Digite Enter para continuar: ')
    
