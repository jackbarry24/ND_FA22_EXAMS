
def ghz(speed):
    return speed * 10 ** 9

def s_to_ns(seconds):
    return seconds * 10 ** 9

CLOCK_RATE = ghz(1)
#percent of instructions that are load/store
LS_PERCENTAGE = 0.33

class Cache:
    def __init__(self, l1_access, l1_miss, main_access, fetch_time):
        self.l1_access = l1_access
        self.l1_miss = l1_miss
        self.main_access = main_access
        self.fetch_time = fetch_time

CACHE = Cache(1, 0.1, 75, 100)

def cpi(cache):
    mem_references = 1 + LS_PERCENTAGE
    penalty = cache.l1_miss * cache.main_access * mem_references
    return 1 + penalty

def amat(cache):
    return cache.l1_access + cache.l1_miss * cache.main_access

def main():
    print("CPI: ", cpi(CACHE))
    print("AMAT: ", amat(CACHE))

if __name__ == "__main__":
    main()


