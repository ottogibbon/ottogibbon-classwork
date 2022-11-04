q=[]
size = 8
# If the the queue is not full an element is added
def enQueue():
    if len(q)==size:
        print("Queue is Full!")
    else:
        element=input("Enter the element:")
        q.append(element)
        print(element,"is added to the Queue!")

# If the queue is not empty element id removed      
def deQueue():
    if not q:
        print("Queue is Empty!")
    else:
        e=q.pop(0)
        print("element removed!",e)


# Returns true if there is no space in the queue
def isFull():
    return not hasSpace()


# Returns true if there is space in the queue
def hasSpace():
    if size < 8:
        return True
    else:
        return False

# Main program


enQueue()
enQueue()
deQueue()
deQueue()
deQueue()

