
function x=xelipseb (u0,t,p,ep,a) 

  u = bsl(u0,t,p,ep);
  x = a* [cos(u) - ep ];
  
 end
 
 %  " Esta funcion nos proporciona la componente x del vector posicion (x,y)
 %      utilizando las funciones de bessel " .   