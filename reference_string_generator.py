import random as rand

def ref_str_gen(current_locus_size = 2, transition_probability = 0.01, target_len=10000):
    location_start = 0
    address_size = 2 ** 32
    page_size = 2 ** 12
    v_mem_size = address_size - page_size
    motion_rate = 100
    resident_string = ''
    while(len(resident_string)<=target_len):
        for x in range(motion_rate):
            rand_int = rand.randint(location_start, location_start + current_locus_size)
            rand_real = rand.random()
            resident_string += repr(rand_int)
            if(len(resident_string)>target_len):
                return resident_string

            if rand_real < transition_probability:
                location_start = rand.randint(0, v_mem_size - 1)
            else:
                location_start = location_start + (1 % v_mem_size)

    return resident_string



