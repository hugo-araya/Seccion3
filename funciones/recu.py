def recu(n):
    print(n)
    if n == 0:
        return n
    else:
        return recu(n-1)

if __name__ == '__main__':
    print(recu(2000))
