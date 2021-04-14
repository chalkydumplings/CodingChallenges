#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort1 function below.
def insertionSort1(n, arr):

    for i in range((n-1),-1,-1):#NEED TO PUT STEP 
        # i= n-1
        
        toSort=arr[i] #second last value [0,0,1,0] 
      
        print(toSort)
        
        while arr[i-1]>toSort and i >0: #while value of interest less than value to the left switch values
            
            temp=arr[i]
            arr[i]=arr[i-1]
            print(*arr)
            arr[i-1]=temp
            i=i-1 #swap values
          
            # print("poo")
    
    # print("poo")
    print(*arr)
if __name__ == '__main__':
    n = 14

    arr = [1,3,5,9,13,22,27,35,46,51,55,83,87,23]

    insertionSort1(n, arr)
