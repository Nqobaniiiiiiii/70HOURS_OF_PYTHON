arr = [-2,3,-1,5,4,-3,0]
def partition(arr,l,r):
    pivot = arr[r]
    i  = l -1
    for j from l upto r-1:
         if arr[j]< pivot:
             i +=1
             swap arr[i] and arr[j]
    swap arr[i+ 1] and arr[r]
    return i +1
        