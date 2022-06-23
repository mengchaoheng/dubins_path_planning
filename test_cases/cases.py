from math import pi


class TestCase:
    """ Provide some test cases for a 10x10 map. """

    def __init__(self):

        # _pos = [x,y,yaw]
        # self.start_pos = [4.6, 2.4, 0]
        # self.end_pos = [1.6, 8, -pi/2]

        # for GIIM project
        self.start_pos = [7, 0.7, 0]
        self.end_pos = [5, 5.5, pi/2]

        # for car.py
        self.start_pos2 = [1, 1, 0]
        self.end_pos2 = [6, 8, pi]

        # for dubins_path.py
        self.start_pos3 = [4, 4, 0]
        self.end_pos3 = [4, 8, 1.2*pi]

        # each one of obs have to be [start_x, start_y, long in x, width in y]
        self.obs = [
            # [2, 3, 6, 0.1],#origin
            # [2, 3, 0.1, 1.5],
            # [4.3, 0, 0.1, 1.8],
            # [6.5, 1.5, 0.1, 1.5],
            # [0, 6, 3.5, 0.1],
            # [5, 6, 5, 0.1],#


            [0, 0, 10, 0.1],# ouside 
            [9.9, 0, 0.1, 10],
            [0, 9.9, 10, 0.1],
            [0, 0, 0.1, 10],#

            # [1.6, 1.6, 2.8, 0.1],# test
            # [4.3, 1.6, 0.1, 6.8],
            # [1.6, 8.3, 2.8, 0.1],
            # [1.6, 1.6, 0.1, 6.8],#

            # [5.9, 1.6, 2.4, 0.1],# test
            # [8.3, 1.6, 0.1, 6.8],
            # [5.9, 8.3, 2.4, 0.1],
            # [5.9, 1.6, 0.1, 6.8],#

            [1.6, 1.6, 2.8, 6.8],# for GIIM project
            [5.9, 1.6, 2.4, 6.8],#
            
        ]
