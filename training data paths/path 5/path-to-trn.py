"""
Created on Thu Oct 26 12:34:47 2017.

@author: thomas
"""

import numpy as np
import sys
import rotate_scans

scan_data = np.load(sys.argv[1])

trn_inputs_raw = []

for i in range(len(scan_data)):
    trn_inputs_raw.append([])
    for j in range(len(scan_data[i])):
        trn_inputs_raw[i].append(scan_data[i][j][2])

# Do the rotatey thing to duplicate trn_inputs in other directions
trn_inputs = np.asarray(rotate_scans.duplicate_inputs(trn_inputs_raw))
trn_outputs = []

output_value = []
raw_length = len(trn_inputs_raw)
for i in range(int(len(trn_inputs)/raw_length)):
    output_value = [0, 0, 0, 0, 0, 0, 0]
    output_value[i] = 1
    for j in range(raw_length):
        trn_outputs.append(output_value)

trn_outputs = np.asarray(trn_outputs)

shuffle_index = np.arange(trn_inputs.shape[0])
np.random.shuffle(shuffle_index)
trn_inputs = trn_inputs[shuffle_index]
trn_outputs = trn_outputs[shuffle_index]

np.save('trn_inputs.npy', trn_inputs)
np.save('trn_outputs.npy', trn_outputs)
