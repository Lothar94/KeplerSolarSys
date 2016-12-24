1 ;
p=326.26 ;
t = 1:p;
x = elipse(pi,t) ;
x1 = xelipse(pi,t) ;
hold on 
y1 = yelipse(pi,t) ;
plot (t,x1)
plot (t,y1)
grind on
hold on
axis equal

% PRUEBAS