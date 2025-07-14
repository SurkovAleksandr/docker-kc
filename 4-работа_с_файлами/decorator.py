def decorator_function(name=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f'there are {len(args)} positional arguments and {len(kwargs)} keyword arguments')
            print(f"До вызова функции {name}")
            func(*args, **kwargs)
            print(f"После вызова функции {name}")
            return len(name)
        return wrapper
    return decorator

@decorator_function(name="Alex")
def say_hello(age1, age2, name1='Ben', name2='Harry'):
    print(f"Hello! {age1}")

length = say_hello(12, 15, name1="Lily", name2="Ola")
print(f"Длина имени: {length}")

