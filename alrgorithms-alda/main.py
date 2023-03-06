import time
import random

def quick_sort2(array):
    if len(array) > 1:
        piv = int(len(array) / 2)
        val = array[piv]
        lft = [i for i in array if i < val]
        mid = [i for i in array if i == val]
        rgt = [i for i in array if i > val]

        res = quick_sort2(lft) + mid + quick_sort2(rgt)
        return res
    else:
        return array

def merge_sort():
    None


def bubble_sort():
    None


if __name__ == '__main__':
    z = [random.randint(0, 10000) for i in range(1000000)]
    quick_sort2(z)
