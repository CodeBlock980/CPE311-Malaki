# -*- coding: utf-8 -*-

'''
The Tower of Hanoi Problem

Approach:
1. Using Stack to represent the peg. Peg A will have 3 elements inside (disks 1,2,3), while Peg B and C will have None.
2. There will be a base case where if there is only one move, the disk moves from source to destination peg
3. If there are multiple disks to move then it is the recursive case.

'''
#Create a stack class
class Stack(object):
  def __init__(self):
    self.stack = []

  def push(self ,data): #Push Items in the Stack
    return self.stack.append(data)

  def pop(self):
    if len(self.stack) == 0: #Remove last element added in the Stack
      raise KeyError("Stack is Empty")
    return self.stack.pop()


  def display(self): #Display all the elements in the stack
    return self.stack

  def getLength(self): #Return the length of the stack
    return len(self.stack)


def moveTo(n, source, middle, dest):
  if n == 1: #Base Case, if there is only one move, then move it to the peg C
    disk = source.pop()
    dest.push(disk)
    print("Move Disk", disk, "from" , source.display(), "to" , dest.display())
  else:
    moveTo(n-1, source, dest, middle)
    disk = source.pop()
    dest.push(disk)
    print("Move Disk", disk, "from" , source.display(), "to" , dest.display())
    moveTo(n-1, middle, source, dest)







pegA = Stack()
pegA.push(3)
pegA.push(2)
pegA.push(1)
pegB = Stack()
pegC = Stack()
moveTo(3, pegA, pegB, pegC)








