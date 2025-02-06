def fun(x):
    if (x==0):
        return
    fun(x-1)
    print(x)
x=5
fun(x)
