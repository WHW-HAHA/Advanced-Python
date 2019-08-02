'Hanwei wang RHDHV'

import numpy as np
import sys
import time

n = 1000
a_disorder = np.random.rand(n)
for i, a in enumerate(a_disorder):
    sys.stdout.write("\rProgress: " + str(i/n *100) + ':' +  str(a))

def select_sort(origin_items, comp = lambda x,y: x < y):
    current_time = time.time()
    items = origin_items[:]
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i+ 1, len(items)):
            if comp(items[j], items[min_index]):
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
    print('Time spent: ',time.time() - current_time)
    return items

def bubble_sort(origin_items, comp=lambda x, y: x > y):
    current_time = time.time()
    items = origin_items[:]
    for i in range(len(items) - 1):
        swapped = False
        for j in range(i, len(items) - 1 - i):
            if comp(items[j], items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if swapped:
            swapped = False
            for j in range(len(items) - 2 - i, i, -1):
                if comp(items[j - 1], items[j]):
                    items[j], items[j - 1] = items[j - 1], items[j]
                    swapped = True
        if not swapped:
            break
    print('Time spent: ', time.time() - current_time)
    return items

def merge_sort(items, comp = lambda x, y: x < y ):
    if len(items) <2:
        return items[:]
    mid = len(items)//2
    left = merge_sort(items[:mid], comp)
    right = merge_sort(items[mid:],comp)
    return merge(left, right, comp)

def merge(items1, items2, comp):
    items = []
    index1, index2 = 0, 0
    while index1 < len(items1) and index2 < len(items2):
        if comp(items1[index1], items2[index2]):
            items.append(items1[index1])
            index1 += 1
        else:
            items.append(items2[index2])
            index2 += 2

    items += items1[index1:]
    items += items2[index2:]
    return items

# bubble_sort is 100 times quicker than select sort
select_sort(a_disorder)
bubble_sort(a_disorder)






