def outer_function():
    print(1)
    def inner_function():
        print('in')
    print('before call in')
    inner_function()
    print('out')


outer_function()
print('normal')