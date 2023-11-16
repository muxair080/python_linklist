

class Node():
    def __init__(self, name, age, address):
        self.name = name
        self.age  = age
        self.address = address
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None 
    
    def insert_at_head(self, name, age, address):
        """
        This method will new node or data at the start of 
        the linkedlist.
        """
        new_node = Node(name, age, address)
        if self.head is None:
            self.head = new_node
            
        else:
            new_node.next = self.head
            self.head = new_node
        
        print("New node inserted at head")

    def insert_at_end(self, name, age, address):
        """
        This method will insert new node at the
        end of linked list.
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while(current_node.next):
                current_node = current_node.next
            current_node.next = new_node
        print("New node inserted at the end of linked list")
    
    def insert_at_index(self, name, age,address, index):
        new_node = Node(name, age, address)
        current_node = self.head 
        position =  0
        if position == index:
            self.insert_at_head(name, age, address)
        else:
            while current_node !=None and position+1 != index:
                possition = position+1
                current_node = current_node.next
            
            if current_node !=None:
                new_node.next = current_node.next
                current_node.next = new_node
            else:
                print("Index not present")

    def update_node(self, name, age, address, index):
        current_node = self.head
        position = 0
        if position == index:
            current_node.name = name
            current_node.age = age 
            current_node.address = address
        else:
            while current_node != None and position !=index:
                position +=1
                current_node = current_node.next
            if current_node !=None:
                current_node.name = name
                current_node.age = age
                current_node.address  = address
            else:
                print("Index not present")

    def remove_first_node(self):
        """
        This method will remove the first 
        node from the linked list.
        """
        if self.head == None:
            return
        self.head = self.head.next
        print("First node removed from head")
    
    def remove_last_node(self):
        if self.head is None:
            print("Linked list is empty")
            return
        
        current_node = self.head 

        while current_node.next.next:
            current_node = current_node.next
        current_node.next = None
        print("last node removed")

    def print_link_list(self):
        """
        this method will print linked list data
        """
        current_node = self.head
        while (current_node):
            print('-----------------')
            print(f"Name : {current_node.name}")
            print(f"Age : {current_node.age}")
            print(f"address : {current_node.address}")
            current_node = current_node.next
    
    def remove_at_index(self, index):
        if self.head == None:
            return
        
        current_node = self.head 
        position = 0
        if position == index:
            self.remove_first_node()
        else:
            while current_node !=None and position+1 !=index:
                position +=1
                current_node = current_node.next
            
            if current_node !=None:
                current_node.next = current_node.next.next
                print(f"Node removed at index {index}")
            else:
                print("Index not present")
                   
    def size_of_list(self):
        size=0
        if self.head:
            current_node = self.head 
            while (current_node):
                size +=1
                current_node = current_node.next
            return size
        else:
            return size
    

# create class object
link_list = LinkedList()
link_list.insert_at_head("uzair",23,"charsadda")
link_list.insert_at_head("yasir",23,"bunner")
link_list.insert_at_head("juniad",23,"peshawar")
link_list.insert_at_head("yasir",23,"peshawar")
link_list.insert_at_head("saad",23,"islamabad")
link_list.insert_at_head("irshad",23,"swat")
link_list.insert_at_head("israr",23,"waziristan")
link_list.insert_at_index("wajid", 23, "swaat",1)
# link_list.print_link_list()
link_list.update_node("wajid", 23, "kabal",1)
# link_list.remove_first_node()
# link_list.remove_last_node()
link_list.remove_at_index(2)
# link_list.print_link_list()
print("Size of linked list : ",link_list.size_of_list())