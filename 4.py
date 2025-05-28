import two

def decor(f):
    def wrapper(*args, **kwargs):
        print(f'Вызов {f.__name__}')
        try:
            result = f(*args, **kwargs)
            return result
        except Exception as e:
            return f'Исключение: {type(e).__name__} - {e}'
    return wrapper
@decor
def func1(x):
    return two.f1(x)
@decor
def func2(x, y):
    return two.f2(x, y)
@decor
def func3(s):
    return two.f3(s)
@decor
def func4():
    return two.f4()
@decor
def func5(x):
    return two.f5(x)

print(func1(-7))
print(func1(1))
print(func2(2, 2))
two.z = 2
print(func2(2, 2))
print(func3(333))
print(func3('333'))
print(func4())
print(func5(5))