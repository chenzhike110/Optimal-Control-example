syms x theta1 dtheta1 theta2 dtheta2 ddtheta1 ddtheta2 dx ddx u
% M m1 m2 g l1 l2
M=1.0;
m1=0.05;
m2=0.03;
l1=0.3;
l2=0.2;
g=9.8;
eqns = simplify(m1*l1*sin(theta1)*dtheta1*dx-2*m1*l1*l2*dtheta1*sin(theta2)+m2*dx*(l2*sin(theta1+theta2)*(dtheta1+dtheta2)...
    +2*l1*dtheta1*sin(theta1))+m1*g*l1*sin(theta1)+m2*g*(2*l1*sin(theta1)+l2*sin(theta1+theta2))...
    -((m1+4*m2)*l1*l1*ddtheta1-(m1+2*m2)*l1*(cos(theta1)*ddx-sin(theta1)*dx*dtheta1)+4*m2*l2*l2*ddtheta1-2*m2*l1*l2*sin(theta2)*ddtheta2...
    -m2*l2*(cos(theta1+theta2)*ddx-sin(theta1+theta2)*(dtheta1+dtheta2)*dx)));
collect(eqns, [ddx, ddtheta1, ddtheta2])
eqns = simplify((M+m1+m2)*ddx+(m2-m1)*l1*(cos(theta1)*ddtheta1-sin(theta1)*dtheta1*dtheta1)...
    +m2*l2*(cos(theta1+theta2)*(ddtheta1+ddtheta2)-sin(theta1+theta2)*(dtheta1+dtheta2)*(dtheta1+dtheta2)));
collect(eqns, [ddx, ddtheta1, ddtheta2])
eqns = simplify(-2*m2*l1*l2*dtheta1*sin(theta2)+m2*g*l2*sin(theta1+theta2)-m2*l2*l2*(ddtheta1+ddtheta2));
collect(eqns, [ddx, ddtheta1, ddtheta2])
