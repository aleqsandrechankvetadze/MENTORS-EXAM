def find_majority(arr):

    if len(arr) % 2 == 0:
        length_divide = len(arr)//2
    else:
        length_divide = len(arr)//2 + 1

    for i in arr:
        if arr.count(i) >= length_divide:
            return i
               
print(find_majority([2,2,2,2,2,2,4,4,5,3,4]))    