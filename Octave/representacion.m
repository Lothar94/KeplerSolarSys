
function representacion(p,ep,a) 
t = 0:0.1:2*p;
x1 = xelipse(pi,t,p,ep,a);
y1 = yelipse(pi,t,p,ep,a);
plot (x1,y1)
end

% " Esta funcion nos representa graficamente la elipse, utilizando la aproximacion de u 
%        mediante el metodo de nwr " .