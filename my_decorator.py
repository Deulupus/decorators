"""
Честно - не было ни единой идеи как еще использовать декораторы кроме как в примерах приведённых на практической.
Декоратор возводит переданное функцией значение в названную степень.
"""
def increase(deg):
    def decorator(func):
        def wrap(*args, **kwargs):
            result = func(*args, **kwargs)
            return result ** deg
        return wrap
    return decorator

@increase(5)
def foo(x):
    return x

print (foo(10))
