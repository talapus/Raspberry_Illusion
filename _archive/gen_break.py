def gen(base):
    for item in base:
        if item%3 == 0:
           break
        yield i

for i in gen(range(1, 100)):
    print("Pass,{}".format(i))