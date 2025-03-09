def trimBST(tree, minVal, maxVal):
    if not tree:
        return
    tree.left=trimBST(tree.left, minVal, maxVal)   #递归调用,后序遍历左子节点
    tree.right=trimBST(tree.right, minVal, maxVal) #递归调用,后序遍历右子节点
    if minVal<=tree.val<=maxVal:
        return tree
    if tree.val<minVal:
        return tree.right
    if tree.val>maxVal:
        return tree.left