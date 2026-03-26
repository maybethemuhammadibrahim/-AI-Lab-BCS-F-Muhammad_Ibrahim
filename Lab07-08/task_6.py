def solveOptimization():
    bestScore = float('-inf')
    bestAssignment = None
    domainRange = range(21)

    # exhaustive search over small bounded domain
    for varX in domainRange:
        for varY in domainRange:
            if 3 * varX + varY > 18:
                continue
            for varZ in domainRange:
                if varX + 2 * varY + varZ > 20:
                    continue

                currentScore = 4 * varX + 2 * varY + varZ
                if currentScore > bestScore:
                    bestScore = currentScore
                    bestAssignment = {'x': varX, 'y': varY, 'z': varZ}

    return bestScore, bestAssignment

if __name__ == "__main__":
    maxScore, optimalVars = solveOptimization()
    if optimalVars:
        print("--- task 6 simple optimization ---")
        print(f"optimal value: {maxScore}")
        print(f"x: {optimalVars['x']}")
        print(f"y: {optimalVars['y']}")
        print(f"z: {optimalVars['z']}")
    else:
        print("optimal solution not found")