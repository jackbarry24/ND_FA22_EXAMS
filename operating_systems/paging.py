from translate import *
import math


#FILL OUT
ADDRESS_SPACE_SIZE = 64
PAGE_SIZE = 16
VIRTUAL_ADDRESS = 36

def page():
    page = int(VIRTUAL_ADDRESS / PAGE_SIZE)
    return page

def offset():
    offset = VIRTUAL_ADDRESS % PAGE_SIZE
    return offset

def physical_address():
    #FILL OUT
    PAGE_FRAME_START = 80
    return PAGE_FRAME_START + offset()

def main():
    print("Page: ", page())
    print("Offset: ", offset())
    print("Physical address: ", physical_address())

if __name__ == "__main__":
    main()
