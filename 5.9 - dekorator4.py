def install_decorator(func):
    def wrapper():
        print("Please accept terms & conditions")
        func()

    return wrapper  # zwracamy adres w pamieci, a nie wywołac funkcje


def install_decorator2(func):
    def wrapper():
        print("Please enter correct licence key...")
        func()

    return wrapper


def install_decorator3(func):
    def wrapper():
        print("Please enter partitioning choice...")
        func()

    return wrapper


@install_decorator
def install_linux():
    print("Linux instalation has starded \n")


@install_decorator
def install_windows():
    print("Windows instalation has starded \n")


@install_decorator3
@install_decorator2
@install_decorator
def install_mac():
    print("Mac instalation has starded \n")


install_linux()
install_windows()
print("------")
install_mac()
# ------
# Please enter partitioning choice...
# Please enter correct licence key...
# Please accept terms & conditions
# Mac instalation has starded