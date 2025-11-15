### Sorting Algorithms 

#### Bubble sort

Bubble sort, sometimes referred to as sinking sort, is a simple sorting algorithm that repeatedly steps through the input list element by element, comparing the current element with the one after it, swapping their values if needed.
The earliest description of the bubble sort algorithm was in a 1956 paper by mathematician and actuary Edward H. Friend, _Sorting on Electronic Computer Systems_, published in the third issue of the third volume of the _Journal of the Association for Computing Machinery_

Because it need to iterate over and over again to sort all of the elements as it just comparing current element with one after it and only swapping if the number on the right is smaller it is really slow and not efficient and does have useful use cases.
Bubble sort has a worst-case and average complexity of O(n2)O(n2), where nn is the number of items being sorted. Most practical sorting algorithms have substantially better worst-case or average complexity, often O(nlog⁡n)O(nlogn). Even other O(n2)O(n2) sorting algorithms, such as insertion sort, generally run faster than bubble sort, and are no more complex. For this reason, bubble sort is rarely used in practice

#### Merge Sort

Merge sort is a recursive sorting algorithm and it's quite a bit faster than bubble sort. It's a divide and conquer algorithm.

In merge sort we: 
- Divide the array into two (equal) halves (divide)
- Recursively sort the two halves 
- Merge the two halves to form a sorted array (conquer)

Pros:

- **Fast**: Merge sort is much faster than bubble sort. `O(n*log(n))` instead of `O(n^2)`.
- **Stable**: Merge sort is a [stable sort](https://en.wikipedia.org/wiki/Category:Stable_sorts) which means that values with duplicate keys in the original list will be in the same order in the sorted list.

Cons:

- **Memory usage**: Most sorting algorithms can be performed using a single copy of the original array. Merge sort requires extra subarrays in memory.
- **Recursive**: Merge sort requires many recursive function calls, and in many languages (like Python), this can incur a performance penalty.

#### Insertion Sort

Insertion sort builds a sorted list one item at a time. It's much less efficient on large lists than merge sort because it's `O(n^2)`, but it's actually faster (not in Big O terms, but due to smaller constants) than merge sort on small lists.
