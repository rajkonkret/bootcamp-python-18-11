def allparams(a, b, /, c, **kwargs):
    print(a, b, c)
    print(kwargs)


allparams(1, 2, 3)
allparams(1, 2, c=5)
# po dodaniu /, argumenty a i b nie mogą zostać podane po nazwie
# allparams(a=1, b=2, c=3)  # TypeError:
# allparams() got some positional-only arguments passed as keyword arguments: 'a, b'
allparams(1, 2, c=7, a=9)


# 1 2 7
# {'a': 9}
# gdy nie ma / zadziała
# allparams(a=1, b=2, c=3)

def allparams_all(a, b, /, c=43, *args, d=256, **kwargs):
    print("a, b", a, b)
    print("c, d", c, d)
    print(args)
    print(kwargs)


allparams_all(1, 2)  # a, b 1 2
allparams_all(1, 2, c=7)  # c, d 7 256
allparams_all(1, 2, 3)  # c, d 3 256
# gdy chcemy przekazac argsy w tym przypadku c musi byc przekazane po pozycji
allparams_all(1, 2, 7, 1, 2, 3, 4, 5, 6, 7)  # (1, 2, 3, 4, 5, 6, 7) c, d 7 256
# d jest po argsach, wiec musi byc podane po nazwie
allparams_all(1, 2, 3, 1, 2, 3, 4, 5, 6, d=100)  # c, d 3 100
allparams_all(1, 2, 3, 1, 2, 3, 4, 5, 6, d=100, name="Radek")  # {'name': 'Radek'}
allparams_all(1, 2, 3, 1, 2, 3, 4, 5, 6, d=100, name="Radek", a=7)  # {'name': 'Radek', 'a': 7}
