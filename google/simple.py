from random import randint
from math import log

# Task: return k-th largest number from array

# generate random array
array_len = 10
array = [randint(0, 9) for p in range(0, array_len)]
# array = [5,4,3,2,1]
print(array)

'''
Use Bubble Sort algorythm to sort array and return k-th element
Time complexity: O(n^2) 
'''
def bubble_sort(array):
    for i in range(1,len(array)):
        for j in range(len(array)-i):
            if array[j] > array[j+1]:
                c = array[j+1]
                array[j+1] = array[j]
                array[j] = c
    return array
# Test
func = bubble_sort 
print( func )
sorted_array = func(array.copy())
# print( sorted_array )
print( sorted_array == sorted(array.copy()) )

'''
Use Quick Sort algorythm to sort array and return k-th element
Time complexity: O(n*log(n)) 

beacuse we crate new arrays (eg. smaller, larger)
this is not the fastest implementation, but it is easier to unterstand

to get O(n*log(n)) speed for all data, we should chose random pivot, 
not allways middle element of array (as implement for simplicity) 
'''
def quick_sort(array):
    if len(array) > 1:
        pivot = array[len(array)//2]
        smaller, larger = [], []
        for i in array[:len(array)//2] \
               + array[len(array)//2+1:]:
            if i < pivot:
                smaller.append(i)
            else:
                larger.append(i)
        smaller = quick_sort(smaller)
        larger = quick_sort(larger)
        array = smaller + [pivot] + larger
    return array 
# Test
func = quick_sort
print( func )    
sorted_array = quick_sort(array.copy())
# print( sorted_array )
print( sorted_array==sorted(array.copy()) )

'''
Use modifived Bubble Sort algorythm to sort usefull part of array and return k-th element
Time complexity: O(k*n)

we can still improve this algorythm for k~=n by reversing comparision (desired order in sorted array) 
to get O(min(k,n-k)*n)
'''
def bubble_part_sort(array, k):
    for i in range(1,k+1):
        for j in range(len(array)-i):
            if array[j] > array[j+1]:
                c = array[j+1]
                array[j+1] = array[j]
                array[j] = c
    return array
# Test
print(bubble_part_sort)
for k in range(1,len(array)+1):
    sorted_array = bubble_part_sort(array.copy(),k)
    # print(sorted_array)
    print(sorted_array[-k]==sorted(array.copy())[-k])

'''
Use modifived Bubble Sort algorythm or Quick Sort: whiewer is faster for given k
and return k-th element
Time complexity: O(min(k,log(n))*n)
'''
def adaptvie(array,k):
    if k < log(len(array),2):
        sorted_array = bubble_part_sort(array.copy(),k)
        return sorted_array[-k]
    else:
        sorted_array = quick_sort(array.copy())
        return sorted_array[-k]
# Test
func = adaptvie
print(func)
for k in range(1,len(array)+1):
    sorted_array = adaptvie(array.copy(),k)
    # print(sorted_array)
    print(sorted_array==sorted(array.copy())[-k])

'''
Use modifived Quick Sort algorythm to get k-th element and return it
Time complexity: O(n)
'''
def quick_part_sort(array, k):
    pivot = array[len(array)//2]
    smaller, larger = [], []
    for i in array[:len(array)//2]+array[len(array)//2+1:]:
        if i < pivot:
            smaller.append(i)
        else:
            larger.append(i)
    if len(larger) >= k:
        return quick_part_sort(larger, k)
    if len(larger)+1 == k:
        return pivot
    if len(larger) < k:
        return quick_part_sort(smaller, k - len(larger) - 1)
# Test
func = quick_part_sort 
print(func)    
for k in range(1,len(array)+1):
    sorted_array = func(array.copy(),k)
    # print(sorted_array)
    print(sorted_array==sorted(array.copy())[-k])
