from collections import defaultdict
import gymnasium as gym


class TD0Prediction:
    """
    Tabular TD(0) for estimating V_pi.
    Input: policy to be evaluated. The policy is supposed to be a function whose input is observation and output is action.
    """
    def __init__(self,  env:gym.Env, policy, alpha=0.1, gamma=0.9) -> None:
        self.alpha = alpha
        self.V = defaultdict(int)
        self.env = env
        self.policy = policy
        self.gamma = gamma

    def predict(self, num_episodes:int):
        for i in range(num_episodes):
            obs, info = self.env.reset()
            done = False
            
            while not done:
                action = self.policy(obs)
                next_obs, reward, done, _, _ = self.env.step(action)
                self.V[obs] = self.V[obs] + self.alpha *(reward + self.gamma * self.V[next_obs] -  self.V[obs])
                obs = next_obs

        return self.V
    
