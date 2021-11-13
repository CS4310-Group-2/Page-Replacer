from lru import lru_page_replacement
from fifo import fifo_page_replacement
from reference_string_generator import ref_str_gen



if __name__ == "__main__":

    ask_more = 'Y'
    while(ask_more == 'Y' or ask_more == 'y'):
        print('Welcome to Page replacer demo!')


        print('0.Nothing\n1. Locus size\n2.transition probability')
        ref_string_choice = int(input('What are we changing on the ref string?:'))
        reference_str = ''

        if ref_string_choice == 1:
            print('Locus size')
            changed_value = int(input('How big do you want the locus?:'))
            reference_str = ref_str_gen(changed_value)

        elif ref_string_choice == 2:
            print('transition probability')
            changed_value = float(input('How high is the probability?:'))
            reference_str = ref_str_gen(2,changed_value)

        else:
            reference_str = ref_str_gen()

        print("The reference string:"+reference_str+"\nLength of string:"+str(len(reference_str)))


        print('1.fifo\n2.lru')
        algo_choice = int(input('Which algorithm do you want?'))

        page_faults = 0
        if algo_choice == 1:
            print('fifo')
            page_faults = fifo_page_replacement(reference_str,3)

        elif algo_choice == 2:
            print('lru')
            page_faults = lru_page_replacement(reference_str,3)

        print("Number of page faults:"+str(page_faults))


        ask_more = input('Do you want to continue?(y/n):')

