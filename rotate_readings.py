"""
Reads a numpy array and creates six more rotated in iterations of 30 degrees.

-90, -60, -30, 0, 30, 60, 90, that is, where 0 is the original.
The point of this is to create training inputs for other movement commands
than the straight forward one.

1/29/2018 - Thomas Phalen
"""


def rotate(arr, angle):
    """Rotate degree-correspondant values by [angle] "degrees".

    That is, if your array is a circle, rotate it by the angle. You know.
    """
    start = int(angle / 360 * len(arr))
    return (arr[start:] + arr[:start])


def duplicate_inputs(arr, reps=7):
    """Create [reps] datasets which are rotations of [arr] and output them all.

    Outputs one array including all rotations with [arr] at the center.
    """
    angle = 180 / (reps-1)
    angles = range(-(reps-1)/2 * angle, (reps-1)/2 * angle, angle)
    rotations = []
    for i in angles:
        rotations.append(rotate(arr, angle))

    return(sum(rotations, []))
