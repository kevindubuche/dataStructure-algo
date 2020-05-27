# funct merge 2 arrays by sorting them
import time
startTime = time.time()
def merge(ar1, ar2, len1, len2):
    i, j =0,0
    res =[]
    while i <len1 and j < len2:
        if ar1[i] < ar2[j]:
            res.append(ar1[i])
            i +=1
        else :
            res.append(ar2[j])
            j +=1
    if i == len(ar1): res.extend(ar2[j:])
    else            : res.extend(ar1[i:])
    return res

def mergeSort(a):
    if len(a) <= 1 : return a
    mid=len(a)//2
    left, right = mergeSort(a[:mid]), mergeSort(a[mid:])
    return merge(left, right, len(left), len(right))

#function to generate random array
def generateArray(size=10, max=50):
    from random import randint
    return [randint(0,max) for _ in range(size)]

a=generateArray()
print(a)
print(mergeSort(a))
print("--%s sec--"%(time.time()-startTime))