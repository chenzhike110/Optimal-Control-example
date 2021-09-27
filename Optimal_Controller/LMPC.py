import numpy as np
import cvxpy

class LMPC():
    """
    Model predict controll
    """
    def __init__(self, x_dim, u_dim) -> None:
        self.x_dim = x_dim
        self.u_dim = u_dim
        self.Q = np.eye(x_dim)
        self.R = np.eye(u_dim)
    
    def update_param(self, A, B, Q, R) -> None:
        self.A = A
        self.B = B
        self.Q = Q
        self.R = R
    
    def get_u(self, forward_time, x_now):

        x = cvxpy.Variable((self.x_dim, forward_time + 1))
        u = cvxpy.Variable((self.u_dim, forward_time))

        cost = 0.0
        constraints = []

        for t in range(forward_time):
            cost += cvxpy.quad_form(u[:, t], self.R)
            cost += cvxpy.quad_form(x[:, t], self.Q)
            constraints += [x[:, t+1] == self.A@x[:, t] + self.B@u[:, t]]
        
        constraints += [x[:, 0] == x_now.reshape(x_now.shape[0],)]
        prob = cvxpy.Problem(cvxpy.Minimize(cost), constraints)
        prob.solve(solver=cvxpy.ECOS, verbose=False)

        if prob.status == cvxpy.OPTIMAL or prob.status == cvxpy.OPTIMAL_INACCURATE:
            return u.value[:, 0]
        else:
            return np.zeros(self.u_dim)