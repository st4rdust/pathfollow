"""Read .npy of scans and turn each scan into 200 readings.

Deletes scans with fewer than 200 readings.
"""
import numpy as np
import sys


def trim(arr, threshold):
    """Trims off extra readings so there are [threshold].

    Read array with degree measures / other value pairs and remove entries
    so that only the closest to 360/threshold remain. You know just trims it.
    """
    step = len(arr)/threshold
    out_arr = []
    for i in range(threshold):
        out_arr.append(arr[int(i*step)-1])
    return out_arr


def standardize_inputs(inpath, outpath, threshold=180):
    """Take list of scans and manipulate so 200 readings in all scans."""
    raw_scans = np.load(inpath)
    out_scans = []
    for i, scan in enumerate(raw_scans):
        # Delete scans with less than [threshold] valid readings. default 200
        # (Just don't add scan to output array)

        # Pass scan right through to output if it has 200 readings.
        if(len(scan) == threshold):
            out_scans.append(scan)

        # Trim down scans with more than [threshold] readings. default 200
        if (len(scan) > threshold):
            out_scans.append(trim(scan, threshold))
    np.save(outpath, np.array(out_scans))


if __name__ == "__main__":
    try:
        inpath = sys.argv[1]
        outpath = sys.argv[2]
    except IndexError:
        print("One argument required for output path.")
    threshold = None
    if(len(sys.argv) > 3):
        threshold = int(sys.argv[3])

    if threshold is None:
        standardize_inputs(inpath, outpath)
    else:
        standardize_inputs(inpath, outpath, threshold)
