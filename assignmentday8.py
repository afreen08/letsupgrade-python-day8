#fibonacci
def fib(n):
    a=0
    b=1
    print(a)
    print(b)
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        print(c)
    def fib_seq(func):
        def inner(a,b):
            if a>b:
                a,b=b,a
                print(func(a,b))
        return inner
k=fib-seq(fib)
fib(10)
