#creation of nodes

class names:
    def __init__(self, dataval = None):
        self.dataval = dataval
        self.nextval = None

    
e1 = names("Fuck")
e2 = names("shit")
e3 = names("bitch")

e1.nextval = e2
e2.nextval = e3

thisval = e1

while thisval:
    print(thisval.dataval)
    thisval = thisval.nextval
