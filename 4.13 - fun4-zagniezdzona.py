# funkcja zagnieżdżona (funkcja w funkcji)
# funkcja może słuzyc jako funkcja konfiguracyjna. dopiero funkcja wewnętrzna wykona zadanie po konfiguracja
# nie da się wywołac funkcji wew bez funkcji konfigurcyjnej
# zasada działania jest wykorzystywana w pythonie w dekoratorach

def fun1():
    print("To jest fun1")

    # definicja funkcji, czyli tu funkcja sie nie wykona (zapamięta adres)
    def fun2():
        print("To jest funkcja fun2")

    return fun2  # zwracamy adres funkcji a nie wynik działania funkcji,
    # fun2 sie tu nie wykona


fun1()  # To jest fun1
print("linijka 17:", fun1())  # To jest fun1
#  linijka 17: <function fun1.<locals>.fun2 at 0x00000166753D03A0>
xFun = fun1()
print("xFun:", xFun)  # <function fun1.<locals>.fun2 at 0x000002024DF203A0>
print(type(xFun))  # <class 'function'>
# jak uruchamiamy funkcję?
# nazwa funkcji i ()
xFun()  # To jest funkcja fun2
