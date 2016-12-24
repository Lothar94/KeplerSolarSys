
 function x = xelipse(u0,t,p,ep,a)
 
  u = nwr(u0,t,p,ep);
  x = a* [cos(u) - ep ];
  
 end 
 
 %  " Esta funcion nos proporciona la componente x del vector posicion (x,y)
 %      mediante el metodo de newton rapson " .  
 