# Linear Search Technique
'''Linear search, also known as sequential search, is a basic search algorithm used to find a specific element in a list or array. While it is simple to implement, there are certain complexities associated with it in Python:

1. Time Complexity:
   - Worst-case time complexity: O(n)
   - Average-case time complexity: O(n)
   - Best-case time complexity: O(1) (when the element is found at the beginning of the list)

   The linear search algorithm examines each element in the list sequentially until it finds the target element or reaches the end of the list. In the worst case, it may need to examine all n elements, resulting in a linear time complexity.

2. Space Complexity:
   - Space complexity: O(1)

   Linear search typically doesn't require additional data structures or memory allocation, so its space complexity is constant, O(1).

3. Lack of Efficiency for Large Datasets:
   Linear search becomes inefficient for large datasets, as it needs to examine every element in the list one by one. Other search algorithms like binary search (for sorted lists) or hash tables can perform much better in terms of time complexity for large datasets.

4. Inefficient for Unsorted Lists:
   Linear search is less efficient when dealing with unsorted lists, as there is no advantage in terms of reducing the number of comparisons compared to searching a sorted list. Sorting the list first or using a more suitable algorithm might be a better choice in such cases.

5. No Early Exit:
   Linear search will continue searching even after finding the target element if you want to find all occurrences. If you only need the first occurrence, you need to add logic to break out of the loop once the element is found.

6. Lack of Adaptivity:
   Linear search doesn't take advantage of any patterns or order in the data. If the target element is near the beginning of the list, linear search will still examine every element sequentially, while some other algorithms can adapt and search more efficiently.

In summary, linear search is a straightforward algorithm suitable for small datasets or when the list is unordered. However, it's not efficient for large datasets, and there are more advanced search algorithms that can perform better in terms of time complexity for larger and sorted data.'''

def linearsearch(read, s):
    for i in range(len(read)):
        if read[i] == s:
            return i
    return -1

print("Enter the list/array of elements: ")
read = list(map(int, input().split()))
s = int(input("Enter the element to be searched: "))
index = linearsearch(read, s)

if index == -1:
    print("Element not found!")
else:
    print("Element found at ", index)