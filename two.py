from one import create_sp1

def f1(x):
    return (8 - x ** 2) / (x + 7)
def f2(x, y):
    return x + y - z
def f3(s):
    return len(s)
def f4(l):
    even = [i for i in l if i % 2 == 0]
    odd = [i for i in l if i % 2 != 0]
    even_avrg = sum(even) / len(even)
    odd_avrg = sum(odd) / len(odd)
    return even_avrg > odd_avrg
def f5(x):
    if x != 1 or x != 0: #всегда True
        return True
    return False

if __name__ == '__main__':
    l = create_sp1()
    #print(f1(-7))
    #print(f2(2, 2))
    #print(f3(333))
    print(f4(l))
    print(f5(5))