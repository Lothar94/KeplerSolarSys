
function representacionb(p,ep,a) 
t = 0:0.1:2*p;
x1 = xelipseb(pi,t,p,ep,a);
y1 = yelipseb(pi,t,p,ep,a);
plot (x1,y1)
end

% " Esta funcion nos representa graficamente la elipse, utilizando la aproximacion de u
%        mediante las funciones de bessel " .