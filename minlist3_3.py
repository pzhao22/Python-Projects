# O(n) vs O(n^2) implementation of finding the minimum value in a list

import time
import random

def quadratic_method(list):
    min = list[0]
    for i in list:
        isSmallest = True
        for j in list:
            if j < i:
                isSmallest = False
        if isSmallest:
            min = i
    return min



def linear_method(list):
    min = list[0]
    for i in list:
        if i < min:
            min = i
    return min

def main():
    n = 10000
    list = []
    for i in range(n):
        list.append(random.random())

    t1 = time.time()
    min1 = quadratic_method(list)
    t2 = time.time()
    min2 = linear_method(list)
    t3 = time.time()

    print(f"Quadratic method took {t2-t1} seconds. Min of list is {min1}")
    print(f"Linear method took {t3-t2} seconds. Min of list is {min2}")

main()