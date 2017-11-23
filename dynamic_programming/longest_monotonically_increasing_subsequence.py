# Give an O(n^2) time dynamic programming algorithm to find the longest
# monotonically increasing subsequence of a sequence of n numbers, i.e,
# each successive number in the subsequence is greater than its predecessor.
# For example, if the input sequence is <5, 24, 8, 17, 12, 45>, the output
# should be either <5, 8, 12, 45> or <5, 8, 17, 45>.

# Solution: Calculates the longest monotonically subsequence by constructing an array (Bottom up from i=0..n) with the longest sequence ending on each element i.
# The values are calculated using the previous calculated values in the array which gives a constant look-up time.
def longest_mono_sub(sequence_array):
    n = len(sequence_array)
    result_items_array = []
    result_array = [1]*n                # initially sequence  at position i is 1 long (if all items before x_i are greater - no increasing for this specific ending item)
    for i in range(0,n):
        if i==0:                        # If it only contains one item will stay 1 (redundant)
            result_array[i] = 1
            result_items_array.append([sequence_array[i]])
            print(result_items_array)
        else:                           # Otherwise we search for the longest sequence ending with item i, using the previously calculated result_array[j] values, where 0<j<i
            max_seq_index = find_max_seq(sequence_array[i], sequence_array[0:i], result_array[0:i])
            max_seq = []
            max_seq_length = 0
            
            if (max_seq_index >= 0):                                            # Invalid index if no prev. sequence exists => max_seq_length=1
                max_seq_length = result_array[max_seq_index]                        # copy length of previous sequence
                max_seq = list(result_items_array[max_seq_index])                   # deepcopy actual sequence of prev. items

            max_seq.append(sequence_array[i])                                   # append current item to actual sequence
            result_items_array.append(max_seq)                                  # store actual sequence
            result_array[i] = max_seq_length +1
            print(max_seq_index, result_items_array)
    return max(result_array)

# Nested loop function to check longest subsequence of all smaller previous elements
# Returns the index of the longest sequence, -1 if no item prev. item is smaller
def find_max_seq(current_element, prev_elements, prev_elemt_seq_length):
    max_seq_index = 0
    for i in range(len(prev_elements)):                                         # Iterate over longest chain from all previous elements
        if (prev_elements[i]<current_element) and (prev_elemt_seq_length[i]>prev_elemt_seq_length[max_seq_index]): # if the element is smaller than current element ending sequence and new max
            max_seq_index = i                                                   # Update index to point longest previous chain
    if (max_seq_index == 0 and prev_elements[0]>=current_element):               # If initial index (first item) is not smaller current item then all items are greater and no item exist => invalid index returned
        return -1
    else:
        return max_seq_index


# returns the maximum of a list of integers
def max(values_array):
    max_val = values_array[0]
    for i in range(0, len(values_array)):
        if values_array[i]>max_val:
            max_val = values_array[i]
    return max_val

print(longest_mono_sub([5,24,8,17,12,45]))

# Runtime analysis:
# The algorithm iterates over all O(n) elements and has a nested loop iterating over all previous O(n-1) elements using their prev. calculated max. length sequence values
# This makes a runtime of O(n^2)
