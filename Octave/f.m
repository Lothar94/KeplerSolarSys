function  y = f(u,t,p,ep)
	to = 0 ;
	y = u - ep * sin(u) - ((2*pi)*(t-to))/p ;
	
end

% Funcion f .