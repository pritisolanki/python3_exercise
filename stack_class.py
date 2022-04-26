#Stack implementation using list
class Stack:
    stk = []

    def push(self,x):
        self.stk.append(x)

    def pop(self):
        return self.stk.pop()

#print stack 
def print_stack(stack):
    for item in stack.stk:
        print(f'Item: {item}')    

def main():
    stack = Stack()
    for x in range(1, 20,3):
        stack.push(x)
    print_stack(stack)
    poppedItem = stack.pop()
    print(f'Item popped: {poppedItem}')

if __name__ == '__main__' : main()
