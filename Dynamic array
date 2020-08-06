
import ctypes

#Attributes n and capacity are the actual count and capacity of elements in array.
#We'll build the make_array method later on.
class DynamicArray(object):
    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity)


 #returns the count of elemnts (getter) 
    def __len__(self):
        return self.n

#Checks if k is between 0 and count of elements and 
#returns the element at index 'k' of array 'A'
    def __getitem__(self,k):
        if not 0 <= k < self.n:
            return IndexError('K is out of bounds!')
        return self.A[k]

#Check count of A against capacity and if it's equal we resize(to be built later)
#We add an element at A[n] and increase the count by 1. 
    def append(self,ele):
        if self.n == self.capacity:
            self._resize(2*self.capacity) 
        self.A[self.n] = ele
        self.n += 1     

 #Temporary array B is created using make_array(to be built later) 
 #Re-referencing elements from A into this new array B.
    def _resize(self,new_cap):

        B = self.make_array(new_cap)

        for k in range(self.n):
            B[k] = self.A[k]

        self.A = B
        self.capacity = new_cap

#We use ctypes library to make a new array. 
    def make_array(self,new_cap):
        return (new_cap * ctypes.py_object)() 

