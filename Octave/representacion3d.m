function representacion3d(u0,t,p,ep,a,omega,gamma,i)
          
          t = 1:1:50 ;
          [s dim]=size(t);
          
          x = zeros (1,dim);
          y = zeros (1,dim);
          z = zeros (1,dim);
          
          for i=1:dim 
          x(i) = xposr3 (u0,t(i),p,ep,a,omega,gamma,i) ;
          y(i) = yposr3 (u0,t(i),p,ep,a,omega,gamma,i) ;
          z(i) = zposr3 (u0,t(i),p,ep,a,omega,gamma,i) 
          
          plot3(x(:),y(:),z(:))  
          
  end 