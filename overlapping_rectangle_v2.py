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
# Notes:
#     This is an improved answer. With this solution, the exact types of overlap no longer need to be defined :).
#     This solution requires the numpy package to be installed!
#     python3 -m pip install numpy
#

import numpy
import sys

# Rectangle
class Rectangle:
    def __init__(self, coordinates: list):
        # Ranges (Uses numpy to include all possibilites with one decimal place!)
        self.x_range = [round(x, 1) for x in numpy.arange(coordinates[0][0], coordinates[1][0] + .1, .1)]
        self.y_range = [round(y, 1) for y in numpy.arange(coordinates[0][1], coordinates[1][1] + .1, .1)]

# Calculate Overlapping Coordinates
def overlapping(a: Rectangle, b: Rectangle):
    # Calculate x overlap
    overlapping_x_range = []
    for n in a.x_range:
        if n in b.x_range:
            overlapping_x_range.append(n)

    # Calculate y overlap
    overlapping_y_range = []
    for n in a.y_range:
        if n in b.y_range:
            overlapping_y_range.append(n)

    # Overlap
    if len(overlapping_x_range) > 1 and len(overlapping_y_range) > 1:
        return [[overlapping_x_range[0], overlapping_y_range[0]], [overlapping_x_range[-1], overlapping_y_range[-1]]]

    # No overlap
    else:
        return [[0.0, 0.0], [0.0, 0.0]]

# Play the funky music...
if __name__ == '__main__':
    # Welcome
    print('Welcome to David Engel\'s Overlapping Rectangle Challenge!')

    try:
        # Second Rectangle Coordinates
        print('\nSecond Rectangle [[x,y], [x,y]]')
        a = Rectangle(eval(input('Enter coordinates for first rectangle: ')))

        # First Rectangle Coordinates
        print('\nFirst Rectangle [[x,y], [x,y]]')
        b = Rectangle(eval(input('Enter coordinates for second rectangle: ')))
    except:
        print('Invalid input!')
        sys.exit()

    # Calculate Overlap
    overlap = overlapping(a, b)

    # Print Result
    print('\nOverlap: '+str(overlap))
