import time
import numpy as np
from Model import CartPoleEnv

import sys
from os.path import dirname
sys.path.append(dirname(dirname(__file__)))
from Optimal_Controller.LMPC import LMPC

if __name__ == "__main__":
    env = CartPoleEnv()
    controller = LMPC(4, 1)
    A, B = env.state_space()
    Q = np.eye(4)*10
    Q[1,1] = 20
    Q[2,2] = 100
    Q[3,3] = 100
    controller.update_param(A, B, Q, np.eye(1))
    state = env.reset()
    while True:
        action = controller.get_u(15, np.array(state).reshape(4,1))
        print(action)
        state = env.step(action)
        env.render()
        time.sleep(0.02)