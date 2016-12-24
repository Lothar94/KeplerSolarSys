 function y = yelipse(u0,t,p,ep,a) 
 
  u = nwr(u0,t,p,ep) ;
  y = a* [sqrt(1-(ep*ep)) * sin(u)];
  
 end 
  
 %  " Esta funcion nos proporciona la componente y del vector posicion (x,y)
 %      mediante el metodo de newton rapson " .  