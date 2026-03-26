class TreeNode:
    def __init__(self, name, value=None):
        self.name = name
        self.value = value
        self.children = []

def build_modified_tree(leafValues):
    root = TreeNode("Root")
    n1 = TreeNode("N1")
    n2 = TreeNode("N2")
    n3 = TreeNode("N3")
    n4 = TreeNode("N4")
    n5 = TreeNode("N5")
    n6 = TreeNode("N6")

    root.children = [n1, n2]
    n1.children = [n3, n4]
    n2.children = [n5, n6]
    
    n3.children = [TreeNode(f"Leaf_{leafValues[0]}", leafValues[0]), TreeNode(f"Leaf_{leafValues[1]}", leafValues[1])]
    n4.children = [TreeNode(f"Leaf_{leafValues[2]}", leafValues[2]), TreeNode(f"Leaf_{leafValues[3]}", leafValues[3])]
    n5.children = [TreeNode(f"Leaf_{leafValues[4]}", leafValues[4]), TreeNode(f"Leaf_{leafValues[5]}", leafValues[5])]
    # adding an extra branch to n6 to meet task requirement
    n6.children = [
        TreeNode(f"Leaf_{leafValues[6]}", leafValues[6]), 
        TreeNode(f"Leaf_{leafValues[7]}", leafValues[7]),
        TreeNode("Leaf_Extra_10", 10)
    ]
    
    return root

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
            if beta <= alpha:
                prunedNodes.append(node.name)
                break
        node.value = bestVal
        return bestVal

def get_optimal_path(node, isMaxPlayer):
    if not node.children:
        return [node.name]
    
    if isMaxPlayer:
        bestChild = max(node.children, key=lambda c: c.value)
    else:
        bestChild = min(node.children, key=lambda c: c.value)
        
    return [node.name] + get_optimal_path(bestChild, not isMaxPlayer)

if __name__ == "__main__":
    # modifying leaf values for this task
    modifiedLeaves = [8, 5, 6, -2, 3, 9, 1, 4]
    rootNode = build_modified_tree(modifiedLeaves)
    
    visited = []
    pruned = []
    alpha_beta(rootNode, float('inf'), float('-inf'), float('inf'), True, visited, pruned)
    
    print("--- modified tree with alpha-beta ---")
    print(f"updated root value: {rootNode.value}")
    print(f"nodes pruned: {pruned}")
    
    optimalPath = get_optimal_path(rootNode, True)
    print(f"optimal path for max: {' -> '.join(optimalPath)}")
    print("\ncomment: root value changes due to new leaf values and pruning occurs differently based on branch ordering")