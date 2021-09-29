import time
from Model import InvertedPendulumEnv
from Core import Controller

if __name__ == "__main__":
    env = InvertedPendulumEnv()
    controller = Controller(0.8, 1.0, 0.2, 0.0)
    state = env.reset()
    while True:
        # action = controller.get_u(state)
        state = env.step(None)
        env.render()
        time.sleep(0.02)