"""Assume that you are given a sorted array of distinct integer values A[0,...,n-1], and your task is
to figure out whether there is an index i for which A[i] = i.
- Devise a naive algorithm that performs this task in a brute force manner (i.e., with O(n) run time). Implement this
algorithm in a Python function named GetPointIndex naive().
- Devise a divide-and-conquer (DC) algorithm for this problem, which has O(logn) run time. Implement this algorithm in
a Python function named GetPointIndex DC()."""

import time
def GetPointIndex_naive(A):
    start_time=time.perf_counter() #start time measurement
    for i in range(len(A)):
        if A[i]==i:    #check if the current index is equal to its value
            return True, time.perf_counter()-start_time  #return True and elapsed time
    return False, time.perf_counter()-start_time    #return False if index not found

def GetPointIndex_DC(A):
    def pointer(left,right):
        if left>right:
            return False
        
        mid=(left+right)//2
        
        if A[mid]==mid:
            return True
        elif A[mid]>mid:
            return pointer(left,mid-1)
        else:
            return pointer(mid+1,right)
    
    start_time=time.perf_counter()  
    res=pointer(0, len(A)-1)
    return res,time.perf_counter()-start_time  

A=[-3, 0, 1, 5, 7, 9, 11]
bool_val_naive,runtime_naive=GetPointIndex_naive(A)
print(f"For Naive method: bool_val={bool_val_naive}, runtime={runtime_naive:10f}")

B=[-3, 0, 2, 5, 7, 9, 11]
bool_val_dc,runtime_dc=GetPointIndex_DC(B)
print(f"For DC method: bool_val={bool_val_dc}, runtime={runtime_dc:.10f}")
