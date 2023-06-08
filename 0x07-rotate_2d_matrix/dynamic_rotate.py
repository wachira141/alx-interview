#!/usr/bin/env python3
from typing import List


def reve_func(arr: list) -> list:
    main_arr = []
    position = 0
    # while position <= len(arr) -1:
    return reverse_sub_arr(arr,len(arr)-1 ,main_arr ,position)
   
        # position += 1
    
    print(main_arr)

def reverse_sub_arr(arr: List,lnt ,sub_arr: list, position: int):
  

    if position > lnt:
        return sub_arr
    
    sub_arr.append(arr[lnt][position])
    # main_arr.append(sub_arr)
    print(sub_arr)
    
    return reverse_sub_arr(arr, lnt -1,sub_arr,position + 1)
        # arr_len -=1
        # position += 1

    # while incrementor <= len(arr) -1:
    #     sub_arr.append(arr[arr_len][position])
    #     incrementor += 1
    #     arr_len -= 1

reve_func([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
