
list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17];

# start = start of the sub-list
#end = end of the sub-list
# element = value of parent node (middle for balanced)
# Input: sorted list: structure algorithm for a tree with middle element as root (balanced).
def listToTree(start,end):
    element = int(start + (end-start)/2)
    if (start>end):
        #print("Debug", list[element-1], "n:", n , "i:", i)
        return
    listToTree(start, element-1)
    print("Element", list[element], "start:", start, "end:", end)
    listToTree(element+1, end)

listToTree(0, len(list)-1)
