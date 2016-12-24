function comparacion(u0,p,ep,a)
    
    t = 0:2:2*p ; 
    hold on
    plot (xelipse(u0,t,p,ep,a),yelipse(u0,t,p,ep,a))
    plot (xelipseb(u0,t,p,ep,a),yelipseb(u0,t,p,ep,a))

end

% "Representa simultaneamente la grafica de la elipse,mediante aprox. nwr y funciones de bessel " . 