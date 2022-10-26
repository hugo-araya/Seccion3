from re import I


def leibniz(n):
    pi4 = 0
    i = 0
    while i < n:
        pi4 = pi4 + ((-1)**i)/(2*i + 1)
        i = i + 1
    return pi4*4

def wallis(n):
    pi2 = 1
    i = 1
    while i <= n:
        pi2 = pi2 * ((2*i)/(2*i-1))*((2*i)/(2*i+1))
        i = i + 1
    return pi2*2

def fact(n):
    f = 1
    i = 1
    while i <= n:
        f = f * i
        i = i + 1
    return f

def euler(n):
    pi2 = 0
    i = 0
    while i < n:
        pi2 = pi2 + 2**i*fact(i)**2/fact(2*i + 1)
        i = i + 1
    return pi2*2

if __name__ == '__main__':
    n = 5000
    print(leibniz(n))
    print(wallis(n))
    print(euler(n))

