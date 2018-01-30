"""
Created on Thu Oct 26 12:34:47 2017.

@author: thomas
"""
from __future__ import print_function

# import tensorflow as tf
import numpy as np
import sys
import rotate_scans
# import matplotlib.pyplot as plt
rng = np.random

scan_data = np.load(sys.argv[1])

trn_inputs_raw = []

for i in range(len(scan_data)):
    trn_inputs_raw.append([])
    for j in range(len(scan_data[i])):
        trn_inputs_raw[i].append(scan_data[i][j][2])

# Do the rotatey thing to duplicate trn_inputs in other directions
trn_inputs = rotate_scans.duplicate_inputs(trn_inputs_raw)

# parameters
learning_rate = .01
training_epochs = 1000
display_step = 50
