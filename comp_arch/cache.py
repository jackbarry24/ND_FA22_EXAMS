import math

#FILL OUT
###########################
DIRECT_MAPPED = False
SET_ASSOCIATIVE = True

WORD_ADDRESSED = False
BYTE_ADDRESSED = True

ADDRESS_SIZE = 32
ADDRESS = "FAB12389"

BLOCK_COUNT = 4096
WORD_SIZE = 4
BLOCK_SIZE = 512
WORDS_PER_BLOCK = 0
SET_ASSOCIATIVE_WAYS = 2
###########################

def hex_to_bin(hex_str):
    return bin(int(hex_str, 16))[2:].zfill(ADDRESS_SIZE)

def bin_to_dec(bin_str):
    return int(bin_str, 2)

class Cache:
    def __init__(self, block_count, word_size, block_size, words_per_block):
        self.block_count = block_count
        self.word_size = word_size
        self.block_size = block_size
        self.words_per_block = words_per_block

    def offset_bits(self):
        if WORD_ADDRESSED:
            if self.words_per_block:
                return int(math.log2(self.words_per_block))
            else:
                return int(math.log2(self.block_size / self.word_size))
        elif BYTE_ADDRESSED:
            return int(math.log2(self.block_size))
    
    def tag_bits(self):
        return int(ADDRESS_SIZE - self.index_bits() - self.offset_bits())

    def translate(self, hex_address):
        bin_address = hex_to_bin(hex_address)
        tag = bin_address[:self.tag_bits()]
        index = bin_address[self.tag_bits():self.tag_bits() + self.index_bits()]
        offset = bin_address[self.tag_bits() + self.index_bits():]
        return bin_to_dec(tag), bin_to_dec(index), bin_to_dec(offset)

    def __str__(self):
        return "Offset bits: " + str(self.offset_bits()) + \
            "\nIndex bits: " + str(self.index_bits()) + \
            "\nTag bits: " + str(self.tag_bits())


class DirectMappedCache (Cache):
    def __init__(self, block_count, word_size, block_size, words_per_block):
        super().__init__(block_count, word_size, block_size, words_per_block)

    def index_bits(self):
        return int(math.log2(self.block_count))
    
    def cache_size(self, tag, index, offset, ways):
        bytes_per_block = 2 ** offset
        blocks_per_cache = 2 ** index
        return bytes_per_block * blocks_per_cache
        

class SetAssociativeCache (Cache):
    def __init__(self, block_count, word_size, block_size, words_per_block, set_count):
        super().__init__(block_count, word_size, block_size, words_per_block)
        self.set_count = set_count

    def index_bits(self):
        return int(math.log2(self.block_count / self.set_count))

    def cache_size(self, tag, index, offset, ways):
        bytes_per_block = 2 ** offset
        sets = 2 ** index
        blocks_per_set = ways
        blocks_per_cache = sets * blocks_per_set
        return bytes_per_block * blocks_per_cache

def main():
    params = [BLOCK_COUNT, WORD_SIZE, BLOCK_SIZE, WORDS_PER_BLOCK]

    if DIRECT_MAPPED:
        cache = DirectMappedCache(*params)
    elif SET_ASSOCIATIVE:
        cache = SetAssociativeCache(*params, SET_ASSOCIATIVE_WAYS)
    else:
        print("Error: Cache type not specified")
        return

    print(cache)
    tag, index, offset = cache.translate(ADDRESS)
    
    if DIRECT_MAPPED:
        print("Block: ", index)
    elif SET_ASSOCIATIVE:
        print("Set: ", index)

    if WORD_ADDRESSED:
        print("Word: ", offset)
    elif BYTE_ADDRESSED:
        print("Byte: ", offset)
    print("Tag: ", tag)

    #size = cache.cache_size(10, 14, 8, 4)
    #print("Cache size: 2^", int(math.log(size, 2)), " bytes")


if __name__ == "__main__":
    main()