def test(a):
    del a[-1]
    print x
    print arr


arr = [1,2,3,4]
x = arr
test(x)
print x
print arr
