def fun1() :
    print("* ")
def fun2(a) :
    print("* * ")
    a()

fun2(fun1)