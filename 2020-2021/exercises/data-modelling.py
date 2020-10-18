'''
- Code a class that represents a binary tree, which is a tree data structure in which each node has at most two children, which are referred to as the left child and the right child. Each node is a class that contains a value.
  
- The class for a binary tree provides methods for:
  - computing the height of the tree
  - counting the number of nodes
  - adding new nodes by automatically checking where it is possible to add a new node in the binary tree
  - removing nodes

- The class for a node provides methods for:
  - getting/setting/removing a value for the node
  - getting/setting/removing left/right child
  - checking if the left/right child is available
'''


class BinaryTree:

    def __init__(self, node=None):
        # We check that the node passed as input is an instance of the class Node
        if isinstance(node, Node) or node is None:
        	self.root = node
        	
    def height(self):
    	if self.root is None:
    		return 0
    	else:
    		return 1 + max(self.__height(self.root.left_child),
    			    self.__height(self.root.right_child))
    			
    def __height(self, node):
    	if node is None:
    		return 0
    	else: 
    		return 1 + max(self.__height(node.left_child),
    			    self.__height(node.right_child))
    		
    def count(self):
    	return self.__count(self.root)
    	
    def __count(self, node):
    	if node is None:
    		return 0
    	else:
    		return 1 + self.__count(node.left_child) + self.__count(node.right_child)
            
    def add(self, node):
    	if self.root is None:
    		self.root = Node(node, None, None)
    	else:
    		self.__add(self.root, Node(node, None, None))
    		
    
    def __add(self, current_node, new_node):
    	if new_node.value <= current_node.value:
    		
    		if current_node.left_child is None:
    			current_node.left_child = new_node
    		else:
    			self.__add(current_node.left_child, new_node)
    	else:
    		if current_node.right_child is None:
    			current_node.right_child = new_node
    		else:
    			self.__add(current_node.right_child, new_node)
    			
    def remove(self, node):
    	if self.root is None:
    		return None
    	else:
    		self.__remove(None, self.root, node, False)
    	
    def __remove(self, parent_node, current_node, node, is_left):
    	if current_node.value == node:
    		if parent_node is not None:
    			if is_left:
    				parent_node.left_child = None
    			else:
    				parent_node.right_child = None
    		else:
    			binary_tree.root = None

    		return current_node
    	else:
    		ret = None
    		if current_node.left_child is not None:
    			ret = self.__remove(current_node, current_node.left_child, node, True)
    		if ret is None and current_node.right_child:
    			return self.__remove(current_node, current_node.right_child, node, False)
    		else:
    			return ret
    			
    def visit(self):
        if self.root is not None:
            return self.__visit(self.root.left_child) + [self.root.value] + self.__visit(self.root.right_child)
        else:
            return []
        
            
    def __visit(self, node):
        if node is not None:
            return self.__visit(node.left_child) + [node.value] + self.__visit(node.right_child)
        else:
            return []
    

class Node:
    def __init__(self, value, lc, rc):
    	self.value = value
    	self.left_child = lc
    	self.right_child = rc
    	
    def get_value(self):
    	return self.value
    	
    def set_value(self, new_value):
    	self.value = new_value
    	
    def has_left_child(self):
    	if self.left_child is None:
    		return False
    	else:
    		return True
    		
    def has_right_child(self):
    	if self.right_child is None:
    		return False
    	else:
    		return True
    		
    def get_left_child(self):
    	return self.left_child
    	
    def set_left_child(self, new_left):
    	if isinstance(new_left, Node):
    		self.left_child = new_left
    	
    def get_right_child(self):
    	return self.right_child
    	
    def set_right_child(self, new_right):
    	if isinstance(new_right, Node):
    		self.right_child = new_right
    		
    
if __name__ == '__main__':
	
	#root = Node(2, Node(7, None, Node(6, None, None)), Node(5, None, Node(9, Node(4, None, None), None)))
	binary_tree = BinaryTree()
	binary_tree.add(5)
	binary_tree.add(7)
	binary_tree.add(3)
	binary_tree.add(9)
	binary_tree.add(4)
	binary_tree.add(2)
	binary_tree.add(1)
	print("The root is ", binary_tree.root)
	print("The binary tree is ", binary_tree)
	
	height = binary_tree.height()
	print("The height of the tree is ", height)
	
	n_nodes = binary_tree.count()
	print("The number of nodes in the tree is ", n_nodes)
	print(binary_tree.visit())
	
	print("We now insert a new node whose value is 8")
	binary_tree.add(8)
	
	print("The number of nodes in the tree is now ", binary_tree.count())
	
	print(binary_tree.visit())
	
	binary_tree.remove(7)
	print("Binary tree after the removal of node 7")
	print(binary_tree.visit())
	