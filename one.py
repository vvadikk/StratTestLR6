#Вариант 19
from fnmatch import fnmatch

def create_sp1():
    sp1 = []
    n = 2092
    for i in range(0, 10 ** 9 + 1, n):
        if fnmatch(str(i), '2?*479?2'):
            sp1.append(i // n)
    return sp1

if __name__ == '__main__':
    print(create_sp1())
