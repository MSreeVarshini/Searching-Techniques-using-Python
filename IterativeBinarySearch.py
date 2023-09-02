# Iterative Binary Search
'''Iterative binary search is a search algorithm used to efficiently find a target element in a sorted list. It operates iteratively, repeatedly dividing the search space in half until the target element is found or it is determined that the element does not exist in the list. Here are the complexities associated with iterative binary search in Python:

1. Time Complexity:
   - Worst-case time complexity: O(log n)
   - Average-case time complexity: O(log n)
   - Best-case time complexity: O(1)

   The time complexity of iterative binary search is logarithmic (base 2). It reduces the search space by half in each iteration, leading to efficient search times even for large datasets. The best-case time complexity occurs when the target element is found at the middle position, resulting in a constant time of O(1).

2. Space Complexity:
   - Space complexity: O(1)

   Iterative binary search uses a constant amount of extra memory, regardless of the size of the input list. This makes its space complexity O(1), as it doesn't rely on additional data structures or recursive function calls.

3. Advantages:
   - Highly efficient for large sorted datasets.
   - Guarantees a logarithmic time complexity, which is significantly faster than linear search for large datasets.
   - Consumes minimal memory, making it suitable for embedded systems or situations where memory usage is a concern.
   - Easier to implement iteratively compared to the recursive approach.

4. Disadvantages:
   - Requires a sorted list as input. If the list is not sorted, a pre-sorting step is necessary.
   - The algorithm is slightly more complex to implement than linear search, but it offers significantly better performance for sorted data.

In summary, iterative binary search is a powerful and efficient algorithm for finding elements in sorted lists. Its logarithmic time complexity and low memory usage make it a preferred choice for a wide range of applications, especially when dealing with large datasets or when memory constraints are a concern.
'''

def IterBinSearch(read, s):
    
    low, mid, high = 0, 0, len(read)-1

    while low<=high:
        mid = (low + high) // 2

        if read[mid] < s:
            low = mid+1

        elif read[mid] > s:
            high = mid-1
        
        else:
            return mid
        
    return -1

print("Enter the elements: ")
read = list(map(int, input().split()))
s = int(input("Enter the element to be searched: "))
index = IterBinSearch(read, s)

if index == -1:
    print("Element not found!")
else:
    print("Element found at ", index)