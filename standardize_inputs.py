"""Read .npy of scans and turn each scan into 200 readings.

Deletes scans with fewer than 200 readings.
"""
import numpy as np
import sys


def trim(arr, threshold):
    fuck


def standardize_inputs(inpath, outpath, threshold=200):
    """Take list of scans and manipulate so 200 readings in all scans."""
    raw_scans = np.load(inpath)
    for i, scan in enumerate(raw_scans):
        # Delete scans with less than [threshold] valid readings. default 200
        if (len(scan) < threshold):
            del raw_scans[i]
        # Do nothing for scans of exactly [threshold] readings. default 200

        # Trim down scans with more than [threshold] readings. default 200
        if (len(scan) > threshold):
            trim(scan, threshold)


if __name__ == "__main__":
    try:
        inpath = sys.argsv[1]
        outpath = sys.argsv[2]
    except IndexError:
        print("One argument required for output path.")

    standardize_inputs(inpath, outpath)
