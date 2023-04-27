def black_hole(*args):
    print(type(args))
    print(args)
    for argument in args:
        print(argument)
black_hole(256, 'Name', 'adress', '2*5', 2 * 5)