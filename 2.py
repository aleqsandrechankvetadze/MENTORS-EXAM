def First_Missing_Positive_Integer(arr):

    for i in range(1,len(arr)):
        if i not in arr:
            return i

print(First_Missing_Positive_Integer([1,2,3,4,5,6,8,9,10]))    