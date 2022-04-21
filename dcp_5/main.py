def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(cns):
    if cns == None:
        return None
    return cns(lambda x,y :x )

def cdr(cns):
    if cns == None:
        return None
    return cns(lambda x,y :y )

print(car( cons(1,2)))
print(cdr( cons(1,2)))
print(car(cdr( cons(1,cons(2,3)))))
print(cdr(cdr( cons(1,cons(2,3)))))

