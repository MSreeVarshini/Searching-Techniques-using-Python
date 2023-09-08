# Interpolation Search
'''Interpolation search is an efficient searching algorithm used to find a specific target element in a sorted array. It improves upon the basic binary search by estimating the position of the target element based on the values of the first and last elements in the array. Interpolation search is particularly effective when the data distribution is non-uniform and the values in the array are approximately uniformly distributed.

The best, average, and worst-case time complexities of the interpolation search algorithm can be analyzed based on the distribution of the data and the specific situation in which the algorithm is applied.

1. **Best Case**:
   - The best-case scenario occurs when the target element is found quickly, typically with very few iterations.
   - In the best case, the target element is found on the first iteration, which results in a time complexity of O(1).
   - This scenario happens when the target element is close to the beginning of the array, and the linear interpolation estimate is accurate.

2. **Average Case**:
   - The average-case complexity depends on the distribution of the data in the array.
   - If the data is uniformly distributed, the interpolation search performs well.
   - In the average case, the time complexity is approximately O(log log n), which is better than the basic binary search's O(log n).
   - However, the average case can deteriorate when the data distribution is not uniform.

3. **Worst Case**:
   - The worst-case scenario occurs when the data distribution is highly skewed, causing the interpolation search to degrade in performance.
   - In the worst case, the time complexity can be as bad as O(n), which is worse than linear search.
   - This situation occurs when the linear interpolation estimate consistently results in a poor choice of the next search interval.
   - For example, if the data is sorted in ascending order, and the target is greater than all elements, interpolation search will keep selecting the last possible position, leading to a linear search.

Interpolation search has a space complexity of O(1) because it uses a constant amount of extra space for variables regardless of the size of the input array.

In summary, the performance of the interpolation search algorithm heavily depends on the distribution of data. In cases where the data is uniformly distributed or close to uniformly distributed, interpolation search can provide excellent average-case performance. However, it may perform poorly in cases where the data distribution is highly skewed or when the target is located in an unfavorable position relative to the interpolation estimate.
'''

def interpolationSearch(read, target):
    low, high = 0, len(read)-1
    while low<=high and read[low] <= target <= read[high]:
        if low == high:
            if read[low] == target:
                return low
            return -1

        pos = low + ((target - read[low]) * (high - low)) // (read[high] - read[low])
        if read[pos] == target:
            return pos
        elif read[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    return -1

print("Enter the elements: ")
read = list(map(int, input().split()))
s = int(input("Enter the searching element: "))
index = interpolationSearch(read, s)

if index == -1:
    print("Element not found!")
else:
    print("Element found at ", index)