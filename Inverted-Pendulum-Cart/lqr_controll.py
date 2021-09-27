import time
import numpy as np
from Model import CartPoleEnv

import sys
from os.path import dirname
sys.path.append(dirname(dirname(__file__)))
from Optimal_Controller.LQR import LQR

if __name__ == "__main__":
    env = CartPoleEnv()
    controller = LQR(4, 1)
    A, B = env.state_space()
    Q = np.eye(4)
    Q[0,0] = 0
    Q[1,1] = 20
    Q[2,2] = 100
    Q[3,3] = 100
    controller.update_continues_param(A, B, Q, np.array([[1]]), 0.02)
    state = env.reset()
    while True:
        action = controller.get_u(50, np.array(state).reshape(4,1))
        print(action)
        state = env.step(action)
        env.render()
        time.sleep(0.02)