import time

def timer_wrap(fn):
    def internal(*args,**kwargs):
        start_time = time.time()
        res = fn(*args, **kwargs)
        function_time = time.time() - start_time
        print("function {} time {}".format(fn.__name__,function_time))
        return res
    return internal;





def html_decorate(  tag ):
    def internal(fn,*args,**kwargs):
        output = "<"+tag+">"
        output += fn(*args,**kwargs)
        output += "</" + tag + ">"
        return output
    return internal


##main
def loop():
    j=0
    for i in range(1000000):
        j+=1
    print(j)
timer_print = timer_wrap(loop)
timer_print()

def foo(string_val):
    return string_val

strong_decorate = html_decorate('strong')
p_decorate = html_decorate('p')

print(p_decorate(strong_decorate,foo,"a yellow banana"))