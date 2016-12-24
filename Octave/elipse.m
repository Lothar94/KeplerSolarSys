 function x = elipse(u0,t,p,ep,a)
  u = nwr(u0,t,p,ep) ;
  x = a .* [cos(u) - ep , sqrt(1- (ep*ep)) * sin(u)];
  
 end 
 
 % "Esta funcion nos da el vector (x,y) en un instante t, aproximando u mediante nwr " .