"""
Created 05/28/18 by Thomas Phalen.

Creates and visualizes confusion matrix for loaded ANN.
"""

from keras.models import load_model
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sn
import numpy as np
import sys


trn_inputs = np.load('trn_inputs.npy')
trn_outputs = np.load('trn_outputs.npy')
model = load_model(sys.argv[1])
predictions = model.predict(trn_inputs)
for pred in predictions:
    max = 0
    index = 0
    for i in range(len(pred)):
        if pred[i] > max:
            max = pred[i]
            index = i
    for i in range(len(pred)):
        if i == index:
            pred[i] = 1
        else:
            pred[i] = 0

cm = confusion_matrix(trn_outputs.argmax(axis=1),
                      predictions.argmax(axis=1))
total_correct = 0

for i in range(len(cm[0])):
    total_correct += cm[i][i]

total_within_1 = total_correct
total_within_1 += (cm[0][1]) + cm[len(cm[0])-1][len(cm[0])-2]
for i in range(len(cm[0])-2):
    total_within_1 += cm[i+1][i]
    total_within_1 += cm[i+1][i+2]

print("Total measurements: ", len(predictions))
print("Total correct: ", total_correct, " / ", total_correct/len(predictions))
print("Total within one angle-step: ", total_within_1, " / ",
      total_within_1/len(predictions))

cm_dataframe = pd.DataFrame(cm, range(7), range(7))
plt.figure(figsize=(10, 7))
sn.set(font_scale=1.4)  # for label size
sn.heatmap(cm_dataframe, annot=True, annot_kws={"size": 12}, fmt='g')
plt.show()
