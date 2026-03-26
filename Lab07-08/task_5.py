#TASK 5

def findAllSolutions():
    solutionsList = []
    domainRange = range(4)

    for varA in domainRange:
        for varB in domainRange:
            if varA == varB or varA + varB > 4:
                continue
            for varC in domainRange:
                if varB == varC:
                    continue
                solutionsList.append({'a': varA, 'b': varB, 'c': varC})

    return solutionsList

if __name__ == "__main__":
    allValidSolutions = findAllSolutions()
    print("--- task 5 all possible valid solutions ---")
    for idx, sol in enumerate(allValidSolutions, 1):
        print(f"solution {idx}: a={sol['a']} b={sol['b']} c={sol['c']}")
    print(f"\ntotal solutions found: {len(allValidSolutions)}")