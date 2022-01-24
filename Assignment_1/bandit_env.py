"""
Environment for the multi-armed bandit problem
"""

import numpy as np 

class bandit_env():
    """
    Initialize the multi-arm bandit environment.

    :params:
    r_mean: takes a list of reward mean
    r_stddev: takes a list of reward standard deviation

    """
    def __init__(self, r_mean, r_stddev):
        if len(r_mean) != len(r_stddev):
            raise ValueError("Reward distribution parameters (mean and variance) must be of the same length")

        if any(r <= 0 for r in r_stddev):
            raise ValueError("Standard deviation in rewards must all be greater than 0")

        self.n = len(r_mean)
        self.r_mean = r_mean
        self.r_stddev = r_stddev

    def pull(self, index_arm):
        """
        Performs the action of pulling the arm/lever of the selected bandit

        :inputs:
        index_arm: the index of the arm/level to be pulled

        :outputs:
        reward: the reward obtained by pulling tht arm (sampled from their corresponding Gaussian distribution)
        """
        reward = np.random.randn(self.r_mean[index_arm], self.r_stddev[index_arm])
        return reward