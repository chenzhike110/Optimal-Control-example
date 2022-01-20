from mujoco_py import load_model_from_path, MjSim, MjViewer
import numpy as np
import os
from gym import spaces
import time

class inverted_pendulum_env():
    """
        Inverted pendulum environment
    """
    def __init__(self) -> None:
        model_path = os.path.dirname(__file__)+"/inverted_pendulum.xml"
        self.model = load_model_from_path(model_path)
        self.sim = MjSim(self.model)
        self.data = self.sim.data
        self.viewer = MjViewer(self.sim)
        self.skip_frame = 5

        self._set_action_space()
        
        # random start
        action = self.action_space.sample()
        self.step(action)
        action = np.zeros_like(action)
        self.step(action)
    
    def _set_action_space(self):
        bounds = self.model.actuator_ctrlrange.copy().astype(np.float32)
        low, high = bounds.T
        self.action_space = spaces.Box(low=low, high=high, dtype=np.float32)
        return self.action_space

    def observation(self):
        jointPos = self.sim.data.sensordata
        return jointPos
    
    def render(self):
        self.viewer.render()

    def step(self, action):
        self.sim.data.ctrl[:] = action
        self._simulate()
    
    def _simulate(self):
        for i in range(self.skip_frame):
            self.sim.step()
    
    def control(self):
        # write your code here
        observation = self.observation()
        action = 0.2
        self.step(action)

if __name__ == "__main__":
    env = inverted_pendulum_env()
    while True:
        env.render()
        env.control()