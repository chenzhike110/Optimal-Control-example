import time
from Model import CartPoleEnv

if __name__ == "__main__":
    env = CartPoleEnv()
    env.reset()
    while True:
        env.step(0.1)
        env.render()
        time.sleep(0.1)