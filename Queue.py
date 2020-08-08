#Queue behave mostly like lists, so we are going to make use of lists as a base for our class 'Queue' 

class Queue(object):

    #Setting 'items' attribute as a empty list as base for our queue
    def __init__ (self):
        self.items = []

    #Returns a boolean for items if equal empty list. 
    def isEmpty(self):
        return self.items == []

    #Making use of insert function from lists to push an element in index 0 of our queue. 
    def enqueue(self, item):
        self.items.insert(0,item)

    #Making use of pop function from lists. 
    def dequeue(self):
        return self.items.pop()
    
    #Returns length of 'items' attirbute of our queue class. 
    def size(self):
        return len(self.items)

#This highlights how lists are versatile with inbuilt functions 'insert' and 'append' 
