syms c_1 c_2 c_3 a_1 a_2 a_3 b_1 b_2 b_3
B = [0; c_1; 0; c_2; 0; c_3];
A = [0 1 0 0 0 0; a_1 0 b_1 0 0 0;0 0 0 1 0 0;a_2 0 b_2 0 0 0;0 0 0 0 0 1;a_3 0 b_3 0 0 0];
simplify(det([B A*B A^2*B A^3*B A^4*B A^5*B]))
