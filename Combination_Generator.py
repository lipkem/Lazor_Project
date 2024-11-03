# Import packages
from itertools import combinations
from PIL import Image, ImageDraw #will only need this if we decide to generate an image
import time


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
        class Input and initialize all the extracted information as variables.
        #THESE NEED TO BE MODIFIED IN ORDER TO WORK WITH MARK'S CODE

        **Input Parameters** 
        #MIGHT NEED TO DESIGN CODE TO GET THESE TWO DATASETS AFTER MARKS CODE
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
        self.o_l = dataset1['o_l'] #Defines grid
        self.size = dataset1['Size'] #Defines size of grid as [x ,y]
        self.lazers = dataset1['Lazers'] #Defines positions and directions of lazers
        self.points = dataset1['Points'] #Defines points of intersections
        self.A = dataset1['A'] #Defines fixed reflect block
        self.B = dataset1['B'] #Defines fixed opaque block
        self.C = dataset1['C'] #Defines fixed refract block
        self.dataset2 = dataset2

#THESE NEED TO BE MODIFIED IN ORDER TO WORK WITH MARK'S CODE
    
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




