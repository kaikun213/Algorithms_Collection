print("test")
mylist = [2,23,43,2,1,10,58]
print ('[%s]' % ', '.join(map(str, mylist)))
mylist = mergesort(mylist)
print ('[%s]' % ', '.join(map(str, mylist)))

def mergesort(l):
    print('mergesort', l) # debug printout
    if (len(l) <= 1):
        return l
    # divide and conquer
    left = mergesort(l[:int(len(l)/2)])
    right = mergesort(l[int(len(l)/2):])
    return merge(left, right)

def merge(l1, l2):
    print('merge l1', l1) # debug printout
    print('merge l2', l2)
    i = 0
    j = 0
    result = []
    # Go through both lists and take smaller item for the new list
    while (i<len(l1) and j<len(l2)):
        if (l1[i] <= l2[j]):
            result.append(l1[i])
            i += 1
        else:
            result.append(l2[j])
            j += 1
    # Not very nice solution, but after comparing both lists, one list is not at the end yet
    while (i<len(l1)):
        result.append(l1[i])
        i += 1
    while (j<len(l2)):
        result.append(l2[j])
        j += 1
    return result
