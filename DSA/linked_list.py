class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

     

    def insert_first(self,value):
        first_node = Node(value)
        if self.head is None:
            self.head = first_node
            return 
        else:
            first_node.next = self.head
            self.head = first_node


    def insert_last(self,value):
        end_node = Node(value)
        if self.head is None:
            self.head = end_node
            return

        current_node = self.head
        while(current_node.next is not None):
            current_node = current_node.next
        current_node.next = end_node

    def insert_multi(self, tup: tuple):
        for t in tup:
            self.insert_last(t)


    def get_at_index(self, index) -> Node:
        current_node = self.head
        position = 0
        while current_node and index!=position:
            current_node = current_node.next
            position+=1
        return current_node

    def insert_at_index(self, index, value):
        if(index>0):
            prev_node = self.get_at_index(index-1)
            new_node = Node(value)
            new_node.next = prev_node.next
            prev_node.next = new_node
        else:
            self.insert_first(value)

    def update_node(self, index, value):
        node = self.get_at_index(index)
        node.value = value

    def delete_first(self):
        if self.head is not None:
            self.head = self.head.next
        return
    
    def delete_last(self):
        if self.head is not None:
            current_node = self.head
            while (current_node.next.next != None):
                current_node = current_node.next
            current_node.next = None
        return
        
    def delete_node(self, index):
        if(index==0):
            self.delete_first()
        else:
            current_node = self.head
            # while(current_node.)


    def size_of(self):
        current_node = self.head
        len = 0

        while(current_node):
            len+=1
            current_node = current_node.next
        return len 

    def printL(self):
        current_node = self.head
        print()
        print("H")
        print("↓")
        while (current_node.next):
            print(current_node.value, end= "->")
            current_node = current_node.next
        print(current_node.value, end="\n")
        print()
    

llist = LinkedList()

llist.insert_first('a')
llist.insert_last("b")
llist.insert_multi(("a","b","c"))
llist.insert_at_index(0,"j")
llist.insert_at_index(2,"z")
llist.update_node(2,"o")
llist.printL()

llist.delete_first()
llist.printL()

llist.delete_last()
llist.printL()
