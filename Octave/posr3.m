function x3 = posr3 (u0,t,p,ep,a,omega,gamma,i)
         x = elipseb(u0,t,p,ep,a) ;
         x = [x 0] ;
         omegab = gamma - omega ;
         A = [1 0 0 ; 0 cos(i) -sin(i) ; 0 sin(i) cos(i)] ;
         B = [cos(omegab) -sin(omegab) 0 ; sin(omegab) cos(omegab) 0 ; 0 0 1] ;
         
         y=[x(1);x(2);x(3)] ;
         x3 = A * (y) ;
         x3 = B * (x3) ;
         
         
end          
          