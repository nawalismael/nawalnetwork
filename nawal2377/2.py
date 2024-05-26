def Func(b):
    dec=0
    try:
        for i in range(len(b)):
            t= int(b[i])
            dec += t * 2**(len(b)-i-1)
        return dec
    except Exception as e:
        print(e)
while True:
    b=input("Input an binary Input x to exit: ")
    if b=='x':
        break
    d=Func(b)
    print(d)
