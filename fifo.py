def fifo_page_replacement(ref, capacity):
    p = []                                  #current page queue using a list
    n = len(ref)
    page_fault = 0                          #number of page faults
    first_hold = 0                          #holds the value of the oldest page to be removed from the set
    for i in range(n):
       if(len(p) < capacity):               #queue has room for another page
          if(ref[i] not in p):              #page is not in memory, page fault and add
               p.append(ref[i])
               page_fault += 1
       else:                                #set is full
          if(ref[i] not in p):              #page is not in memory, page fault FIFO
               fp.pop(0)                    #pop the first (oldest) in queue
               p.append(ref[i])             
               page_fault += 1

    return page_fault





