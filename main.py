from lru import lru_page_replacement
from fifo import fifo_page_replacement
from reference_string_generator import ref_str_gen



if __name__ == "__main__":

    ask_more = 'Y'
    while(ask_more == 'Y' or ask_more == 'y'):
        print('Welcome to Page replacer demo!')

        ask_more = input('Do you want to continue?(y/n):')
        print('continue')

