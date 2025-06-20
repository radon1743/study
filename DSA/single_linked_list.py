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
            return
        elif index == self.size_of():
            self.delete_last()
        else:
            current_node = self.head.next
            position = 1
            while(current_node.next):
                if index == position+1:
                    current_node.next = current_node.next.next
                    return
                position+=1
                current_node = current_node.next

    def reverse(self):
        current_node = self.head
        prev = None


        while current_node:
            next_node = current_node.next

            current_node.next = prev

            prev = current_node
            current_node = next_node
        
        self.head = prev 



    def size_of(self):
        current_node = self.head
        len = 0

        while(current_node):
            len+=1
            current_node = current_node.next
        return len 

    def printL(self):
        current_node = self.head
        if (current_node):
            print()
            print("H")
            print("↓")
            while (current_node.next):
                print(current_node.value, end= "->")
                current_node = current_node.next

            print(current_node.value, end="\n")
            print()
        else:
            print(self.head)



def add_node(l1,l2,c):

    if not (l1 or l2) and c == 0:
        return None


    l1_val = l1.value if l1 else 0 
    l2_val = l2.value if l2 else 0 

    sum = l1_val + l2_val + c
    
    h = Node( sum%10 )
    h.next = add_node(l1.next if l1 else None,l2.next if l2 else None,sum//10)     

    return h

def add_linked_lists(l1,l2):

    h1 = l1.head
    h2 = l2.head
    r = LinkedList()
    c = 0  
    while h1 or h2:
        if h1 and h2:
            sum = h1.value + h2.value
            h1, h2 = h1.next, h2.next 
        elif h1:
            sum = h1.value
            h1 = h1.next
        else:
            sum = h2.value
            h2 = h2.next

        r.insert_last(sum%10 + c)
        c = sum//10
    if c >0:
        r.insert_last(c)
    r.printL()

def remove_n_node(head, n):
    front = head
    back =  head
    i = 0
    while front.next and i<n:
        front = front.next
        i+=1



    while front.next:
        back = back.next
        front = front.next
    if back.next == front or back == front:
        if n == 1:
            return back.next
        elif n ==2:
            return front
    back.next = back.next.next

    return head        

def merge_nodes(l1,l2):

    if not l1:
        return l2
    if not l2:
        return l1

    if l1.value < l2.value:
        l1.next = merge_nodes(l1.next,l2)
        return l1
    else: 
        l2.next = merge_nodes(l1,l2.next)
        return l2

def swap_pair(head):
    current_head = head.next
    head.next = current_head

    while current_head.next:
        current_head = head.next
        head.next = current_head

        current_head = current_head.next
        head = head.next
    return current_head



if __name__=="__main__":
    list1 = LinkedList()
    list1.insert_multi((1,2,3,4))
    list1.printL()
    
    list2 = LinkedList()
    list2.printL()

    list2.head = swap_pair(list1.head)
    list2.printL()

