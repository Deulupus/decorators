def make_html(tag):
    def decorator(func):
        def wrap(*args,**kwargs):
            return '<'+tag+'>'+func(*args,**kwargs)+'</'+tag+'>'
        return wrap
    return decorator

@make_html('b')
def foo():
    return "hello world!"

print (foo())