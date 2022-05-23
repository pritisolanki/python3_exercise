#Stack implementation using list
class Stack:
    def __init__(self):
        self.stack=[]

    def push(self,item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

#print stack 
def print_stack(list_stack):
    for item in list_stack.stack:
        print(f'Item: {item}')    

def main():
    stack = Stack()
    for x in range(1, 20,3):
        stack.push(x)
    print_stack(stack)
    poppedItem = stack.pop()
    print(f'Item popped: {poppedItem}')

if __name__ == '__main__' : main()
