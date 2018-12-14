def call_counter(func):
    def counter(*args,**kwargs):
        counter.calls += 1
        return func(*args,**kwargs)
    counter.calls=0
    return counter

@call_counter
def succ(x):
    return x+1

for i in range(20):
    succ(i)

print (succ.calls)