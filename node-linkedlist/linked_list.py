class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
        # initialize Node with value, and next being None

class LinkedList:
    def __init__(self, head = None):
        # initialize Linked List by initializing head
        self.head = Node()
        
    
    def get_head(self):
        # return head of the Linked List
        cur_node = self.head
        cur_node = cur_node.next
        return(cur_node.value)
        
    def insert_back(self, node):
        # insert node to the back of the Linked List
        
        new_node = Node(node)

        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
        cur_node.next= new_node
        # print(cur_node)
    def get_last(self):
        # return last node of the Linked List
        cur_node = self.head
        while cur_node.next is not None:
        	cur_node = cur_node.next
        
        return(cur_node.value)
        
    def get_list(self):
        # create list and append every value of Linked List to it.
        # return the list
        lst = []
        cur_node = self.head
        while cur_node.next is not None:
            
            cur_node = cur_node.next
            val = cur_node.value
            lst.append(val)
        return(lst)

my_list = LinkedList()

my_list.insert_back(4)
my_list.insert_back(3)
my_list.insert_back(1)
my_list.insert_back(2)

my_list.insert_back(4)
my_list.insert_back(3)
my_list.insert_back(1)
my_list.insert_back(2)

my_list.insert_back(4)
my_list.insert_back(3)
my_list.insert_back(1)
my_list.insert_back(2)
print(my_list.get_list())
print(my_list.get_head())
print(my_list.get_last())
