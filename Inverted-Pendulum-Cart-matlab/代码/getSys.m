syms t x_dot theta1_dot theta2_dot m1 m2 l1 l2 x3
x = x_dot * t;
theta1 = theta1_dot * t;
theta2 = theta2_dot * t;
x2 = x - 2*l1*sin(theta1)-l2*sin(theta1+theta2);
y2 = 2*l1*cos(theta1)+l2*cos(theta1+theta2);
a = diff(x2, t);
b = diff(y2,t);
simplify(a*a + b*b);

