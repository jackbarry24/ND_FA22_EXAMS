from translate import *
import math


#FILL OUT
VIRTUAL_ADDRESS_SIZE = 14
PHYSICAL_ADDRESS_SIZE = 16
PAGE_SIZE = 64
PTE_SIZE = 4
PDE_SIZE = 4

def addressable_bytes():
    bytes = 2**VIRTUAL_ADDRESS_SIZE
    return power2(bytes)

def pages_needed():
    pages = 2**VIRTUAL_ADDRESS_SIZE / PAGE_SIZE
    return pages

def vpn_bits():
    return math.log(pages_needed(), 2)

def offset_bits():
    return math.log(PAGE_SIZE, 2)

def number_ptes():
    return 2**vpn_bits()
    
def page_table_bytes():
    return number_ptes() * PTE_SIZE

def page_table_pages():
    return number_ptes() * PTE_SIZE / PAGE_SIZE

def number_pdes():
    return page_table_pages()

def pdi_bits():
    return math.log(number_pdes(), 2)

def pti_bits():
    ptes_per_page = PAGE_SIZE / PTE_SIZE
    return math.log(ptes_per_page, 2)

def page_directory_bytes():
    return number_pdes() * PDE_SIZE

def page_directory_pages():
    return number_pdes() * PDE_SIZE / PAGE_SIZE

def main():
    print("Addressable bytes: ", addressable_bytes())
    print("Pages needed: ", pages_needed())
    print("VPN bits: ", vpn_bits())
    print("Offset bits: ", offset_bits())
    print("Number of PTEs: ", number_ptes())
    print("Page table size: ", page_table_bytes())
    print("Page table pages: ", page_table_pages())
    print("Number of PDEs: ", number_pdes())
    print("PDI bits: ", pdi_bits())
    print("PTI bits: ", pti_bits())
    print("Page directory size: ", page_directory_bytes())
    print("Page directory pages: ", page_directory_pages())

if __name__ == "__main__":
    main()
