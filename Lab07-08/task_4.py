# TASK 4

def validateConstraints(currentAssignment):
    varA = currentAssignment.get('a')
    varB = currentAssignment.get('b')
    varC = currentAssignment.get('c')

    if varA is not None and varB is not None:
        if varA == varB:
            return False
        if varA + varB > 4:
            return False
            
    if varB is not None and varC is not None:
        if varB == varC:
            return False

    return True

def runBacktrack(variableList, currentAssignment):
    # return state when depth matches variable count
    if len(currentAssignment) == len(variableList):
        return currentAssignment

    targetVar = variableList[len(currentAssignment)]
    domainRange = [0, 1, 2, 3]

    for testValue in domainRange:
        currentAssignment[targetVar] = testValue
        
        # evaluate partial state before advancing depth
        if validateConstraints(currentAssignment):
            validPath = runBacktrack(variableList, currentAssignment)
            if validPath:
                return validPath
                
        # revert state for next iteration
        del currentAssignment[targetVar]

    return None

if __name__ == "__main__":
    varTargets = ['a', 'b', 'c']
    finalSolution = runBacktrack(varTargets, {})

    if finalSolution:
        print("--- task 4 basic csp solution ---")
        print(f"a: {finalSolution['a']}")
        print(f"b: {finalSolution['b']}")
        print(f"c: {finalSolution['c']}")
    else:
        print("no solution found")