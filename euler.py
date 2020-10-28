import time

def y_hat(x, y):
    return x + y + x * y


def euler(x0, y, h, x, f):
    temp = -0
    while x0 < x:
        temp = y
        y = y + h * f(x0, y)
        x0 += h
    return y


if __name__ == '__main__':
    x0 = 0
    y0 = 1
    h = 0.025
    x = 0.1
    print(euler(x0, y0, h, x, y_hat))
