# DO *NOT* WRITE YOUR NAME TO MAINTAIN ANONYMITY FOR PLAGIARISM DETECTION

# Defines two classes, Point and NonVerticalLine.
#
# Point:
# Either no coordinate or two coordinates should be passed to __init__(),
# as floating point numbers or as integers.
# In the first case, the coordinates are set to those of the point
# at the origin.
#
# NonVerticalLine:
# No, one or two named arguments, point_1 and point_2, of type Point,
# should be passed to __init__().
# When an argument is not passed, it is set to the point at the origin.
# Both points have to determine a nonvertical line.
# Such an object can be modified by changing one point or both points
# thanks to the change_point_or_points() method.
# At any stage, the object maintains correct values for slope and intersect.


# Will be tested only when passing no, one or two arguments; moreover,
# when an argument is passed, it will be a float or an int.
class Point:
    pass
    # REPLACE PASS ABOVE WITH YOUR CODE

class PointError(Exception):
    pass


# Will be tested only when passing no, one or two arguments,
# that have to be named; moreover, when an argument is passed,
# it will be a Point object.
class NonVerticalLine:
    pass
    # REPLACE PASS ABOVE WITH YOUR CODE


class NonVerticalLineError(Exception):
    pass

