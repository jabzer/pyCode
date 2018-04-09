from command import MyObject
comuter = MyObject()
def run(x):
    inp=input('method>')
    if hasattr(comuter,inp):
        func = getattr(comuter,inp)
        print(func())
    else:
        setattr(comuter,inp,lambda x:x+1)
        func = getattr(comuter,inp)
        print(func(x))

if __name__=='__main__':
    run(10)