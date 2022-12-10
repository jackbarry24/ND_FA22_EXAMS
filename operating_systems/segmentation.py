from translate import *
import math

class Segment:
    def __init__(self, name, base, size, growth, protection):
        self.name = name
        self.base = base
        self.size = size
        self.growth = growth
        self.protection = protection


#FILL OUT
CODE = Segment("Code", 32*KB, 2*KB, 1, "rx")
DATA = Segment("Data", 34*KB, 2*KB, 1, "rw")
HEAP = Segment("Heap", 36*KB, 2*KB, 1, "rw")
STACK = Segment("Stack", 28*KB, 2*KB, 0, "rw")
MEMORY = [CODE, DATA, HEAP, STACK]
VIRTUAL_ADDRESS = '1000001000001010'

#DO NOT CHANGE
VIRTUAL_ADDRESS_SIZE = len(VIRTUAL_ADDRESS)
NUMBER_OF_SEGMENTS = len(MEMORY)
SEGMENT_BITS = int(math.log(NUMBER_OF_SEGMENTS, 2))
OFFSET_BITS = VIRTUAL_ADDRESS_SIZE - SEGMENT_BITS

def largest_segment():
    return 2**OFFSET_BITS

def max_offset():
    return hex(2**OFFSET_BITS - 1)

def which_segment():
    segment = int(VIRTUAL_ADDRESS[:SEGMENT_BITS], 2)
    return MEMORY[segment].name

def physical_address():
    segment = int(VIRTUAL_ADDRESS[:SEGMENT_BITS], 2)
    offset = int(VIRTUAL_ADDRESS[SEGMENT_BITS:], 2)
    if offset > MEMORY[segment].size:
        return "Segmentation fault"
    base = MEMORY[segment].base
    return base + offset

def main():
    print("Largest segment: ", largest_segment())
    print("Maximum offset: ",  max_offset())
    print("Which segment: ", which_segment())
    print("Physical address: ", physical_address())

if __name__ == "__main__":
    main()





