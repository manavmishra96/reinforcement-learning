"""
Definition of the Warehouse Agent environment
"""

class WarehouseAgent():
    def __init__(self):
        """
        Initializing the environment
        """
        self.GRID_DIM = [6,7]

        self.agent_position = [1,2]

        self.box_location = [4,3]
        self.goal_location = [3,1]

     
    def reset(self):
        """Function to reset the environment at the end of each episode to its initial state configuration

        Returns:
            state: the state of the environment reset to its initial conditions
        """
        pass
    
    def step(self, action):
        """Function to control and evaluate the agents' action

        Args:
            action: pass on the action which the agent needs to take at that time step

        Returns:
            new_state: the new state agent reaches after taking the action
            reward: the reward obtained on taking the action
            done: boolean value to determine if episode terminating condition is reached
        """
        pass
    
    def render(self):
        """Function to get the simulation of the warehouse agent system 
        """
        pass



