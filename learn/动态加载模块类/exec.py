from command import MyObject
computer = MyObject()

def run():
    inp = input('method >')

    if inp =='add':
        print(computer.add())
    elif inp =='sub':
        print(computer.sub())
    elif inp =='div':
        print(computer.div())
    elif inp =='pow':
        print(computer.pow())
    else:
        print('404')

if __name__=='__main__':
    run()