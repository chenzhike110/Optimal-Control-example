import numpy as np
import time
from scipy.optimize import minimize

class MPC():
    """
    Model predict controll
    """
    def __init__(self, x_dim, u_dim, model) -> None:
        self.model = model
        self.x_dim = x_dim
        self.u_dim = u_dim
        self.Q = np.eye(x_dim)
        self.R = np.eye(u_dim)
    
    def update_param(self, Q, R) -> None:
        self.Q = Q
        self.R = R
    
    @staticmethod
    def objective(u_hat, self, x_now, forward_time):
        obj = 0.0
        for t in range(forward_time):
            obj += u_hat[t] * self.R * u_hat[t]
            x_now = self.model.model(x_now, u_hat[t])
            obj += x_now.transpose()@self.Q@x_now
        return obj.flatten()
            
    def get_u(self, forward_time, x_now):
        u_hat0 = np.zeros((self.u_dim, forward_time))
        start = time.time()
        solution = minimize(self.objective, u_hat0, (self, x_now, forward_time), method='SLSQP')
        u_hat = solution.x
        print("use time: ", time.time()-start)
        return u_hat[0]