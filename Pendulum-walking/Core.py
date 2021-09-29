import numpy as np

class Controller:
    """
    LIPM controller
    """
    def __init__(self, H, LEG, Vmax, Vmin) -> None:
        self.gravity = 9.8
        self.Tc = np.math.sqrt(self.gravity/H)
        self.H = H
        self.Vtarget = Vmax
        self.Energy = self.Vtarget**2/2.0
        # self.step = step
        self.leg = LEG
        self.maxRange = np.math.sqrt(LEG**2-H**2)
        self.time_step = 0.02
 
    def update_param(self, footX, comX, comVx):
        self.Footx = footX
        self.comX = comX
        self.comVx = comVx

    def get_u(self, state):
        action = state[0]*1.2+state[-1]
        return action

        