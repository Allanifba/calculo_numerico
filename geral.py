#Incluir o polinômio_triplo após consertar o erro

from colorama import Fore, Style
print('\nProgramas referentes à disciplina Cálculo Numérico do Instituto Federal de Educação,\n'
      'Ciência e Tecnologia da Bahia - Campus Vitória da Conquista\n'
      'Autoria: Allan de Sousa Soares')
print('Canal: https://www.youtube.com/c/MatematicaParaGenteGrande')

continuar = input('\nAperte enter para continuar: ')
print('\n')

def fgeral():
    from localizacao_zeros import flocalizacao_zeros
    from metodo_bisseccao import fmetodo_bisseccao
    from metodo_ponto_fixo import fmetodo_ponto_fixo
    from metodo_newton import fmetodo_newton
    from metodo_secante import fmetodo_secante
    from zeros_polinomio import fzeros_polinomio
    from interpolacao import finterpolacao
    from ajuste_linear import fajuste_linear
    from ajuste_exponencial import fajuste_exponencial
    from polinomio_triplo import fpolinomio_triplo
    from linear_quadratico_exponencial import flinear_quadratico_exponencial
    from regra_trapezio import fregra_trapezio
    from regra_simpson import fregra_simpson
    from quadratura_gaussiana import fquadratura_gaussiana
    from metodo_euler import fmetodo_euler
    from metodo_ponto_medio import fmetodo_ponto_medio
    from metodo_euler_modificado import fmetodo_euler_modificado
    from metodo_heun import fmetodo_heun
    from runge_kutta_4 import frunge_kutta_4
    from eliminacao_gaussiana import feliminacao_gaussiana
    from decomposicao_LU import fdecomposicao_LU
    from metodo_jacobi import fmetodo_jacobi
    from metodo_gauss_seidel import fmetodo_gauss_seidel
    from condicional import fcondicional

    print(' ------------------------ Equações Com Uma Variável -----------------------\n'
          ' 1 para aplicar o Método de Localização de zeros\n'
          ' 2 para aplicar o Método da Bissecção\n'
          ' 3 para aplicar o Método do Ponto Fixo\n'
          ' 4 para aplicar o Método de Newton\n'
          ' 5 para aplicar o Método da Secante\n'
          ' 6 para aplicar o Método de Delimitação de Zeros de Um Polinômio\n'
          ' ------------------------ Interpolação Polinomial -------------------------\n'
          ' 7 para obter os coeficientes do Polinômio Interpolador, avaliá-lo em um\n'
          '   valor e esboçar seu gráfico\n'
          ' -------------------------- Teoria da Aproximação -------------------------\n'
          ' 8 para obter o ajuste linear via Mínimos Quadrados\n'
          ' 9 para obter o ajuste exponencial via Mínimos Quadrados\n'
          ' 10 para o obter um comparativo gráfico entre os modelos de ajuste linear, \n'
          '   quadrático e exponencia via Mínimos Quadrados\n'
          ' ------------------------------- Integração -------------------------------\n'
          ' 11 para aplicar a Regra do Trapézio\n'
          ' 12 para aplicar a Regra de Simpson\n'
          ' 13 para aplicar Quadratura Guassiana\n'
          ' -------------------- Equações Diferenciais Ordinárias --------------------\n'
          ' 14 para aplicar o Método de Euler\n'
          ' 15 para aplicar o Método do Ponto Médio\n'
          ' 16 para aplicar o Método de Euler Modificado\n'
          ' 17 para aplicar o Método de Heun\n'
          ' 18 para aplicar o Método de Runge-Kutta de Ordem 4\n'
          ' --------------------------- Sistemas Lineares ----------------------------\n'
          ' 19 para aplicar o Método da Eliminação Gaussiana\n'
          ' 20 para aplicar o Método da Decomposição LU\n'
          ' 21 para aplicar o Método de Jacobi\n'
          ' 22 para aplicar o Método de Gauss-Seidel\n'
          ' 23 para calcular o Número Condicional de uma matriz'
          '\n --------------------------------------------------------------------------')



    escolha = int(input('\n Digite o valor correspondente a alguma das opções acima e aperte enter: '))

    if escolha == 1:
        flocalizacao_zeros()
    if escolha == 2:
        fmetodo_bisseccao()
    if escolha == 3:
        fmetodo_ponto_fixo()
    if escolha == 4:
        fmetodo_newton()
    if escolha == 5:
        fmetodo_secante()
    if escolha == 6:
        fzeros_polinomio()
    if escolha == 7:
        finterpolacao()
    if escolha == 8:
        fajuste_linear()
    if escolha == 9:
        fajuste_exponencial()
    if escolha == 10:
        flinear_quadratico_exponencial()
    if escolha == 11:
        fregra_trapezio()
    if escolha == 12:
        fregra_simpson()
    if escolha == 13:
        fquadratura_gaussiana()
    if escolha == 14:
        fmetodo_euler()
    if escolha == 15:
        fmetodo_ponto_medio()
    if escolha == 16:
        fmetodo_euler_modificado()
    if escolha == 17:
        fmetodo_heun()
    if escolha == 18:
        frunge_kutta_4()
    if escolha == 19:
        feliminacao_gaussiana()
    if escolha == 20:
        fdecomposicao_LU()
    if escolha == 21:
        fmetodo_jacobi()
    if escolha == 22:
        fmetodo_gauss_seidel()
    if escolha == 23:
        fcondicional()


fgeral()

