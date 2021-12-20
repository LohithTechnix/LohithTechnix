class Node():
    def __init__(self,data):
        self.data=data
        self.next=None

class Linked():
    def __init__(self):
        self.head=None
    
    def add_first(self,data):
        new = Node(data)
        new.next=self.head
        self.head=new
    
    def add_last(self,data):
        new = Node(data)
        temp=self.head
        while temp.next!=None:
            temp=temp.next
        temp.next=new

    def delete(self,data):
        temp=self.head
        prev = self.head
        while temp.next!=None:
            prev=temp
            if temp.data==data:
                old = temp.next
                prev.next=old
                return
            temp=temp.next
        if temp.data==data:
            old = temp.next
            prev.next=old
            return
        else:
            print("Data not found")

    def display(self):
        temp=self.head
        while temp!=None:
            print(temp.data)
            temp=temp.next
ll=Linked()
ll.add_first(3)
#ll.display()
print("============================")
ll.add_first(2)
#ll.display()
print("============================")
ll.add_first(1)
#ll.display()
print("============================")
ll.add_last("added last")
ll.display()
print("============================")
ll.delete(3)
ll.display()
print("============================")
ll.delete(0)
ll.display()