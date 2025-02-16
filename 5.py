def arr_multip(arr):

    result = []

    for i in range(len(arr)):
        x = 1
        for x in range(len(arr)):
            if x != 1:
                x*= arr[x]  
        result.append(x)    
    return result            

print(arr_multip([1,2,3]))  

# დროში ვერ ჩავეტიე