function d = diferencia (uo,t,p,ep)
    
    n = nwr (uo,t,p,ep) ;
    b = bsl (uo,t,p,ep) ;
    d = abs (n - b ) ;
    
 end
 
 % "Calcula la diferencia entre el valor de u obtenido mediante nwr y el obtenido por las funciones
 %     de bessel" .