function uf = nwr(u,t,p,ep)

	 u1 = u ;
	 u2 = u1 - (f(u1,t,p,ep)/fd(u1,ep)) ;  
	 
	while (abs(u1-u2) > 0.00000000001) 
		u1 =  u2 ; 
		u2 = u1 - (f(u1,t,p,ep)/fd(u1,ep)) ;
		end 
  
  uf = u2 ;
  
end

% " Esta funcion aproxima el valor de u mediante el metodo de newton rapson " .