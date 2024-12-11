class ArraySorts:

    '''
     * Bubble sort is a simple sorting algorithm that repeatedly steps through
     *  the list, compares adjacent elements, and swaps them if they are in
     *  the wrong order. This process continues until no swaps are needed,
     *  indicating that the list is sorted.
     *
     * Time Complexity :
     *  Best Case: O(n) - when list is already sorted
     *  Avg Case: O(n^2)
     *  Worst Case: O(n^2)
    '''
    @staticmethod
    def bubble_sort(array):
        for outer in range(len(array) - 1):
            max_index = len(array) - outer - 1
            
            for inner in range(max_index):
                if array[inner] <= array[inner + 1]:
                    continue
            
                # Swap array[inner] and array[inner + 1]
                temp = array[inner]
                array[inner] = array[inner + 1]
                array[inner + 1] = temp