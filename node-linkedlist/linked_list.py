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
        count = 0
        if cur_node.value is False:
            print(None)
        elif cur_node.next is None:
            print(cur_node.value)
        else:
            while cur_node.next is not None:
                count +=1
                cur_node = cur_node.next
                if count == 1:
                    print(cur_node.value)
                    break
        # print(cur_node.value)
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
        if cur_node.value is False:
            print(None)
        elif cur_node.next is None:
            print(cur_node.value)
        else:
            while cur_node.next is not None:
                cur_node = cur_node.next
                if cur_node.next is None:
                    print(cur_node.value)
                    break
        
    def get_list(self):
        # create list and append every value of Linked List to it.
        # return the list
        lst = []
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
            lst.append(cur_node.value)
        print(lst)

# my_list = LinkedList()


# my_list.get_list()
# my_list.get_last()
# my_list.get_head()
