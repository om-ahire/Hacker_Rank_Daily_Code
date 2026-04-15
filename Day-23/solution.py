import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        #Write your code here
        # If the tree is empty, there is nothing to print
        if root is None:
            return
        
        # Initialize a queue with the root node
        queue = [root]
        
        # While there are still nodes to process
        while len(queue) > 0:
            # Pop the first node from the queue
            node = queue.pop(0)
            
            # Print the node's data
            print(node.data, end=" ")
            
            # Enqueue the left child if it exists
            if node.left:
                queue.append(node.left)
            
            # Enqueue the right child if it exists
            if node.right:
                queue.append(node.right)

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
