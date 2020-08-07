#
# David Engel
#
# Challenge: Overlapping Rectangle
#
# Instructions:
#
#   Given two parameters that represent rectangles that may overlap with each other, write a function that returns the overlapping rectangle.
#
#   The inputs to this function are 2 rectangles, each represented by a 2-Dimensional array.
#   A 2-D array representing a rectangle should contain 2 arrays, each containing 2 numbers, that represent 2 points on the rectangle.
#   The first point represents the bottom-left corner of the rectangle, and the second point represents the top-right corner of the rectangle.
#
#   The output of this function must take the same form as an input rectangle, a 2-D array that represents the overlapping rectangle.
#   Here again, the first point is the bottom-left point of the overlapping rectangle and the second point is the top-right point of the overlapping rectangle.
#
#    ______
#   |      |
#   |  A __|____
#   |___|██|    |
#       |   B   |
#       |_______|
#
# Example:
#
#     Input 1: [ [2.0, 1.0], [6.0, 5.0] ]
#     Input 2: [ [4.0, 3.0], [7.0, 6.0] ]
#     Output: [ [4.0, 3.0], [6.0, 5.0] ]
#
# Note: If the input rectangles do not overlap, your function should return [ [0.0, 0.0], [0.0, 0.0] ].
#
# Example:
#
#     Input 1: [ [7.0, 7.0], [9.0, 15.0] ]
#     Input 2: [ [4.0, 3.0], [5.0, 6.0] ]
#     Output: [ [0.0, 0.0], [0.0, 0.0] ]
#
# Goals:
#
#    Using a language of your choice, the goal is to have a working function that will be able to output the desired results against a number of test inputs.
#    Utilize the runtime provided for your choice of language to run your function against a set of test inputs.
#

# Rectangle
class Rectangle:
    def __init__(self, coordinates: list):
        # Bottom Left
        self.bl = {
            'x': coordinates[0][0],
            'y': coordinates[0][1]
        }
        # Top Right
        self.tr = {
            'x': coordinates[1][0],
            'y': coordinates[1][1]
        }

# Calculate Overlapping Coordinates
def overlapping(a: Rectangle, b: Rectangle):
    # 1.    ______
    #      |      |
    #  ____|_  B  |
    # |    |_|____|
    # |  A   |
    # |______|
    if a.bl['x'] < b.bl['x'] < a.tr['x'] < b.tr['x'] and a.bl['y'] < b.bl['y'] < a.tr['y'] < b.tr['y']:
        return [[b.bl['x'], b.bl['y']], [a.tr['x'], a.tr['y']]]
    # 2.
    #  ______
    # |      |
    # |  A __|____
    # |___|__|    |
    #     |   B   |
    #     |_______|
    elif a.bl['x'] < b.bl['x'] < a.tr['x'] < b.tr['x'] and b.bl['y'] < a.bl['y'] < b.tr['y'] < a.tr['y']:
        return [[b.bl['x'], a.bl['y']], [a.tr['x'], b.tr['y']]]
    # 3.    ______
    #      |      |
    #  ____|_  A  |
    # |    |_|____|
    # |  B   |
    # |______|
    elif b.bl['x'] < a.bl['x'] < b.tr['x'] < a.tr['x'] and b.bl['y'] < a.bl['y'] < b.tr['y'] < a.tr['y']:
        return[[a.bl['x'], a.bl['y']], [b.tr['x'], b.tr['y']]]
    # 4.
    #  ______
    # |      |
    # |  B __|____
    # |___|__|    |
    #     |   A   |
    #     |_______|
    elif b.bl['x'] < a.bl['x'] < b.tr['x'] < a.tr['x'] and a.bl['y'] < b.bl['y'] < a.tr['y'] < b.tr['y']:
        return [[a.bl['x'], b.bl['y']], [b.tr['x'], a.tr['y']]]
    # 5.
    #       ______
    #  ____|_     |
    # |    | |    |
    # |  A | | B  |
    # |____|_|    |
    #      |______|
    elif a.bl['x'] < b.bl['x'] < a.tr['x'] < b.tr['x'] and b.bl['y'] < a.bl['y'] < a.tr['y'] < b.tr['y']:
        return [[b.bl['x'], a.bl['y']], [a.tr['x'], a.tr['y']]]
    # 6.
    #     ______
    #    |   A  |
    #  __|______|__
    # |  |______|  |
    # |      B     |
    # |____________|
    elif b.bl['x'] < a.bl['x'] < b.tr['x'] > a.tr['x'] and b.bl['y'] < a.bl['y'] < b.tr['y'] < a.tr['y']:
        return [[a.bl['x'], a.bl['y']], [a.tr['x'], b.tr['y']]]
    # 7.
    #  ______
    # |    __|____
    # |   |  |    |
    # | B |  | A  |
    # |   |__|____|
    # |______|
    elif b.bl['x'] < a.bl['x'] < b.tr['x'] < a.tr['x'] and b.bl['y'] < a.bl['y'] < a.tr['y'] < b.tr['y']:
        return [[a.bl['x'], a.bl['y']], [b.tr['x'], a.tr['y']]]
    # 8.
    #  ____________
    # |      B     |
    # |   ______   |
    # |__|______|__|
    #    |   A  |
    #    |______|
    elif b.bl['x'] < a.bl['x'] < a.tr['x'] < b.tr['x'] and a.bl['y'] < b.bl['y'] < a.tr['y'] < b.tr['y']:
        return [[a.bl['x'], b.bl['y']], [a.tr['x'], a.tr['y']]]
    # 9.
    #  ______
    # |    __|____
    # |   |  |    |
    # | A |  | B  |
    # |   |__|____|
    # |______|
    elif a.bl['x'] < b.bl['x'] < a.tr['x'] < b.tr['x'] and a.bl['y'] < b.bl['y'] < b.tr['y'] < a.tr['y']:
        return [[b.bl['x'], b.bl['y']], [a.tr['x'], b.tr['y']]]
    # 10.
    #  ____________
    # |      A     |
    # |   ______   |
    # |__|______|__|
    #    |   B  |
    #    |______|
    elif a.bl['x'] < b.bl['x'] < b.tr['x'] < a.tr['x'] and b.bl['y'] < a.bl['y'] < b.tr['y'] < a.tr['y']:
        return [[b.bl['x'], a.bl['y']], [b.tr['x'], b.tr['y']]]
    # 11.
    #       ______
    #  ____|_     |
    # |    | |    |
    # |  B | | A  |
    # |____|_|    |
    #      |______|
    elif b.bl['x'] < a.bl['x'] < b.tr['x'] < a.tr['x'] and a.bl['y'] < b.bl['y'] < b.tr['y'] < a.tr['y']:
        return [[a.bl['x'], b.bl['y']], [b.tr['x'], b.tr['y']]]
    # 12.
    #     ______
    #    |   B  |
    #  __|______|__
    # |  |______|  |
    # |      A     |
    # |____________|
    elif a.bl['x'] < b.bl['x'] < b.tr['x'] < a.tr['x'] and a.bl['y'] < b.bl['y'] < a.tr['y'] < b.tr['y']:
        return [[b.bl['x'], b.bl['y']], [b.tr['x'], a.tr['y']]]
    # 13.
    #  ____________
    # | A ______   |
    # |  |   B  |  |
    # |  |______|  |
    # |____________|
    elif a.bl['x'] < b.bl['x'] < b.tr['x'] < a.tr['x'] and a.bl['y'] < b.bl['y'] < b.tr['y'] < a.tr['y']:
        return [[b.bl['x'], b.bl['y']], [b.tr['x'], b.tr['y']]]
    # 14.
    #  ____________
    # | B ______   |
    # |  |   A  |  |
    # |  |______|  |
    # |____________|
    elif b.bl['x'] < a.bl['x'] < a.tr['x'] < b.tr['x'] and b.bl['y'] < a.bl['y'] < a.tr['y'] < b.tr['y']:
        return [[a.bl['x'], a.bl['y']], [a.tr['x'], a.tr['y']]]
    # No overlap
    else:
        return [[0, 0], [0, 0]]

# Play the funky music...
if __name__ == '__main__':
    # Welcome
    print('Welcome to David Engel\'s Overlapping Rectangle Challenge!')

    # First Rectangle Coordinates
    print('\nFirst Rectangle [[x,y], [x,y]]')
    a = Rectangle(eval(input('Enter coordinates for first rectangle: ')))

    # Second Rectangle Coordinates
    print('\nSecond Rectangle [[x,y], [x,y]]')
    b = Rectangle(eval(input('Enter coordinates for second rectangle: ')))

    # Calculate Overlap
    overlap = overlapping(a, b)

    # Print Result
    print('\nOverlap: '+str(overlap))
