
def get_large_sum_no_adjaset(array):
    first = 0
    second = 0
    lenArray = len(array)
    for i in range(1, lenArray+1):
        indx = (lenArray - i)
        newSum = max(array[indx] + second, first)
        second = first
        first = newSum

    return first
    
print(get_large_sum_no_adjaset([2, 4, 6, 2, 5]))
print(get_large_sum_no_adjaset([5, 1, 1, 5]))

