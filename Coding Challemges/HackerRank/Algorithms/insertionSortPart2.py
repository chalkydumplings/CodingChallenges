#!/bin/python3

import math
import os
import random
import re
import sys

# pretty sure this is just plain jane insertion sort
#Why does it work from front to back and fron to back iteration the same CONCEPTUALIZATION CRAZY

def insertionSort2(n, arr):

    for x in range(1,n): #up to but not inclduing n
        #skip the first index

        varOfInterest=arr[x]


        while varOfInterest < arr[x-1] and x>0:

            arr[x-1],arr[x]=arr[x],arr[x-1]
   
            x=x-1
        
    print(*arr)


if __name__ == '__main__':
    n =6
    arr = [1,4,3,5,6,2]

    insertionSort2(n, arr)
