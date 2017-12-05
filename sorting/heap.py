# Simple priority queue implemented as heap
# Operations:
# 1) Insert in O(log n)
# 2) Extract-Min in O(log n)
# Implemented with internal array:
#   parent: i/2
#   left-child: i*2
#   right-child: i*2+1

class Heap:
    def __init__(self):
        self.heap = []

    def insert_array(self, array):
        for i in range(0,len(array)):
            self.insert(array[i])

    # Insert lowest level free spot, bubble up if parent is greater
    def insert(self, element):
        # append end of array
        self.heap.append(element)
        # index of the last item
        i = len(self.heap)-1
        # bubble up until root or greater than parent
        while (i/2 >= 0 and self.heap[i/2] > self.heap[i]):
            self.swap(i/2,i)
            i = i/2

    def length(self):
        return len(self.heap)

    # Swap two items in the heap
    def swap(self,i,j):
        tmp = self.heap[j]
        self.heap[j] = self.heap[i]
        self.heap[i] = tmp

    def extract_min(self):
        heap_len = len(self.heap)
        if (heap_len < 1):
            return None
        # return min-item (root)
        root = self.heap[0]

        # copy last item to heap & reduce by last item
        self.heap[0] = self.heap[heap_len-1]
        self.heap.pop()
        heap_len = len(self.heap)
        smaller = True

        # bubble down item
        i = 1   # position of item equals index+1
        while (smaller):
            # right child  (smaller parent & left child)
            if i*2+1 <= heap_len and self.heap[i*2] < self.heap[i-1] and self.heap[i*2] < self.heap[i*2-1]:
                self.swap(i*2,i-1)
                i = i*2+1
            # only left child
            elif i*2 <= heap_len and self.heap[i*2-1] < self.heap[i-1]:
                self.swap(i*2-1,i-1)
                i = i*2
            # done
            else:
                smaller = False

        return root

heap = Heap()
heap.insert_array([8,2,3,5,6,10])
for i in range(0,6):
    print(heap.extract_min())
