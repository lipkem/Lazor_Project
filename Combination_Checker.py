class Solution:
    '''
        This class has functions to solve the lazor puzzle
        - Criteria: Lazer intersection with given points
        - Input: Possble combinations of blocks, lazors, points of intersection
        - Handles the functions for refract, reflect, hitting the block,
          moving lazor, position and lazor encounters
        - List of points of intersection is empty

    '''

    def __init__(self, sel_comb, lazers, points, dataset2, size):
        '''

        The __init__ method will initialize the previously generated dictionaries,
        lazors' information, size of the grid etc.

        **Input Parameters**
            sel_comb: *dict*
                The dictionary with following attributes
                size of the grid, and blocks (A, B, C)
            lazers: *list, int*
                The list of lazor positions and directions
            points: *list, int*
                The list of positions of points of intersections
            dataset2: *dict*
                The dictionary with following attributes
                size of the grid, and individual lists of blocks
                (A,B.C) and no-movement positions
            size:*list, int*
                The size of the grid for the lazor
        **Returns**
            None

        '''
        self.size = size
        self.sel_comb = sel_comb
        self.lazers = lazers
        self.points = points
        self.x = 0
        self.y = 0
        self.vx = 0
        self.vy = 0
        self.A_l = dataset2['A_l']
        self.B_l = dataset2['B_l']
        self.C_l = dataset2['C_l']

    def __call__(self):
        '''
        The __call__ method will add fixed elements into the dictionary and
        test if all POIs are intersected by the lazors

        **Input Parameters**
            None
        **Returns**
            True/False *bool*
                True if list of points of intersection (POI) is empty
        '''
        # Incoporate coordinates of fixed A blocks
        if self.A_l:
            for i in self.A_l:
                self.sel_comb[(i[0], i[1])] = 'A'
        # Incoporate coordinates of fixed B blocks
        if self.B_l:
            for i in self.B_l:
                self.sel_comb[(i[0], i[1])] = 'B'
        # Incoporate coordinates of fixed C blocks
        if self.C_l:
            for i in self.C_l:
                self.sel_comb[(i[0], i[1])] = 'C'
        # Iterating over every lazer
        for li in self.lazers:
            # Run the function
            self.move_lazor(li)

        # if list of POI is empty
        if self.points == []:
            return True
        return False

    def pos_chk(self, upd_pos):
        '''
        This function will check if the position is
        within the range of the grid

        **Input Parameters**
            upd_pos: *list, int*
                The list with x, y coordinates or positions
        **Returns**
            True/False: *bool*
                True if coordinates is within the range
        '''
        # Initializing x boundaries
        x = upd_pos[0]
        # Max x-position
        xu = self.size[0]
        # Initializing y boundaries
        y = upd_pos[1]
        # Max y-position
        yu = self.size[1]

        # True if within the range
        return x >= 0 and x < xu and y >= 0 and y < yu

    def move_lazor(self, lazer):
        '''
        This function represents the movement of lazor along its direction

        **Input Parameters**
            lazer: *list, int*
                The list with lazor position and direction
        **Returns**
            None
        '''
        self.x, self.y, self.vx, self.vy = lazer
        pos = [self.x, self.y]
        # If lazer position interesects one of POIs, remove the POI from list
        self.points = list(filter(lambda x: x != pos, self.points))
        # If direction of x-comp is negative and x-coordinate is a whole number
        if self.x.is_integer() and self.vx < 0:
            self.conditional((self.x - 1, (self.y * 2 - 1) / 2), lazer)
        # If direction of x-comp is positive and x-coordinate is a whole number
        elif self.x.is_integer() and self.vx > 0:
            self.conditional((self.x, (self.y * 2 - 1) / 2), lazer)
        # If direction of y-comp is negative and y-coordinate is a whole number
        elif not self.x.is_integer() and self.vy < 0:
            self.conditional(((self.x * 2 - 1) / 2, self.y - 1), lazer)
        # If direction of y-comp is positive and y-coordinate is a whole number
        else:
            self.conditional(((self.x * 2 - 1) / 2, self.y), lazer)

    def reflect(self, lazer):
        '''
        This function is executed if it encounters the A block
        To validate the lazor touching the blocks:
        Step 1: Check lazor direction
        Step 2: Verify the touch (Lazor - block)
        Step 3: If touch is on sides or top or bottom


        **Input Parameters**
            lazer: *List, int*
                The list with lazor positions and directions
        **Returns**
            None
        '''
        x, y, vx, vy = lazer
        # If x-coordinate is integer
        if self.x.is_integer():
            # Update position and run move_lazor() function
            self.move_lazor((x - vx, y + vy, - vx, vy))
        else:
            self.move_lazor((x + vx, y - vy, vx, - vy))

    def refract(self, lazer):
        '''
        This function is executed if it encounters the C block
        This function will encrypt any string
        Reflect section
        Step 1: Check lazor direction
        Step 2: Verify the touch (Lazor - block)
        Step 3: If touch is on sides or top or bottom

        Refract section
        Step 4: Run the move_lazor() function

        **Input Parameters**
            parameter: *int, float, optional*
                The parameter that adds itself to the previous term
        **Returns**
            None
        '''
        x, y, vx, vy = lazer
        up_x = x + vx
        up_y = y + vy
        mov_pos = (up_x, up_y, vx, vy)
        self.move_lazor(mov_pos)
        # If x-coordinate is a whole number
        if self.x.is_integer():
            mov_pos = (x - vx, y + vy, - vx, vy)
            self.move_lazor(mov_pos)
        else:
            mov_pos = (x + vx, y - vy, vx, - vy)
            self.move_lazor(mov_pos)

    def conditional(self, upd_pos, lazer):
        '''
        This function test will block (A, B or C) the lazer encounters

        **Input Parameters**
            upd_pos: *tuple, float, optional*
                The updated position in lazer direction
        **Returns**
            None: *None-type*
                If lazor position is outside the grid
                or if it encounters Block B
        '''
        # If lazor position is within the grid
        if self.pos_chk(upd_pos):
            #  If lazor position found amongst the selected combination
            if upd_pos in self.sel_comb:
                # Get the name of the block
                name = self.sel_comb[upd_pos]
                # Run reflect() function
                if name == 'A':
                    self.reflect(lazer)
                # Run refract() function
                elif name == 'C':
                    self.refract(lazer)
                # If Block B, return
                else:
                    return None
            else:
                l_upd = (self.x + self.vx, self.y + self.vy, self.vx, self.vy)
                self.move_lazor(l_upd)
        else:
            return None
