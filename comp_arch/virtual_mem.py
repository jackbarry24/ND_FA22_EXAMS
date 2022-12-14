import math

def ghz(speed):
    return speed * 10 ** 9

def add_hex(hex1, hex2, length=16):
    return hex(int(hex1, 16) + int(hex2, 16)).zfill(length)


VIRTUAL_ADDRESS_LENGTH = 40
PHYSICAL_ADDRESS_LENGTH = 32
CACHE_LEVELS = 2
CLOCK_RATE = ghz(1)
PAGE_TABLE_ENTRIES = 2 ** 16
PTR = "10010000"
VIRTUAL_ADDRESS = "BE97142880"

OFFSET_BITS = int(math.log(PAGE_TABLE_ENTRIES, 2))

def get_physical_address():
    #the vritual page number is the first x bits of the virtual address where x is (vrutal address length - offset bits)
    virtual_page_number = VIRTUAL_ADDRESS[:(VIRTUAL_ADDRESS_LENGTH - OFFSET_BITS)//4]
    print("Virtual page number: " + virtual_page_number)
    offset = VIRTUAL_ADDRESS[(VIRTUAL_ADDRESS_LENGTH - OFFSET_BITS)//4:]
    print("Offset: " + offset)
    pfn = add_hex(PTR, virtual_page_number, PHYSICAL_ADDRESS_LENGTH//4)
    print("PFN: " + pfn)
    #ADD DATA MANUALLY
    DATA = "00000966"
    output = DATA + offset
    return output.lstrip("0")

    
def main():
    print(get_physical_address())

if __name__ == "__main__":
    main()





