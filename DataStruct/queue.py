#This progrsamm is to make a queue uing lists

class myqueue:
    def __init__(self):
        self.data =  []

    def length(self):
        return len(self.data)

    def enqueue(self, element):
        if len(self.data) < 5:
            self.data.append(element)
        else:
            print("Overflow")

    def dequeue(self):
        if len(self.data) == 0:
            print("Underflow")
        else:
            self.data.pop()


a = myqueue()
a.enqueue(90)
a.enqueue(30)
a.enqueue(0)
a.enqueue(90)
a.enqueue(90)
a.enqueue(90)
print(a.data)
a.dequeue()
print(a.data)
a.dequeue()
a.dequeue()
a.dequeue()
a.dequeue()
a.dequeue()