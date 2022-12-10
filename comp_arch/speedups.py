
def ghz(speed):
    return speed * 10 ** 9

def seconds_to_ghz(seconds):
    return 1 / (seconds * 10 ** 9)

class Instruction:
    def __init__(self, cci, percentage):
        self.cci = cci
        self.percentage = percentage

def execution_time(instructions, clock_cycle_time):
    weighted_cci = sum([(i.cci * i.percentage) for i in instructions])
    return (1/ghz(clock_cycle_time)) * weighted_cci

class BASE:
    floating_point = Instruction(7, 0.1)
    integer = Instruction(4, 0.5)
    load_store = Instruction(5, 0.25)
    branch = Instruction(3, 0.15)
    insts = [floating_point, integer, load_store, branch]
    CC_TIME = 2.33
    execution_time = execution_time(insts, CC_TIME)
    speedup = 1

class MOD1:
    floating_point = Instruction(7, 0.1)
    integer = Instruction(3, 0.5)
    load_store = Instruction(5, 0.25)
    branch = Instruction(3, 0.15)
    insts = [floating_point, integer, load_store, branch]
    CC_TIME = 2.15
    execution_time = execution_time(insts, CC_TIME)
    speedup = BASE.execution_time / execution_time

class MOD2:
    integer = Instruction(4, 0.6)
    load_store = Instruction(5, 0.25)
    branch = Instruction(3, 0.15)
    insts = [integer, load_store, branch]
    CC_TIME = 2.33
    execution_time = execution_time(insts, CC_TIME)
    speedup = BASE.execution_time / execution_time

class MOD3:
    floating_point = Instruction(7, 0.1)
    integer = Instruction(4, 0.5)
    load_store = Instruction(5, 0.25)
    branch = Instruction(4, 0.15)
    insts = [floating_point, integer, load_store, branch]
    CC_TIME = 2.5
    execution_time = execution_time(insts, CC_TIME)
    speedup = BASE.execution_time / execution_time

def pretty(name, obj):
    print(name)
    print("\tExecution Time: {}".format(obj.execution_time))
    print("\tSpeedup: {}".format(obj.speedup))

def main():
    pretty("Base", BASE)
    pretty("Mod1", MOD1)
    pretty("Mod2", MOD2)
    pretty("Mod3", MOD3)

if __name__ == "__main__":
    main()


    