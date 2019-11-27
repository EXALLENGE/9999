def f42(x):
    if x == 42:
        print("Вы угадали")
        str = "Win"
    else:
        print("Попробуйте еще")
        str = "Lose"
    return str

x = float(input())
f42(x)
