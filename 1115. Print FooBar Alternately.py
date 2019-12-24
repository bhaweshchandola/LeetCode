import time
class FooBar:
    def __init__(self, n):
        self.n = n
        self.fir = False
        self.sec = True


    def foo(self, printFoo: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            
            
            # print("foo",i)
            while not self.sec:
                time.sleep(0.0001)
            # printFoo() outputs "foo". Do not change or remove this line.    
            printFoo()
            self.fir = True
            self.sec = False
            


    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            
            # print("bar",i)
            while not self.fir:
                time.sleep(0.0001)
            
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.sec = True
            self.fir = False