#!/usr/bin/python3
""" a method that determines if all the boxes can be opened."""


def canUnlockAll(boxes):
    """
    Returns True if Box can be unlocked
    otherwise false
    """
    i = 0
    arr = [0]
    x = len(boxes)
    opened_box = [1] + [0] * (x - 1)


    if i == 0:
        return True
    while stack is not None:
        j = arr.pop()
        for b in boxes[j]:
            if b > 0 and b < x and opened_box[b] == 0:
                opened_box[b] = 1
                arr.append[b]
        i+= 1
    if 0 in opened_box:
        return False
    return True
