def fifo_page_replacement(ref, capacity):
    p = []                                  #current page queue
    s = set()                               #unordered set of current pages for quick check
    n = len(ref)
    page_fault = 0                          #number of page faults
    first_hold = 0                          #holds the value of the oldest page to be removed from the set
    for i in range(n):
       if(len(s) < capacity):             #set has room for another page
          if(ref[i] not in s):              #page is not in memory, page fault and add
               s.add(ref[i])
               p.append(ref[i])
               page_fault += 1
        else:                               #set is full
           if(ref[i] not in s):             #page is not in memory, page fault FIFO
               first_hold = p.pop(0)        #the value of the First (oldest) in queue
               s.remove(first_hold)         #remove first from set by value
               s.add(ref[i])                
               p.append(ref[i])             
               page_fault += 1

    return page_fault





