#stack implementation with functions
# Passing list isn't a coolest idea checkout stack_class for class based implementation

def main():
    stack = []
    push(stack,6)
    push(stack,3)
    x= pop(stack)
    print(f'popped: {x}')
    
def push(stack, x):
    stack.append(x)

def pop(stack):
    print(stack)
    return stack.pop()

if __name__ == '__main__': main()  