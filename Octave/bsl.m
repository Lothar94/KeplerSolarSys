function uf = bsl(u0,t,p,ep)
  h = 0 ;
	to = 0 ;
  u1 = u0 ;
  uf = (((2*pi)*(t-to))/p)+ h  ;
  n = 1 ;
  while ( abs(u1-uf) > 0.0000001)
    u1 = uf ;
    h = h + (2/n)*besselj(n*ep,0,0)*sin(((2*pi*n)*(t-to))/p) ;
    uf = (((2*pi)*(t-to))/p)+ h ;
    n = n+1 ;
    end
       
 end
 
 % " Esta funcion nos aproxima el valor de u en el instante t, mediante las funciones de bessel " 
 