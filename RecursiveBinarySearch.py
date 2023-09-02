# Recursive Binary Search
'''Recursive binary search is a search algorithm that efficiently finds a target element in a sorted list by repeatedly dividing the search space in half. Here are the complexities associated with recursive binary search in Python:

1. Time Complexity:
   - Worst-case time complexity: O(log n)
   - Average-case time complexity: O(log n)
   - Best-case time complexity: O(1)

   The time complexity of recursive binary search is logarithmic (base 2). It reduces the search space by half in each recursive call, resulting in efficient search times even for large datasets. The best-case time complexity occurs when the target element is found at the middle position (the first element checked).

2. Space Complexity:
   - Space complexity: O(log n) (due to the recursive call stack)

   Recursive binary search utilizes the call stack for its recursive function calls. In the worst case, the maximum depth of the call stack is logarithmic in relation to the size of the input list, leading to a space complexity of O(log n).

3. Advantages:
   - Highly efficient for large sorted datasets.
   - Guarantees a logarithmic time complexity, which is significantly faster than linear search for large datasets.
   - Can be easily implemented recursively, making it a straightforward algorithm to write and understand.

4. Disadvantages:
   - Requires a sorted list as input. If the list is not sorted, a pre-sorting step is necessary.
   - The overhead of recursive function calls may be slightly higher compared to an iterative approach, but this is often negligible for most practical purposes.

Overall, recursive binary search is a powerful and efficient algorithm for finding elements in sorted lists. Its logarithmic time complexity makes it a preferred choice for large datasets where the performance of linear search becomes impractical. However, for small datasets or when sorting is not a concern, other search methods like linear search might be more straightforward to implement.
'''

def RecursiveBinSearch(read, low, high, s):
    while low <= high:

        mid = (low + high)//2
        
        if read[mid] == s:
            return mid
        
        elif read[mid] > s:
            return RecursiveBinSearch(read, low, mid-1, s)
        
        else:
            return RecursiveBinSearch(read, mid+1, high, s)
    else:
        return -1
    
print("Enter the elements: ")
read = list(map(int, input().split()))
s = int(input("Enter the searching element: "))
index = RecursiveBinSearch(read, 0, len(read), s)

if index == -1:
    print("Element not found!")
else:
    print("Element found at ", index)