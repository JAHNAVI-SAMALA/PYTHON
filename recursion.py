def fun(x):
    if (x==0):
        return
    print(x)
    fun(x-1)
x=5
fun(x)
