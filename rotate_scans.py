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
    angle = -angle % 360
    start = int(angle / 360 * len(arr))
    return (arr[start:] + arr[:start])


def rotate_all_scans(scans, angle):
    """Rotates every scan in the list of scans [arr] passed by [angle]."""
    out_scans = []
    for scan in scans:
        out_scans.append(rotate(scan, angle))
    return out_scans


def duplicate_inputs(arr, reps=7):
    """Create [reps] datasets which are rotations of [arr] and output them all.

    Outputs one array including all rotations with [arr] at the center.
    """
    # 180 because all outputs should be in cone/semicircle in front.
    angle = int(180 / (reps-1))
    angles = range(int(-(reps-1)/2 * angle), int((reps-1)/2 * angle)+1, angle)
    rotations = []
    for i in angles:
        rotations.append(rotate_all_scans(arr, i))

    return(sum(rotations, []))
