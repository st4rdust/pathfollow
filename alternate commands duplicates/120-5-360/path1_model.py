"""
Created on Thu Oct 26 12:34:47 2017.

@author: thomas
"""

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout

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

model = Sequential()

model.add(Dense(30, input_dim=len(trn_inputs[0]),
                kernel_initializer='random_normal', activation='sigmoid'))
# model.add(Dense(3, kernel_initializer='uniform', activation='softmax'))
model.add(Dropout(0.4))
model.add(Dense(7, activation='softmax'))

# sgd = optimizers.SGD(lr=0.1, momentum=0.0, decay=0.0, nesterov=False)
model.compile(loss='categorical_crossentropy', optimizer='rmsprop',
              metrics=['accuracy'])

model.fit(trn_inputs, trn_outputs, epochs=150, validation_split=.15,
          batch_size=4, verbose=2)

model.save('path1_model_final.h5')
np.save('trn_inputs.npy', trn_inputs)
np.save('trn_outputs.npy', trn_outputs)
