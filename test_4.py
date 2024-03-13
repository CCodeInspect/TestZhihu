class A():
    def __init__(self,a):
        self.a = a
        
        
    def func(self,b):
        print(self.a+b)



a =A(a=2)


if __name__ =='__main__':
    a.func(1)        
