class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
        # initialize Node with value, and next being None

class LinkedList:
    def __init__(self, head = None):
        # initialize Linked List by initializing head
        self.head = head
    
    def get_head(self):
        # return head of the Linked List
        cur = self.head
        count = 0
        while cur.next != None:
            count +=count
            if count == 1:
                return(self.head)
            break
        return(self.head)
    def insert_back(self, node):
        # insert node to the back of the Linked List
        new_node = Node(node)
        if self.next == None:
            self.next = new_node
    def get_last(self):
        # return last node of the Linked List
        cur = self.head
        while cur.next == None:
            return(self.head)
    def get_list(self):
        # create list and append every value of Linked List to it.
        # return the list
        lst = []
        cur = self.head
        while cur.next != None:
            lst.append(cur.next)
        return(lst)
            
