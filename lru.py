
def lru_page_replacement(reference, cap):
    p = []                                  #page queue
    pfaults = 0
    x = len(reference)

    for i in range(x):
        if reference[i] not in p:
            if (len(p) == cap):
                p.pop(0)
                p.append(reference[i])
            else:
                p.append(reference[i])
            pfaults += 1
        else:
            p.remove(reference[i])
            p.append(reference[i])

    return pfaults





