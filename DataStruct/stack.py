#This code is for making a stack using list

class mystack:
    def __init__(self):     #Defining a constuctor for mystack class
        self.data = []

    def length(self):           #to check the length
        return len(self.data)

    def isfull(self):           #to check if the stack is full
        if self.data == 5:
            return True
        else:
            return False

    def push(self, element):
        if len(self.data) < 5:
            self.data.append(element)
        else:
            print("overtflow")

    def pop(self):
        if len(self.data) == 0:
            print("underflow")
        else:
            return self.data.pop()


a = mystack()
a.push(9)
a.push(19)
print(a.data)
print(a.isfull())
a.push(874)
a.push(23)
a.push(645)
a.push(8778)
print(a.data)
print(a.pop())
print(a.pop())
print(a.pop())
print(a.pop())
print(a.pop())
print(a.pop())