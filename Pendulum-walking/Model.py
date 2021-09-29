from os import stat
import numpy as np
from gym.utils import seeding
from gym.envs.classic_control import rendering

class InvertedPendulumEnv():
    """
    Description:
        A inverted pendulum is attached by an un-actuated joint to the ground, which moves along
        a frictionless track. The pendulum starts upright, with changable joint position and the goal is to
        prevent it from falling over by increasing and reducing the cart's
        velocity.
    Source:
        This environment corresponds to the version of the cart-pole problem
        described by Barto, Sutton, and Anderson
    Observation:
        Type: Box(4)
        Num     Observation              
        1       Pole position x             
        2       Pole velocity x
        3       Pole angle
        4       Pole anguler velocity
        5       Foot position x
    Actions:
        Type: change foot pos
    """

    metadata = {"render.modes": ["human", "rgb_array"], "video.frames_per_second": 50}

    def __init__(self):
        self.gravity = 9.8
        self.maxlength = 1.0
        self.torso_h = 0.8
        self.time_step = 0.02

        self.changefoot = 0
        self.foot_x = 0
        self.kinematics_integrator = "euler"

        self.x_threshold = 2.4

        self.viewer = None
        self.state = None

        self.fell = False
    
        self.seed()

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]
    
    def step(self, action=None):
        last_state = self.state.copy()
        if action is not None:
            self.state[0] -= (action-self.foot_x)
            self.foot_x = action
            self.state[4] = self.foot_x
        
        if abs(self.state[0]) > np.math.sqrt(self.maxlength**2-self.torso_h**2):
            theta_last = np.math.atan2(last_state[0], np.math.sqrt(self.maxlength**2-last_state[0]**2))
            theta_acc = self.gravity*np.math.sin(theta_last)/self.maxlength
            if self.state[3] == 0:
                self.state[3] = self.state[1] * np.math.cos(theta_last)
            if abs(self.state[2]) < np.math.pi/2.0:
                self.state[3] += theta_acc * self.time_step
                self.state[2] += self.state[3] * self.time_step
                self.state[0] = np.math.sin(self.state[2]) * self.maxlength
            else:
                self.state[2] = self.state[2]/abs(self.state[2])*np.math.pi/2.0
        else:
            if self.kinematics_integrator == "euler":
                self.state[0] += self.time_step*self.state[1]
                xacc = self.gravity/self.torso_h*self.state[0]
                self.state[1] += xacc*self.time_step
            else:
                xacc = self.gravity/self.torso_h*self.state[0]
                self.state[1] += xacc*self.time_step
                self.state[0] += self.time_step*self.state[1]
            self.state[2] = np.math.atan2(self.state[0], self.torso_h)
            self.length = np.math.sqrt(self.state[0]**2+self.torso_h**2)
            
        return np.array(self.state, dtype=np.float32)

    def reset(self):
        self.state = self.np_random.uniform(low=-0.05, high=0.05, size=(5,))
        self.length = np.sqrt(self.torso_h**2+self.state[0]**2)
        self.state[2] = np.math.atan2(self.state[0],self.torso_h)
        self.state[3] = 0
        self.state[4] = self.foot_x
        return np.array(self.state, dtype=np.float32)

    def render(self, mode="human"):
        screen_width = 600
        screen_height = 400

        world_width = self.x_threshold * 2
        scale = screen_width / world_width
        polewidth = 10.0
        carty = 100  # TOP OF CART
        polelen = scale * self.length

        if self.viewer is None:

            self.viewer = rendering.Viewer(screen_width, screen_height)
            l, r, t, b = (
                -polewidth / 2,
                polewidth / 2,
                polelen,
                0,
            )
           
            pole = rendering.FilledPolygon([(l, b), (l, t), (r, t), (r, b)])
            pole.set_color(0.8, 0.6, 0.4)
            self.poletrans = rendering.Transform()
            self.poletrans.set_translation(screen_width / 2.0, carty)
            pole.add_attr(self.poletrans)
            self.viewer.add_geom(pole)
            poleCore = rendering.make_circle(polewidth*2)
            poleCore.set_color(0.1, 0.6, 0.4)
            self.poleCoretrans = rendering.Transform()
            self.poleCoretrans.set_translation(0, self.length*scale)
            poleCore.add_attr(self.poleCoretrans)
            poleCore.add_attr(self.poletrans)
            self.viewer.add_geom(poleCore)
            self.axle = rendering.make_circle(polewidth / 2)
            self.axle.add_attr(self.poletrans)
            self.axle.set_color(0.5, 0.5, 0.8)
            self.viewer.add_geom(self.axle)
            self.track = rendering.Line((0, carty+self.torso_h*scale), (screen_width, carty+self.torso_h*scale))
            self.track.set_color(255, 0, 0)
            self.viewer.add_geom(self.track)
            self.groud = rendering.Line((0, carty), (screen_width, carty))
            self.groud.set_color(0, 0, 0)
            self.viewer.add_geom(self.groud)

            self._pole_geom = pole

        if self.state is None:
            return None

        # Edit the pole polygon vertex
        pole = self._pole_geom
        l, r, t, b = (
            -polewidth / 2,
            polewidth / 2,
            polelen,
            0,
        )
        pole.v = [(l, b), (l, t), (r, t), (r, b)]

        self.poletrans.set_rotation(self.state[2])
        self.poleCoretrans.set_translation(0, self.length*scale)
        return self.viewer.render(return_rgb_array=mode == "rgb_array")

    def close(self):
        if self.viewer:
            self.viewer.close()
            self.viewer = None