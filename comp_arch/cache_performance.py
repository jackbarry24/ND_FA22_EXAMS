
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

class Cache2:
    def __init__(self, ccs, hit_rate, main_mem_access):
        self.ccs = ccs
        self.hit_rate = hit_rate
        self.main_mem_access = main_mem_access

CACHE = Cache(1, 0.1, 75, 100)

def cpi(cache):
    mem_references = 1 + LS_PERCENTAGE
    penalty = cache.l1_miss * cache.main_access * mem_references
    return 1 + penalty

def amat(cache):
    return cache.l1_access + cache.l1_miss * cache.main_access

L1 = Cache2(1, 0.92, None)
L2 = Cache2(17, 0.95, 225)
L3 = Cache2(21, 1 - 0.022, None)
L4 = Cache2(40, 1 - 0.005, 120)

def amat_2level(l1, l2, additional):
    return l1.ccs + (1 - l1.hit_rate) * (l2.ccs + (1 - l2.hit_rate) * (l2.main_mem_access + additional))

def amat_3level(l1, l2, l3, additional):
    return l1.ccs + (1 - l1.hit_rate) * (l2.ccs + (1 - l2.hit_rate) * \
        (l3.ccs + (1 - l3.hit_rate) *(l3.main_mem_access + additional)))

def amat_4level(l1, l2, l3, l4, additional):
    return l1.ccs + (1 - l1.hit_rate) * (l2.ccs + (1 - l2.hit_rate) * \
        (l3.ccs + (1 - l3.hit_rate) * (l4.ccs + (1 - l4.hit_rate) * \
        (l4.main_mem_access + additional))))

def main():
    print("CPI: ", cpi(CACHE))
    print("AMAT: ", amat(CACHE))
    print("AMAT 2-level: ", amat_2level(L1, L2, 0))
    print("AMAT 4-level: ", amat_4level(L1, L2, L3, L4, 0))
if __name__ == "__main__":
    main()


