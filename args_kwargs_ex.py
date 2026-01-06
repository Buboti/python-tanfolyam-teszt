def summarize(*args):
    return sum(args)

print(summarize(1, 2, 3))
print(summarize(4, 5, 6, 7, 8, 9))

def ex_fn(**kwargs):
    for k, v in kwargs.items():
        print(f'{k}: {v}')

ex_fn(nev='Elek', kor=22, varos='Budapest')

def ex_fn2(item, *args, **kwargs):
    print(f'Parameter: {item}')
    print('Args argumentum: ' , args)
    print('A kwargs argumentum: ', kwargs)

ex_fn2('Alma', 1,2,3, nev='Jakab', kor=55)

def receive(*args, **kwargs):
    print('Args: ', args)
    print('Kwargs: ', kwargs)

def send(*args, **kwargs):
    receive(*args, **kwargs)

send(1,2,3, nev='Jakab', kor=55)
