class Lazor:
    '''
        This class estimates all possible combinations to find the solution
        Step 1: Sorting A blocks in possible 'o' positions to get all
                combinations
        Step 2: With leftover o positions, do similar combination search
                for B, C
        Step 3: Create possible combinations of A, B, C with available
                'o' positions and locked blocks within the grid
    '''

    def __init__(self, dataset1, dataset2):
        '''
        The __init__ method will utilize the dictionaries created from
        class Input and initialize all the extracted information as variables

        **Input Parameters**
            dataset1: *dict*
                The dictionary with following attributes
                size of the grid, lazors, points of intersection,
                and number of blocks (A, B, C)
            dataset2: *dict*
                The dictionary with following attributes
                size of the grid, individual lists of blocks
                and no-movement positions
        **Returns**
            None

        '''
        self.o_l = dataset1['o_l']
        self.size = dataset1['Size']
        self.lazers = dataset1['Lazers']
        self.points = dataset1['Points']
        self.A = dataset1['A']
        self.B = dataset1['B']
        self.C = dataset1['C']
        self.dataset2 = dataset2

    def __call__(self):
        '''
        The __call__ method will return the right combination
        of coordinates of different blocks

        **Input Parameters**
            None
        **Returns**
            sel_comb: *dict, list, int*
                The right combination of coordinates of different blocks
        '''
        # All possible combinations of A in 'o' positions
        o_lA = list(combinations(self.o_l, self.A))
        # For every A block
        for i_a in o_lA:
            # Sorting the available 'o' positions, A combinations
            o_l, a_comb = self.new_sort("a_comb", self.o_l, list(i_a))
            # Possible combinations of B with new o positions
            # (after A block is fixed)
            o_lB = list(combinations(self.o_l, self.B))
            # For every B block
            for i_b in o_lB:
                # Sorting the available 'o' positions, B combinations
                o_l, b_comb = self.new_sort("b_comb", self.o_l, list(i_b))
                # Possible combinations of C with new 'o' positions
                # (after A, B blocks fixed)
                o_lC = list(combinations(self.o_l, self.C))
                # For every C block
                for i_c in o_lC:
                    # Sorting the available 'o' positions, C combinations
                    o_l, c_comb = self.new_sort("c_comb", self.o_l, list(i_c))

                    # Selecting a set of different coordinates amongst
                    # all possible combinations
                    sel_comb = self.set_abc(
                        [a_comb, b_comb, c_comb], ['A', 'B', 'C'])

                    # Testing the selected combination under class Solution
                    test_comb = Solution(
                        sel_comb,
                        self.lazers,
                        self.points,
                        self.dataset2,
                        self.size)

                    # If true, return the right combination
                    # of coordinates of different blocks
                    if test_comb():
                        return sel_comb
                    # Else test the next possible combination
                    o_l, c_comb = self.rearrange(
                        c_comb, o_l, self.C, list(i_c), "C")
                o_l, b_comb = self.rearrange(
                    b_comb, o_l, self.B, list(i_b), "B")
            o_l, a_comb = self.rearrange(a_comb, o_l, self.A, list(i_a), "A")

    def set_abc(self, block_positions, name):
        '''
        This function will create a new dictionary with A, B, C
        combinations

        **Input Parameters**
            block_positions: *list, int*
                The list with positions of a specific block
            name: *list, int*
                The name of the specific block
        **Returns**
            sel_comb: *dict, list, int*
                An updated dictionary with A, B, C combinations
        '''
        sel_comb = {}
        for j in range(len(block_positions)):
            # Accessing each position
            block_position = block_positions[j]
            for i in block_position:
                # Creating a key, value pair
                sel_comb[(i[0], i[1])] = name[j]
        return sel_comb

    def new_sort(self, list_name, o_l, list_elements):
        '''
        This function will update 'o' positions list
        after every iteration in the combinations loop

        **Input Parameters**
            list_name: *str*
                The name of the specific block
            o_l: *list, int*
                The 'o' positions list
            list_elements: *list, int*
                The specific block positions (A, B, or C)

        **Returns**
            o_l: *list, int*
                The 'o' positions list
            vars()[list_name]: *variable name*
                The name of the specific block
        '''
        # Creating a list with the variable name
        vars()[list_name] = []
        # extending the list with specific block positions
        (vars()[list_name]).extend(list_elements)
        # For A, B blocks
        if not list_name == 'c_comb':
            for item in list_elements:
                # Try and except for removing elements
                try:
                    o_l.remove(item)
                except BaseException:
                    pass
        return o_l, vars()[list_name]

    def rearrange(self, block_list, o_l, number, extend_list, alphabet):
        '''
        This function will rearrange the o_list and specific block list
        by removing newly added positions. This new list will be used for
        next iteration to find the right combination

        **Input Parameters**
            block_list: *list, int*
                The list of specific block combinations with available
                'o' positions
            o_l: *list, int*
                The 'o' positions list
            number: *int*
                The number of specific blocks for every iteration
            extend_list: *list, int*
                The positions of the block (A, B, C) from all combinations
            alphabet: *str*
                The name for the specific function

        **Returns**
            o_l: *list, int*
                The updated o positions list
            block_list: *list, int*
                The updated list of specific block combinations
        '''
        # When there are specific blocks
        if number != 0:
            del block_list[-number:]
            # Updating o positions list
            if alphabet != "C":
                o_l.extend(extend_list)
        return o_l, block_list


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
                # Get the name of the blocl
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
