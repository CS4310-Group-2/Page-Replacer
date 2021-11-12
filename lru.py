import random as rand
import queue

def lru_page_replacement(current_locus_size = 2, transition_probability = 0.01, target_len=100):
    p = []                                  #page queue
    location_start = 0                      #s
    address_size = 2 ** 32
    page_size = 2 ** 12
    v_mem_size = address_size - page_size   #P
    motion_rate = 100                       #m
    resident_string = ''                    #RS
    pfaults = 0
    flag = 0
    temp = 0

    while(len(resident_string)<=target_len):
        for x in range(motion_rate):
            p.append(-1)
            rand_int = rand.randint(location_start, location_start + current_locus_size)
            resident_string += repr(rand_int)

            for i in range(motion_rate):
                if p[i] == rand_int:
                    p.pop(i)                             #if random int is a process in the list, the process goes to the end of queue.
                    p.append(i)
                else:
                    p.pop(i)
                    p.append(rand_int)
                    pfaults += 1

            rand_real = rand.random()
            if rand_real < transition_probability:
                print("under prob")
                #pfaults = pfaults + 1
                location_start = rand.randint(0, v_mem_size - 1)
            else:
                location_start = location_start + (1 % v_mem_size)


    return resident_string,pfaults





