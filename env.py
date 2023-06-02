"""
Environment 
"""

class Env1:
    def __init__(self):
        self.x_range = (-3, 33)
        self.y_range = (-10, 10)
        self.obs_boundary = self.obs_boundary(self)
        self.obs_circle = self.obs_circle()
        self.obs_rectangle = self.obs_rectangle()

    @staticmethod
    def obs_boundary(self):
        obs_boundary = [
            [self.x_range[0] - 1, self.y_range[0] - 1, 1, self.y_range[1] - self.y_range[0] + 2],
            [self.x_range[0] - 1, self.y_range[1], self.x_range[1] - self.x_range[0] + 2, 1],
            [self.x_range[0] - 1, self.y_range[0] - 1, self.x_range[1] - self.x_range[0] + 2, 1],
            [self.x_range[1], self.y_range[0] - 1, 1, self.y_range[1] - self.y_range[0] + 2]
        ]
        return obs_boundary

    @staticmethod
    def obs_rectangle():
        
        obs_rectangle = []
        
        return obs_rectangle

    @staticmethod
    def obs_circle():

        obs_cir = [
            [10, -1, 3],
            [20, 1, 3]
        ]
       
        return obs_cir
    
class Env2:
    def __init__(self):
        self.x_range = (-3, 33)
        self.y_range = (-10, 10)
        self.obs_boundary = self.obs_boundary(self)
        self.obs_circle = self.obs_circle()
        self.obs_rectangle = self.obs_rectangle()

    @staticmethod
    def obs_boundary(self):
        obs_boundary = [
            [self.x_range[0] - 1, self.y_range[0] - 1, 1, self.y_range[1] - self.y_range[0] + 2],
            [self.x_range[0] - 1, self.y_range[1], self.x_range[1] - self.x_range[0] + 2, 1],
            [self.x_range[0] - 1, self.y_range[0] - 1, self.x_range[1] - self.x_range[0] + 2, 1],
            [self.x_range[1], self.y_range[0] - 1, 1, self.y_range[1] - self.y_range[0] + 2]
        ]
        return obs_boundary

    @staticmethod
    def obs_rectangle():
        """
        obs_rectangle = [[8.5, -10, 2, 14],
                         [21.5, -4, 2, 14]]
        """
        obs_rectangle = [[8.5, -10, 2, 13.5],
                        [22, -4, 2, 14]]
        
        
        return obs_rectangle

    @staticmethod
    def obs_circle():
        """
        obs_cir = [
            [10, -1, 3],
            [20, 1, 3]
        ]
        """
        obs_cir = []
        return obs_cir
