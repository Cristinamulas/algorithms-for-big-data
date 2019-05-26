#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 17:31:00 2019

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
#implemtation of merge function
def merge(left, right):
        if not len(left) or not len(right): #chenking if both half arrays are the same lenght
                return left or right
        result = [] # final output array
        i, j = 0, 0 #indexing staring at 0
        while (len(result) < (len(left) + len(right))):#continue to interate until we use all the values of the arrays
                if left[i] < right[j]: # comparing elements
                        result.append(left[i]) #paste the left elements to the reuslt list
                        i+= 1 # go to next value
                else:
                        result.append(right[j]) # paste the right elements to the reuslt list
                        j+= 1 # go to next value

                if i == len(left) or j == len(right): #cheking for arrays wnatnt completely use up inside the while loop
                        result.extend(left[i:] or right[j:]) # adding remaining elements
                        break

        return result
#implemetation of merge_sort function
def merge_sort(arr):
        # conditinal for chenking if the array is bigger than two
        # if its smaller than 2 do not neet to sort
        if len(arr) < 2: 
                return arr

        middle = len(arr)//2 # diviede the array into 2 half
        left = merge_sort(arr[:middle]) # sort half array form 0 to middle
        right = merge_sort(arr[middle:]) # sort hafl array from middel to final

        return merge(left, right) # return both

   
print(merge_sort(arr_200)) #calling the merge_sort function
time_end = time.time() # calculate time
cal_time = time_end - time_start
formate_caltime = format(cal_time, "e") # format to scientifict notation
print(formate_caltime)  
            
                