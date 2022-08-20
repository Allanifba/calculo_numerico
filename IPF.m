clc
clear all
format long

function[p] = IPF(g, p0, TOL, N)
 i = 1;
 while (i <= N)
  printf("iteração ")
  p=g(p0)
  printf('delta ')
  abs(p0-p)
  if (abs(p0-p) < TOL)
   return
  endif
  i = i + 1;
  p0 = p;
 endwhile
 printf("error: O procedimento não foi bem sucedido.")
endfunction

%IPF(g=@(x)(x^3-x+1)/30,1,10^(-3),10)