class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data):
        # Create the new node with the given data
        new_node = Node(data)
        
        # Case 1: The list is empty
        if head is None:
            return new_node
        
        # Case 2: The list is not empty
        current = head
        # Iterate until we reach the last node
        while current.next:
            current = current.next
        
        # Point the last node's next to the new node
        current.next = new_node
        
        # Return the original head of the list
        return head
    #Complete this method

mylist= Solution()
