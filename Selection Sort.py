#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 17:48:42 2019

@author: cristinamulas
"""
import numpy as np
import random
import time

def create_array (x,y):
    randon_sample = random.sample(range(x), y)# creat an list of ramdon mumbers
    array = np.array(randon_sample) # convert a list into an array
    return array
arr_20 = create_array(21,20) #call the function to creat an array of 20 elements
arr_100 = create_array(101,100) ##call the function to creat an array of 100 elements
arr_200 = create_array(201,200)#call the function to creat an array of 20 elements
#print(arr_20)
#print(arr_100)
print(arr_200)


time_start = time.time()  # calulate time

#Iplementation of selection_sort function
def selection_sort(arr):
    for i in range(len(arr)): #iterates over the array
        ind = i #index = value
        for j in range(i + 1, len(arr)):#iterates over the unsorted part of the array
            if arr[ind] > arr[j]: #compare 
                ind = j
        arr[i], arr[ind] = arr[ind], arr[i] # swich the item in place
   
    return arr
print(selection_sort(arr_200)) #calling the selection_sort function
time_end = time.time() # calculate time
cal_time = time_end - time_start
formate_caltime = format(cal_time, "e") # format to scientifict notation
print(formate_caltime)

