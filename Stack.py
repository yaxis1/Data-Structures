#Stacks behave mostly like lists, so we are going to make use of lists as a base for our class 'Stack' 

class Stack(object):

    #Setting 'items' attribute as a empty list as base for our stack
    def __init__ (self):
        self.items = []

    #Returns a boolean for items if equal empty list. 
    def isEmpty(self):
        return self.items == []

    #Making use of append function from lists to push an element into our stack. 
    def push(self, item):
        self.items.append(item)

    #Making use of pop function from lists. 
    def pop(self):
        return self.items.pop()

    #Returns the last element without chaning the original stack.
    #Using slicing from lists.
    def peek(self):
        return self.items[-1]
        #or
        #return self.items[len(self.items)-1]

    #Returns length of 'items' attirbute of our stack class. 
    def size(self):
        return len(self.items)


#This shows how stacks are not flexible like lists due to their LIFO behaviour
