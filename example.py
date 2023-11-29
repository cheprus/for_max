from random import *

hp = 10
some_variable = 5


def meet_monster(_hp, _var):
    meet = randint(1, _var)

    if meet == 1:
        _hp -= 1
        i = 0
        while True:
            i += 1
            print('    Вечный цикл #2: ', i)
            if (i >= 10):
                print("Exit from #2")
                exit()
    else:
        # Зачем ты отнимаешь тут _var = 1000-1 ?
        _var -= 1
    return _var


n = 0
while True:
    n += 1
    variable = meet_monster(hp, some_variable)
    print("Вечный цикл #1:", variable)

    if (n >= 10):
        print("Exit from #1")
        exit()
