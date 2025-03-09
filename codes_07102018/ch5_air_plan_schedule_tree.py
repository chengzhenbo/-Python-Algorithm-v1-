#coding=utf-8
class BSTnode(object):
    def __init__(self, parent, t):
        self.key = t
        self.parent = parent
        self.left = None
        self.right = None
    def insert(self, t):
        if abs(t-self.key)<3:                  # 发现冲突
            print("Insert error!")
            return
        if t < self.key:                       # 往左子树
            if self.left is None:              # 没有左子节点
                self.left = BSTnode(self, t)   # 当前节点作为左子节点              
                return self.left
            else:
                return self.left.insert(t)     # 递归
        else:
            if self.right is None:             # 没有右子节点
                self.right = BSTnode(self, t)  # 当前节点作为右子节点 
                return self.right
            else:
                return self.right.insert(t)   # 递归
    def inorder_tree_walk(self,x):
    	if x != None:
    		self.inorder_tree_walk(x.left)
    		print (x.key)
    		self.inorder_tree_walk(x.right)

class BST(object):
    def __init__(self):
        self.root = None
    def insert(self, t):
        if self.root is None:
            self.root = BSTnode(None, t)
            return self.root
        else:
        	return self.root.insert(t)
    def inorder_tree_walk(self):
    	if self.root is not None:
    		self.root.inorder_tree_walk(self.root)

    def __str__(self):
        if self.root is None: return '<empty tree>'
        def recurse(node):
            if node is None: return [], 0, 0
            label = str(node.key)
            left_lines, left_pos, left_width = recurse(node.left)
            right_lines, right_pos, right_width = recurse(node.right)
            middle = max(right_pos + left_width - left_pos + 1, len(label), 2)
            pos = left_pos + middle // 2
            width = left_pos + middle + right_width - right_pos
            while len(left_lines) < len(right_lines):
                left_lines.append(' ' * left_width)
            while len(right_lines) < len(left_lines):
                right_lines.append(' ' * right_width)
            if (middle - len(label)) % 2 == 1 and node.parent is not None and \
               node is node.parent.left and len(label) < middle:
                label += '.'
            label = label.center(middle, '.')
            if label[0] == '.': label = ' ' + label[1:]
            if label[-1] == '.': label = label[:-1] + ' '
            lines = [' ' * left_pos + label + ' ' * (right_width - right_pos),
                     ' ' * left_pos + '/' + ' ' * (middle-2) +
                     '\\' + ' ' * (right_width - right_pos)] + \
              [left_line + ' ' * (width - left_width - right_width) +
               right_line
               for left_line, right_line in zip(left_lines, right_lines)]
            return lines, pos, width
        return '\n'.join(recurse(self.root) [0])

if __name__ == "__main__": 
	R=[46, 41, 49, 56]
	t=53
	tree = BST()
	for item in R:
		tree.insert(item)
	tree.insert(t)
	print (tree)
	tree.inorder_tree_walk()