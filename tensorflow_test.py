"""
Created on Thu Oct 26 12:34:47 2017.

OUDATED
@author: thomas
"""
from __future__ import print_function

# import tensorflow as tf
import numpy as np
import sys
import rotate_scans
# import matplotlib.pyplot as plt
rng = np.random

# parameters
learning_rate = .01
training_epochs = 1000
display_step = 50

scan_data = np.load(sys.argv[1])

trn_inputs_raw = []

for i in range(len(scan_data)):
    trn_inputs_raw.append([])
    for j in range(len(scan_data[i])):
        trn_inputs_raw[i].append(scan_data[i][j][2])

# Do the rotatey thing to duplicate trn_inputs in other directions
trn_inputs = rotate_scans.duplicate_inputs(trn_inputs_raw)
trn_outputs = []

output_value = []
raw_length = len(trn_inputs_raw)
for i in range(int(len(trn_inputs)/raw_length)):
    output_value = [0, 0, 0, 0, 0, 0, 0]
    output_value[i] = 1
    for j in range(raw_length):
        trn_outputs.append(output_value)
