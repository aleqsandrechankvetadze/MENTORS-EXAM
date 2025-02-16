def Rotate_an_Array(arr,k):

    lengt_arr = len(arr)

    if lengt_arr == 0:
        return []
    
    k = k % lengt_arr
    if k == 0:
        return arr
    
    return arr[-k:] + arr[:-k]

print(Rotate_an_Array([1,2,3],2))