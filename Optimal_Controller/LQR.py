from operator import inv
import numpy as np

class LQR():
    """
    Discrete LQR controller
    """
    def __init__(self, x_dim, u_dim) -> None:
        self.A = np.eye(x_dim)
        self.B = np.zeros((x_dim, u_dim))
        self.Q = np.eye(x_dim)
        self.R = np.eye(u_dim)
    
    def update_param(self, A, B, Q, R, P=None) -> None:
        self.A = A
        self.B = B
        self.Q = Q
        self.R = R
        if P is not None:
            self.P = P
        else:
            self.P = self.Q
    
    def update_continues_param(self, A, B, Q, R, T, P=None) -> None:
        self.A = A*T+np.eye(self.A.shape[0])
        self.B = B*T
        self.Q = Q
        self.R = R
        if P is not None:
            self.P = P
        else:
            self.P = self.Q
    
    def get_u(self, forward_number, x_now):
        P = self.P
        K = np.zeros((forward_number, self.A.shape[1]))
        U = np.zeros(forward_number)
        for i in range(forward_number-1, -1, -1):
            Ki = np.linalg.inv(self.R-self.B.transpose()@P@ self.B) @ self.B.transpose() @ P @ self.A
            K[i,:] = Ki
            P = self.Q + Ki.reshape(self.A.shape[1],1)@self.R@Ki + (self.A-self.B@Ki).transpose()@P@(self.A-self.B@Ki)
        for i in range(forward_number):
            U[i] = -K[i]@x_now
            x_now = self.A@x_now + self.B*U[i]
        return U[0]
    