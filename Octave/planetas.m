function planetas()
    t = input (" Introduzca un tiempo, y 0 para salir : "  ) ;
    while ( t != 0 ) 
 
       planeta = input ( " Introduzca el nombre del planeta : " , "s") ;
  
       entrar = 1 ;

        switch  (planeta)
                                                  % DATOS DE LOS PLANETAS
         case "mercurio"
              a = 0.387 ;
              p =  87.97 ;
              ep = 0.206 ;
              omega = 47.14 ;
              gamma = 75.90 ;
              i = 7 ;
    
         case "venus"
              a = 0.723 ;
              p = 224.7 ;
              ep = 0.007 ;
              omega = 75.78 ;
              gamma = 130.15 ;
              i = 3.59 ;
         case "tierra"  
              a = 1 ;
              p = 365.26 ;
              ep = 0.017 ; 
              omega = 0 ;
              gamma = 101.22 ;
              i =  0 ;
         case "marte"  
              a = 1.524 ;
              p = 686.98 ;
              ep = 0.093 ;
              omega = 48.78 ;
              gamma = 334.22 ;
              i = 1.85 ;
         case "jupiter"
              a = 5.203 ;
              p = 4332.6;
              ep = 0.048 ; 
              omega = 99.44 ;
              gamma = 12.72 ;
              i = 1.31 ;
         case "saturno"  
              a = 9.546 ;
              p = 10759 ;
              ep = 0.056 ; 
              omega = 112.79 ;
              gamma = 91.09 ;
              i = 2.5 ;
         case "urano"  
              a = 19.20 ;
              p = 30687 ;
              ep = 0.047; 
              omega = 73.48 ;
              gamma = 169.05 ;            
              i = 0.77 ; 
         case "neptuno"  
              a = 30.09 ;
              p = 60784 ;
              ep = 0.009 ;
              omega = 130.68 ;
              gamma = 43.83 ;
              i = 1.78 ;
         %case "pluton"        Por la controversia de considerarlo un planeta.
         %   a = 39439;
         %   p = 90474.902 ;
         %   ep = 0.25 ;
    
         otherwise

             printf ("El nombre del planeta no esta registrado \n") ;   
             entrar = 0  ;
             t = 0 ;
             
    endswitch
    
    if  entrar == 1 
    % Valor de u en el instante (t) , por el metodo de newton rapson .
      nw = nwr (pi,t,p,ep) ;
      printf ("\n\nEl valor de u, en el instante t, mediante el metodo de newton rapson es : %d \n\n ",nw) ;
    % Valor de u en el instante (t) , mediante las funciones de bessel .
      b = bsl (pi,t,p,ep) ;
      printf ("\nEl valor de u, en el instante t, mediante las funciones de bessel es : %d \n\n ",b) ;
    % diferencia
      di = diferencia (pi,t,p,ep) ;
      printf ("\nLa diferencia entre ambos valores es : %d \n\n", di ) ;
      
   
    %Posicion en el tiempo t
      printf("La posicion del planeta en el instante t, mediante NWR es:        \n")
      x = elipse(pi,t,p,ep,a)
      printf("\nLa posicion del planeta en el instante t, mediante Bessel es:        \n")
      x = elipseb(pi,t,p,ep,a)
   
    %Pintamos la gráfica
     % representacionb(p,ep,a)
   
    %Calculamos la energia en el instante t
    %Cuando el planeta tiene un periodo demasiado grande la energia es aprox 0:
    %switch (letra)
      
     % case "neptuno"
      %  printf("La energia es aprox 0 \n\n")
        
      %case "urano"
       %  printf("La energia es aprox 0 \n\n")
         
      %case "pluton"
       %  printf("La energia es aprox 0 \n\n")
         
      %otherwise
        e = energia(p,a);
        printf("La energia en el instante t es: %d \n\n", e)
        
    %endswitch
    
    %Comparamos Bessel y Newton Rapshon graficamente .
     % comparacion(pi,p,ep,a)
   
    %Calculamos la distancia al sol en el instante t .
      d = distanciasol(t,p,ep,a);
      
      printf("La distancia al sol en el instante t es: %d \n\n", d)
      printf("Posicion en R3 \n\n" )
      te = 1:50
      posr3(pi,te,p,ep,a,omega,gamma,i)
     %posr3(pi,t,p,ep,a,omega,gamma,i) 
     %xposr3(pi,t,p,ep,a,omega,gamma,i)
     %yposr3(pi,t,p,ep,a,omega,gamma,i)
     % zposr3(pi,t,p,ep,a,omega,gamma,i)
      
      %representacion3d(pi,t,p,ep,a,omega,gamma,i)
      
      printf(":::::::::::::::::::::::::::::::::::::::::::: \n\n") 
   
      t = input (" Introduzca un tiempo, y 0 para salir : "  ) ;
      
      
   end
   end
   
      
 end
          
          