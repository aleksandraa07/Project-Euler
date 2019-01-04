
def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = float((te - ts) * 1000)
        else:
            print('%r  %2.2f ms' % \
                  (method.__name__, (te - ts) * 1000))
        return result
    return timed
@timeit
def even_fib(limit):
    a, b = 0, 1
    while a < limit:
        if not a % 2:
            yield a
        a, b = b, a + b


@timeit
def fibonacci(n):
    x=1
    y=1
    even_sum = 0
    new_element=0
    if n==0:
        return 0
    if n==1:
        return 0
    while new_element <4000000:
        new_element = x + y
        # if new_element%3 ==0:
        #     even_sum+=new_element
        x=y
        y=new_element

   # print(even_sum)

fibonacci(4000000)
even_fib(4000000)
