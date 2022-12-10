



def type1():
    UNCONDITIONAL = 0.04
    CONDITIONAL = 0.12
    PENALTY = 3
    CONDITIONAL_TAKEN = 0.5
    
    #unconditional branch penalty
    uncond_penalty = UNCONDITIONAL * PENALTY
    #conditional branch penalty
    cond_penalty = CONDITIONAL * PENALTY * CONDITIONAL_TAKEN
    #overall penalty
    overall_penalty = uncond_penalty + cond_penalty
    print("Penalty: ", overall_penalty)
    print("New CPI: ", 1 + overall_penalty)


def type2():
    MIX = {
        "loads": 0.23,
        "stores": 0.13,
        "conditional": 0.19,
        "unconditional": 0.02,
        "other": 0.43
    }
    #what percentage of the time the next instruction uses the value loaded
    LOAD_USED_NEXT = 0.5
    #what percentage of the time is the conditional branch predicted correctly
    COND_BR_PRED = 0.75
    #penalties
    MISPREDICT_PENALTY = 1
    BRANCH_PENALTY = 1
    LOAD_IMMEDIATE_PENALTY = 1

    load_immediate = MIX["loads"] * LOAD_USED_NEXT * LOAD_IMMEDIATE_PENALTY
    branch = MIX["unconditional"] * BRANCH_PENALTY 
    mispredict = MIX["conditional"] * (1 - COND_BR_PRED) * MISPREDICT_PENALTY
    overall_penalty = load_immediate + branch + mispredict
    print("Penalty: ", overall_penalty)
    print("New CPI: ", 1 + overall_penalty)

def main():
    type1()
    type2()

if __name__ == "__main__":
    main()
