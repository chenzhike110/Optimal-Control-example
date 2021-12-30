import numpy as np

class LIPM:
    """
    LIPM based trajectory planning
    """
    def __init__(self, H, LEG) -> None:
        self.gravity = 9.8
        self.Zc = H
        self.Tc = np.math.sqrt(self.gravity/self.Zc)
        self.max_step = np.math.sqrt(LEG**2-H**2)*2.0
        self.CoM_x = 0
        self.LFoot_x = 0
        self.RFoot_x = 0
    
    def step(self, x) -> None:

