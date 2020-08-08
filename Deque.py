#Deque is similar to queue with both ends front and rear.

class Deque(object):

    #Setting 'items' attribute as a empty list as base for our Deque
    def __init__ (self):
        self.items = []

    #Returns boolean for items equal empty list.
    def isEmpty(self):
        return self.items == []

    #Append puts the item at the very end i.e at front of Deque.
    def addFront(self, item):
        self.items.append(item)

    #Insert puts the item at rear i.e at rear of Deque
    def addRear(self, item):
        self.items.insert(0,item)

    #Pop removes the very end item i.e front for Deque
    def removeFront(self):
        return self.items.pop()

    #Pop([-1]) removes the first item i.e rear for Deque
    def removeRear(self, item):
        self.items.pop(0)
        
    #Returns length of 'items' attirbute of our Deque class. 
    def size(self):
        return len(self.items)

#Deques are a bit flexible compared to queue and stack, 
#elements can be added or removed from either front or rear. 
