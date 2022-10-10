"""Reduce and accumulate module"""

import re
from tkinter import Y
from typing import TypeVar, Callable
A = TypeVar('A')
B = TypeVar('B')


def reduce(f: Callable[[A], B], x: list[A]) -> B:
    """
    Reduce f over list x.x

    >>> reduce(lambda x,y: x+y, [1, 2, 3])
    6
    >>> reduce(lambda x,y: x*y, [2, 2, 3])
    12
    """
    assert len(x) >= 2

    result = f(x[0],x[1])

    for i in range(2,len(x)):
        result = f(result,x[i])
    
    return result



def accumulate(f: Callable[[A], A], x: list[A], init_val) -> list[A]:
    """
    Accumulate f over list x.x

    >>> accumulate(lambda x,y: x+y, [1, 2, 3],0)
    [1, 3, 6]
    >>> accumulate(lambda x,y: x*y, [2, 2, 3],1)
    [2, 4, 12]
    """

    result = f(init_val,x[0])
    acc = [f(init_val,x[0])]

    for i in range(1,len(x)):
        result = f(result,x[i])
        acc.append(result)
    
    return acc


# print(accumulate(lambda x,y: x*y,[2, 2, 3],1))


# x = 5

# def f():
#     x = 25
#     print(x)

# print(x)
# f()
# print(x)


# print(f())