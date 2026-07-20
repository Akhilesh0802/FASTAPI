def test():
    print("Start")
    yield "Hello"
    print("End")

x = test()

print(next(x))

next(x)