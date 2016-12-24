function  y = yelipseb (u0,t,p,ep,a) 

  u = bsl(u0,t,p,ep);
  y = a* [sqrt(1-(ep*ep)) * sin(u)];
  
 end
 
  %  " Esta funcion nos proporciona la componente y del vector posicion (x,y)
  %      utilizando las funciones de bessel " .   