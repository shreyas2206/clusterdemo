#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 15:53:30 2020

@author: shreyasr
"""


import torch
import numpy
import time

print("Startin nnet training... \n")

for i in range(60):
    time.sleep(1)
    print("epoch {}: loss = {}".format(i,(1/(1+i))))
    
print("Done")
