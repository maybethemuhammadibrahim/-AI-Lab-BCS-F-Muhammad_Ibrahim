class TreeNode:
    def __init__(self, name, value=None):
        self.name = name
        self.value = value
        self.children = []

def build_tree(leafValues):
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
    n6.children = [TreeNode(f"Leaf_{leafValues[6]}", leafValues[6]), TreeNode(f"Leaf_{leafValues[7]}", leafValues[7])]
    
    return root

def minimax(node, depth, isMaxPlayer, visitedOrder):
    visitedOrder.append(node.name)
    
    if depth == 0 or not node.children:
        return node.value

    if isMaxPlayer:
        bestVal = float('-inf')
        for child in node.children:
            val = minimax(child, depth - 1, False, visitedOrder)
            bestVal = max(bestVal, val)
        node.value = bestVal
        return bestVal
    else:
        bestVal = float('inf')
        for child in node.children:
            val = minimax(child, depth - 1, True, visitedOrder)
            bestVal = min(bestVal, val)
        node.value = bestVal
        return bestVal

if __name__ == "__main__":
    leaves = [4, 7, 2, 5, 1, 8, 3, 6]
    
    print("--- standard minimax ---")
    rootFull = build_tree(leaves)
    visitedFull = []
    minimax(rootFull, float('inf'), True, visitedFull)
    print(f"root value: {rootFull.value}")
    print(f"visited order: {visitedFull}")
    
    print("\n--- depth limited minimax (depth=2) ---")
    rootLimited = build_tree(leaves)
    visitedLimited = []
    # depth 2 means it will stop at level 3 (n3-n6)
    # since n3-n6 have no values initially we need to mock heuristic evaluation
    # for simplicity we will just assign heuristic values to n3-n6
    rootLimited.children[0].children[0].value = 4
    rootLimited.children[0].children[1].value = 5
    rootLimited.children[1].children[0].value = 1
    rootLimited.children[1].children[1].value = 3
    
    # remove leaves to simulate depth limit at n3-n6
    for child in rootLimited.children:
        for grandchild in child.children:
            grandchild.children = []
            
    minimax(rootLimited, 2, True, visitedLimited)
    print(f"root value with depth 2 limit: {rootLimited.value}")
    print(f"visited order: {visitedLimited}")