"""
Created on Thu Oct 26 12:34:47 2017.

@author: thomas
"""
from __future__ import print_function

# import tensorflow as tf
import numpy
# import matplotlib.pyplot as plt
rng = numpy.random


def txt_to_array(path):
    """Read data from text file and put it into an array."""
    infile = open(path)
    file_arr = infile.readlines()
    string_arr = []
    for i in range(0, len(file_arr)):
        strs = (file_arr[i].split("\t"))
        for i in range(0, len(strs)):
            strs[i] = str.strip(strs[i])
        string_arr.append(strs)
    return string_arr


def txt_to_trn_inputs(path):
    """Read from text file and output training inputs."""
    scans = txt_to_array(path)
    arr_out = []
    temp = []
    first = True
    for reading in scans:
        if(reading[0] == "False" or first):
            temp.append(float(reading[3]))
            first = False
        elif(reading[0] == "True"):
            arr_out.append(temp[:])
            temp.clear()
    return arr_out


# parameters
learning_rate = .01
training_epochs = 1000
display_step = 50

arr = txt_to_trn_inputs("/home/thomas/Documents/RESEARCH_SNAKES/lidar.txt")
print(arr)
