def get_first_missing_positive(array):
    # max term from the array
    maxNumber = 0
    # sum acom
    acom = 0
    for item in array:
        if item > 0 :
            # only the positive numbers
            if maxNumber < item:
                maxNumber = item
            acom += item
    # calculate the summation from max integer
    summation = (maxNumber * (maxNumber + 1))/2
    miss = summation - acom
    return miss if miss else maxNumber +1


print(get_first_missing_positive([3,4,1]))
print(get_first_missing_positive([3,4,-1,1]))
print(get_first_missing_positive([1,2,0]))
