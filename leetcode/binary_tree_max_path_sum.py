"""
I have used recursion based tree traversal to solve the problem
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class SearchTreeNode:
    
    def __init__(self,node_value,path_value=0,branch_value=0):
        self.node_value = node_value
        self.path_value = path_value
        self.branch_value = branch_value

class Solution:
    
    def _initialize_max_path_val(self):
        self.max_path_val = -9999
    
    def _probe_node(self,current_node):
        if current_node.val is None:
            return None
        elif current_node.left is None and current_node.right is None:
            if current_node.val > self.max_path_val:
                self.max_path_val = current_node.val
            #print("Max value after node iteration")
            #print(self.max_path_val)
            return SearchTreeNode(current_node.val,current_node.val,current_node.val)
        
        path_value = current_node.val
        branch_value = current_node.val
        
        if current_node.left is not None:
            searchnode = self._probe_node(current_node.left)
            if searchnode is not None:
                path_value = max(current_node.val,current_node.val + searchnode.branch_value)
                branch_value = max(branch_value,current_node.val + searchnode.branch_value)
                
        if current_node.right is not None:
            searchnode = self._probe_node(current_node.right)
            if searchnode is not None:
                path_value = max(path_value,path_value + searchnode.branch_value)
                branch_value = max(branch_value,current_node.val + searchnode.branch_value)
        
        #if current_node.val > path_value:
        #    path_value = current_node.val
        
        if path_value > self.max_path_val:
            self.max_path_val = path_value
        
        #print("Max value after node iteration")
        #print(self.max_path_val)
        return SearchTreeNode(current_node.val,path_value,branch_value)
    
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        self._initialize_max_path_val()
        node = self._probe_node(root)
        return self.max_path_val if self.max_path_val > -9999 else 0