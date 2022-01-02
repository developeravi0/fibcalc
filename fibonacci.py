def fibcalc():
    print("Activted fibonacci number calculator")
    #0,1,b,2,3,5,8,13,21,34,55
    def fibonacci(n):
        a=0
        b=1
        if n==1:
            print(a)
        else:
            print(a)
            print(b)
            for i in range(2,n):
                c=a+b
                a=b
                b=c
                print(c)
    number=int(input("Enter the number of fibonacci numbers you wanna generate : "))
    fibonacci(number)
    print("Exited fibonacci number calculator")
if __name__=="__main__":
    fibcalc()