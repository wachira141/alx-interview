#!/usr/bin/env python3
from typing import List


def makeChange(arr: List, amount: int) -> int:
    total = arr[len(arr) - 1]
    index = len(arr) - 1
    count = 0

    result = rec_change(sorted(arr), total, amount, index, count)
    return result


def rec_change(arr, total, amount, index, count):
    if index < 0:
        return - 1

    count += 1
    if total == amount:
        return count

    total = total + arr[index]

    if total > amount:
        total = total - arr[index]
        if total > amount:
            total = arr[index - 1]
        count -= 1
        return rec_change(arr, total, amount, index - 1, count)
    else:
        return rec_change(arr, total, amount, index, count)


# makeChange([1256, 54, 48, 16, 102], 1453)
