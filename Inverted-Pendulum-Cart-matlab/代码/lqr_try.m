syms x theta1 dtheta1 theta2 dtheta2 ddtheta1 ddtheta2 dx ddx u
M=1.0;
m1=0.05;
m2=0.03;
l1=0.3;
l2=0.2;
g=9.8;
% eqns = [g*(theta1+theta2)==l2*(ddtheta1+ddtheta2), (m2*l2+m1*l1+2*m2*l1)*ddx==(4*m2*l1*l1+4*m2*l2*l2+m1*l1*l1)*ddtheta1-(m2*g*l2+m2*g*l1+2*m2*g*l1)*theta1-m2*g*l2*theta2, (M+m1+m2)*ddx==u-(m2*l1-m1*l1+m2*l2)*ddtheta1-m2*l2*ddtheta2];
eqns = [u==(27*ddx)/25 + ((3*cos(theta1 + theta2))/500 - (3*cos(theta1))/500)*ddtheta1 + ((3*cos(theta1 + theta2))/500)*ddtheta2 + (3*dtheta1^2*sin(theta1))/500 - (3*sin(theta1 + theta2)*(dtheta1 + dtheta2)^2)/500,...
    0==((3*cos(theta1 + theta2))/500 + (33*cos(theta1))/1000)*ddx - (201*ddtheta1)/10000 + ((9*sin(theta2))/2500)*ddtheta2 + (147*sin(theta1 + theta2))/2500 + (1617*sin(theta1))/5000 - (3*dtheta1*sin(theta2))/500,...
    0==(147*sin(theta1 + theta2))/2500 - (3*ddtheta2)/2500 - (3*ddtheta1)/2500 - (9*dtheta1*sin(theta2))/2500];
[ddtheta1, ddtheta2, ddx]=solve(eqns, [ddtheta1,ddtheta2,ddx]);

collect(ddtheta1, [theta1,theta2,u])
collect(ddtheta2, [theta1,theta2,u])
collect(ddx, [theta1,theta2,u])

% A = [0 1 0 0 0 0; 18767/1193 0 2891/1193 0 0 0;0 0 0 1 0 0;39690/1193 0 55566/1193 0 0 0;0 0 0 0 0 1;-259/5120 0 -7/80 0 0 0];
% B = [0; 6500/3579; 0; -6500/3579; 0; 3350/3579];
% Q = diag([1000, 50, 1000, 50, 10, 100]);
% R = 1;
% N = [0;0;0;0;0;0];
% rank(ctrb(A,B))
% [K,S,e] = lqr(A,B,Q,R,N)
% 
