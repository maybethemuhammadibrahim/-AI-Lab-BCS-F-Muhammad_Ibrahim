class TreeNode:
    def __init__(self, name, value=None):
        self.name = name
        self.value = value
        self.children = []

def build_tree(leafValues):
    root = TreeNode("Root")
    n1 = TreeNode("N1")
    n2 = TreeNode("N2")
    
    
    root.children = [n1, n2]
    n3, n4, n5, n6 = TreeNode("N3"), TreeNode("N4"), TreeNode("N5"), TreeNode("N6")
    n1.children = [n3, n4]
    n2.children = [n5, n6]
    
    n3.children = [TreeNode(f"Leaf_{leafValues[0]}", leafValues[0]), TreeNode(f"Leaf_{leafValues[1]}", leafValues[1])]
    n4.children = [TreeNode(f"Leaf_{leafValues[2]}", leafValues[2]), TreeNode(f"Leaf_{leafValues[3]}", leafValues[3])]
    n5.children = [TreeNode(f"Leaf_{leafValues[4]}", leafValues[4]), TreeNode(f"Leaf_{leafValues[5]}", leafValues[5])]
    n6.children = [TreeNode(f"Leaf_{leafValues[6]}", leafValues[6]), TreeNode(f"Leaf_{leafValues[7]}", leafValues[7])]
    
    return root

def minimax(node, depth, isMaxPlayer, visitedOrder):
    visitedOrder.append(node.name)
    if depth == 0 or not node.children:
        return node.value

    if isMaxPlayer:
        bestVal = float('-inf')
        for child in node.children:
            bestVal = max(bestVal, minimax(child, depth - 1, False, visitedOrder))
        node.value = bestVal
        return bestVal
    else:
        bestVal = float('inf')
        for child in node.children:
            bestVal = min(bestVal, minimax(child, depth - 1, True, visitedOrder))
        node.value = bestVal
        return bestVal

def alpha_beta(node, depth, alpha, beta, isMaxPlayer, visitedOrder, prunedNodes):
    visitedOrder.append(node.name)
    
    if depth == 0 or not node.children:
        return node.value

    if isMaxPlayer:
        bestVal = float('-inf')
        for child in node.children:
            val = alpha_beta(child, depth - 1, alpha, beta, False, visitedOrder, prunedNodes)
            bestVal = max(bestVal, val)
            alpha = max(alpha, bestVal)
            # prune if current max guarantee is better than min upper bound
            if beta <= alpha:
                prunedNodes.append(node.name)
                break
        node.value = bestVal
        return bestVal
    else:
        bestVal = float('inf')
        for child in node.children:
            val = alpha_beta(child, depth - 1, alpha, beta, True, visitedOrder, prunedNodes)
            bestVal = min(bestVal, val)
            beta = min(beta, bestVal)
            # prune if current min guarantee is worse than max lower bound
            if beta <= alpha:
                prunedNodes.append(node.name)
                break
        node.value = bestVal
        return bestVal

if __name__ == "__main__":
    leaves = [4, 7, 2, 5, 1, 8, 3, 6]
    
    rootStandard = build_tree(leaves)
    visitedStandard = []
    minimax(rootStandard, float('inf'), True, visitedStandard)
    
    rootPruned = build_tree(leaves)
    visitedPruned = []
    prunedNodes = []
    alpha_beta(rootPruned, float('inf'), float('-inf'), float('inf'), True, visitedPruned, prunedNodes)
    
    print("--- alpha-beta pruning ---")
    print(f"root value: {rootPruned.value}")
    print(f"visited order: {visitedPruned}")
    print(f"pruned at nodes: {prunedNodes}")
    
    print("\n--- comparison ---")
    print(f"nodes visited (standard): {len(visitedStandard)}")
    print(f"nodes visited (alpha-beta): {len(visitedPruned)}")
    print("pruning reduces computation by ignoring branches that cannot affect the final decision")