#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 16:52:35 2019

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

#Iplementation of quick_sort function
def quick_sort(arr):
    quick_sort2(arr, 0, len(arr)) #recursive call of quick_sort2
    return arr

def quick_sort2(arr, beg, end):
    if end - beg > 1: #chaning if its more that 1 elemets to be sorted
        par = partition(arr, beg, end) # recusive called of partition function
        quick_sort2(arr, beg, par) #  recirsive called of quicksort2 functionright part of the array
        quick_sort2(arr, par + 1, end) # recirsive called of quicksort2 functionrsort left part of the array


def partition(arr, beg, end):
    piv = arr[beg] # initialize pivot value
    i = beg + 1  # Initialiase beg value
    j = end - 1 #  Initialiase end value

    while True: # iterate over the array
        while (i <= j and arr[i] <= piv): # comparing each element to the piv
            i += 1 # add 1
        while (i <= j and arr[j] >= piv):
            j -= 1 # substract one

        if i <= j: #comparation elemets
            arr[i], arr[j] = arr[j], arr[i] #swap it values
        else:
            arr[beg], arr[j] = arr[j], arr[beg] #swap it values
            return j


print(quick_sort(arr_200))#calling the selection_sort function
time_end = time.time() # calculate time
cal_time = time_end - time_start
formate_caltime = format(cal_time, "e") # format to scientifict notation
print(formate_caltime)
