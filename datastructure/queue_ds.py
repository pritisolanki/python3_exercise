#Queue implementation using list

class Queue():
    def __init__(self):
        self.queue=[]
    
    def is_empty(self):
        return not len(self.queue)
    
    def print_queue(self):
        print(self.queue)

    def enqueue(self,element):
        self.queue.append(element)
    
    def dequeue(self):
        if(self.is_empty()):
            raise "Warning: Queue empty"
        return self.queue.pop(0)

def main():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.print_queue()
    item1= queue.dequeue()
    print(item1)
    item2 = queue.dequeue()
    print(item2)

if __name__ == '__main__' : main()

