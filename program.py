from basics.data_structs.singly_linked_list import SinglyLinkedList
from basics.data_structs.doubly_linked_list import DoublyLinkedList
from basics.algorithms.array_sorts import ArraySorts
from easy.two_sum import TwoSum
from medium.add_two_numbers import AddTwoNumbers
from medium.longest_substring import LongestSubstring

print("\nDSA coverage & LeetCode solutions!\n")

# region PRIVATE METHODS
def _display_int_array(array):   
    output_str = "[ "

    for num in array:
        output_str += f"{num}, "

    output_str = output_str[:-2] + " ]"
    print(output_str)
#endregion

# region DATA STRUCTS
print("\nDATA STRUCTURES:\n")

# Singly Linked List
print("\nSingly Linked List:")
single_linked_list = SinglyLinkedList()
sample_data = [1, 2, 3, 4, 5]

for num in sample_data:
    single_linked_list.insert(num)

single_linked_list.display()

# Doubly Linked List
print("\nDoubly Linked List:")
double_linked_list = DoublyLinkedList()
sample_data = [1, 2, 3, 4, 5]

for num in sample_data:
    double_linked_list.insert(num)

double_linked_list.display_forward_traversal()
double_linked_list.display_reverse_traversal()

# Circular Linked List
# Skip List
# Binary Search Tree
# Trie Tree
# Graph
# Red-Black Tree

# endregion

# region SORTS
print("\nSORTS:\n")

print("\nBubble Sort:")
bubble_array = [21, 73, 676, 3, 89, 9, 102, 203]
_display_int_array(bubble_array)
ArraySorts.bubble_sort(bubble_array)
_display_int_array(bubble_array)

# Selection Sort
# Insertion Sort
# Merge Sort
# Quick Sort
# Heap Sort
# Counting Sort
# Radix Sort
# Bucket Sort

# endregion

#region LEETCODE
print("\nLEETCODE:\n")

# 1. Two Sums
TwoSum.run()

# 2. Add Two Numbers
AddTwoNumbers.run()

# 3. Longest Substring Without Repeating Characters
LongestSubstring.run()

#endregion

print("Thanks!")