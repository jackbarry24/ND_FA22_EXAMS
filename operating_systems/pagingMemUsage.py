from translate import *
import math


#FILL OUT
MACHINE_BITS = 32
PAGE_SIZE = 4*KB
PTE_SIZE = 4 

def max_pages():
    pages = 2**MACHINE_BITS / PAGE_SIZE
    return pages

def vpn_bits():
    return math.log(max_pages(), 2)

def offset_bits():
    return math.log(PAGE_SIZE, 2)

def page_table_size():
    return translate(max_pages() * PTE_SIZE)

def main():
    print("Maximum number of pages: ", power2(max_pages()))
    print("VPN bits: ", vpn_bits())
    print("Offset bits: ", offset_bits())
    print("Page table size: ", page_table_size())

if __name__ == "__main__":
    main()
