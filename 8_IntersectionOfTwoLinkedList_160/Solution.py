class Node: 
    def __init__(self, val , next= None):
        self.val = val
        self.next = next

class LinkedList:

    def __init__(self):
        self.head = None
    
    def addNode(self,val):
        if self.head == None:
            self.head = Node(val)
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(val)
    
    def showList(self):
        curr = self.head
        while curr:
            print(curr.val , end = ' ')
            curr = curr.next

def getIntersectionNode(headA: Node, headB: Node) -> Node:
    if not headA or not headB:
        return None
    xPtr = headA
    yPtr = headB

    while xPtr != yPtr:
        if xPtr:
            xPtr = xPtr.next
        else:
            xPtr = headB
        if yPtr:
            yPtr = yPtr.next
        else:
            yPtr = headA
    return xPtr # or return yPtr, since both are same