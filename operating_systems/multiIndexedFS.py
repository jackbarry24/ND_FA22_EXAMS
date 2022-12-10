from translate import *

#FILL OUT
BLOCK_SIZE = 4*KB
BLOCK_ADDRESS_SIZE = 32
DIRECT_BLOCK_NUM = 4
INDIRECT_BLOCK_NUM = 1
POINTER_SIZE = 4
DISK_SIZE = 128*GB
BYTE = 8


def largest_disk():
    bytes = 2**BLOCK_ADDRESS_SIZE * BLOCK_SIZE
    return translate(bytes)

def largest_file():
    direct = DIRECT_BLOCK_NUM * BLOCK_SIZE
    indirect = INDIRECT_BLOCK_NUM * (BLOCK_SIZE/POINTER_SIZE) * BLOCK_SIZE
    return translate(direct) + " + " + translate(indirect)

def largest_file_num():
    direct = DIRECT_BLOCK_NUM
    indirect = INDIRECT_BLOCK_NUM * (BLOCK_SIZE/POINTER_SIZE)
    return direct + indirect

def free_block_bitmap():
    bytes = DISK_SIZE / BLOCK_SIZE / BYTE
    return translate(bytes)

def main():
    print("Largest disk size: ", largest_disk())
    print("Largest file size: ", largest_file())
    print("Largest number of files: ", largest_file_num())
    print("Free block bitmap size: ", free_block_bitmap())

if __name__ == "__main__":
    main()