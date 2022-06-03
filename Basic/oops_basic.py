class Car:
    def __init__(self,height,length,engine) -> None:
        self.height = height
        self.length = length
        self.engine = engine
    
    def __str__(self) -> str:
        return(f'Car :{self.engine},{self.height}{self.length}')

def main():
    audi = Car(140,143,'Audi 3.2L 6 cylinder 250hp 236ft-lbs')
    print(audi)

if __name__ == '__main__': main()
