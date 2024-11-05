class Node:
    # Node constructor
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

class LinkedList:
    # Linked List constructor     
    def __init__(self):
        self.head = None  

    def addLast(self, data):
        new_node = Node(data) 
       # If we don't have, we make new node the head
        if self.head is None:
            self.head = new_node
            return
        # If we already have a head, then we add it to the last node
        current = self.head
        while current.next:
            current = current.next
        
        current.next = new_node

    # My Solution: 
def removeNthModeFromEndOfList(head: Optional[Node] ,n: int) -> Optional[Node]:
    p = head
    q = head
    counter = 0
    while q:
        q = q.next
        counter += 1
        
    if counter == n:
        return head.next

    for _ in range (0,counter-n-1):
        p = p.next
        
    p.next = p.next.next
    return head   
    
def otherSolution(head: Optional[Node] ,n: int) -> Optional[Node]:
    leftPointer = head
    rightPointer = head

    while n > 0:
        rightPointer = rightPointer.next
    
    while rightPointer and rightPointer.next:
        rightPointer = rightPointer.next
        leftPointer = leftPointer.next
    
    if leftPointer == head and rightPointer == None:
        return head.next
    
    leftPointer = leftPointer.next

    return head