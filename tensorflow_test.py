#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 12:34:47 2017

@author: thomas
"""
from __future__ import print_function

import tensorflow as tf
import numpy
import matplotlib.pyplot as plt
rng = numpy.random
import io
    
#parameters
learning_rate = .01
training_epochs = 1000
display_step = 50   

arr = txt_to_array("/home/thomas/Documents/RESEARCH_SNAKES/lidar.txt")
print(arr)