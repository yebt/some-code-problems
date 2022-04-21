
def probeAdd(array, k):
    indx = 0
    for item in array:
        indx += 1
        if ((k - item) in array[indx:]):
            return True
    return False


k = 17
array = [10, 15, 3, 7]

print(probeAdd(array, k))
