import random as rand
import queue

def lru_page_replacement(reference, cap):
    p = []                                  #page queue
    pfaults = 0
    x = len(reference)

    for i in range(x):
        if i not in p:
            if (len(p) == cap):
                p.pop(p[0])
                p.append(i)
            else:
                p.append(i)
            pfaults += 1
        else:
            p.pop(i)
            p.append(i)

    return pfaults





