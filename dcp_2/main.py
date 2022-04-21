def operate_array(array):
    multComulate = 1
    for item in array:
        multComulate *= item
    newArr = [ (multComulate/item) for item in array]
    return newArr
    
def operate_array_nodiv(array):
    # try use dinamic programation
    newArr = []
    for i in range(len(array)):
        premult = 1
        for j in range(len(array)):
            if i != j:
                premult *= array[j]
        newArr.append(premult)

    return newArr

print('YD', operate_array([1, 2, 3, 4, 5]))
print('ND', operate_array_nodiv([1, 2, 3, 4, 5]))
print('YD', operate_array([3, 2, 1]))
print('ND', operate_array_nodiv([3, 2, 1]))
