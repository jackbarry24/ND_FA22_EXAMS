
def seconds_to_ghz(seconds):
    return 1 / (seconds * 10 ** 9)

class Instruction:
    def __init__(self, cci, count):
        self.cci = cci
        self.count = count

#FILL OUT
branch = Instruction(3, 150000000)
store = Instruction(4, 185000000)
load = Instruction(5, 260000000)
alu = Instruction(4, 225000000)

INSTRUCTIONS = { 
    "branch": branch,
    "store": store,
    "load": load,
    "alu": alu
}

#PUT as 1 if cpu time should be a multiple of "N"
CLOCK_CYCLE_TIME = 1
CPU_TIME = 0

TOTAL_INSTRUCTIONS = sum([i.count for i in INSTRUCTIONS.values()])

def modification(instructions, percentage, inst1, inst2, new_cc):
    inst1_count = instructions[inst1].count
    instructions[inst1].count = inst1_count * (1 - percentage)
    new_instructions = Instruction(new_cc, inst1_count * percentage)
    instructions[inst1 + "_" + inst2] = new_instructions
    instructions[inst2].count = instructions[inst2].count - \
                                        (new_instructions.count)
    global TOTAL_INSTRUCTIONS
    TOTAL_INSTRUCTIONS = sum([i.count for i in instructions.values()])

def clock_cycle_time(instructions, cpu_time):
    weighted_cci = sum([(i.cci * (i.count / TOTAL_INSTRUCTIONS)) for i in instructions.values()])
    return cpu_time / (weighted_cci * TOTAL_INSTRUCTIONS)

def cpu_time(instructions, clock_cycle_time):
    weighted_cci = sum([(i.cci * (i.count / TOTAL_INSTRUCTIONS)) for i in instructions.values()])
    return clock_cycle_time * weighted_cci * TOTAL_INSTRUCTIONS

def speedup(old_time, new_time):
    return old_time / new_time

def main():
    #CALL MODIFICATION HERE
    #modification(INSTRUCTIONS, 0.25, "load", "alu", 7)
    if CLOCK_CYCLE_TIME == 0:
        print(seconds_to_ghz(clock_cycle_time(INSTRUCTIONS, CPU_TIME)))
    if CPU_TIME == 0:
        print(cpu_time(INSTRUCTIONS, CLOCK_CYCLE_TIME))  

if __name__ == "__main__":
    main()